import dash_ag_grid as dag

def create_table(id: dict, columns: list, data: list) -> dag.AgGrid:
    table = dag.AgGrid(
        id=id,
        rowData=data,
        columnDefs=columns,
        defaultColDef={
            "flex": 1,
            "minWidth": 100,
            "resizable": True,
        },
        style={"height": "400px", "width": "100%"},
        className="ag-theme-alpine-dark",
    )
    return table