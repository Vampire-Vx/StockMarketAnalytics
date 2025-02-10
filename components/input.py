from dash import dcc

def create_numeric_input(id: str, min: float, max: float, step: float, value: float) -> dcc.Input:
    numeric_input = dcc.Input(
        id=id,
        type="number",
        min=min,
        max=max,
        step=step,
        value=value,
        debounce=True,
        style={
            "width": "100%",
            "height": "48px",
            "padding": ".375rem .75rem",
            "fontSize": "1rem",
            "lineHeight": "1.5",
            "border": "none",
            "textAlign": "center"
        },
        className="form-control bg-primary text-light" 
    )
    return numeric_input