import dash_bootstrap_components as dbc

def create_alert(id: str, duration: int = 3000) -> dbc.Alert:
    alert = dbc.Alert(
        id=id,
        is_open=False,
        duration=duration,
        dismissable=True,
        children="",
        style={
            "width": "10px + 10vw",
            "height": "5px + 5vw",
            "position": "fixed",
            "top": "50%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",
            "zIndex": "1050"
        }
    )
    return alert