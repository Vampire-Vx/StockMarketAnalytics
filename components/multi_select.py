from dash import dcc

def create_multi_select(
    id: str, 
    options: list,
    value: list = None,
    placeholder: str = None) -> dcc.Dropdown:
    multi_select = dcc.Dropdown(
                        id=id,
                        options=options,
                        value=value,
                        multi=True,
                        placeholder=placeholder,
                        clearable=False,
                        className='p-1 w-100 dbc',
                    )
    return multi_select