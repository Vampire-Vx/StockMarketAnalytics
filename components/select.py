from typing import List, Dict
import dash_bootstrap_components as dbc

def create_select(
    id: str, 
    options: List[Dict[str, str]], 
    value: str = None, 
    placeholder: str = None) -> dbc.Select:
    select = dbc.Select(
                id=id,
                options=options,
                value=value,
                placeholder=placeholder,
                class_name='bg-primary text-light w-100',
            )
    return select