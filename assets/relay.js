window.dash_clientside = Object.assign({}, window.dash_clientside, {

    someApp: {
  
      graphDiv: null,
  
      onRelayout(e) {
        if (
          !e || e.autosize || e.width || e.height ||  // plot init or resizing
          e['yaxis.range'] || e['yaxis.autorange'] || // yrange already adjusted
          e['yaxis.range[0]'] || e['yaxis.range[1]']  // yrange manually set
        ) {
          // Nothing to do.
          return dash_clientside.no_update;
        }
  
        if (!window.dash_clientside.someApp.graphDiv) {
          const selector = '#date-bar-chart .js-plotly-plot';
          window.dash_clientside.someApp.graphDiv = document.querySelector(selector);
        }
  
        const gd = window.dash_clientside.someApp.graphDiv;
  
        if (e['xaxis.autorange']) {
          Plotly.relayout(gd, {'yaxis.autorange': true});
          return dash_clientside.no_update;
        }
  
        // Convert xrange to timestamp so we can easily filter y data.
        const toMsTimestamp = x => new Date(x).getTime();
        const [x0, x1] = gd._fullLayout.xaxis.range.map(toMsTimestamp);
  
        // Filter y data according to the given xrange for each visible trace.
        const yFiltered = gd._fullData.filter(t => t.visible === true).flatMap(t => {
          return gd.calcdata[t.index].reduce((filtered, data) => {
            if (data.p >= x0 && data.p <= x1) {
              filtered.push(data.s0, data.s1);
            }
            return filtered;
          }, []);
        });
  
        const ymin = Math.min(...yFiltered);
        const ymax = Math.max(...yFiltered);
  
        // Add some room if needed before adjusting the yrange, taking account of
        // whether the plot has positive only vs negative only vs mixed bars.
        const room = (ymax - ymin) / 20;
        const yrange = [ymin < 0 ? ymin - room : 0, ymax > 0 ? ymax + room : 0];
  
        Plotly.relayout(gd, {'yaxis.range': yrange});
  
        return dash_clientside.no_update;
      }
    }
  });