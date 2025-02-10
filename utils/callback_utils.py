from typing import Tuple

def get_period(period_key: str) -> str:
    period_mapping = {
        'btn-one-month': '1 month',
        'btn-three-months': '3 months',
        'btn-six-months': '6 months',
        'btn-one-year': '1 year',
        'btn-five-years': '5 years',
        'btn-max': 'max'
    }
    return period_mapping.get(period_key, 'max')

def get_volume_range(volume_range_key: str) -> Tuple[int, int]:
    volume_range_mapping = {
        'all': (0, float('inf')),
        'very_high': (5000001, float('inf')),
        'high': (1000001, 5000000),
        'medium': (500001, 1000000),
        'low': (100001, 500000),
        'very_low': (0, 100000),
    }
    return volume_range_mapping.get(volume_range_key, (0, float('inf')))