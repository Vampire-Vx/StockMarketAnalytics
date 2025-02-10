import dash_bootstrap_components as dbc
import components as cmp

def create_button_group(id: str, buttons: list, color: str, size: str) -> dbc.ButtonGroup:
    button_components = [
        cmp.create_button(id=button['id'], text=button['text'], color=color)
        for button in buttons
    ]
    button_group = dbc.ButtonGroup(
        button_components,
        id=id,
        size=size,
        className='w-100',
        style={'justify-content': 'center'}
    )
    return button_group