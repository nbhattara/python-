from .record import TemperatureRecord
from .converter import convert
from .analytics import (
    average_temperature_across_days,
    hottest_day,
    detect_extreme_days,
    temperature_range_for_each_day,
    temperature_trend,
    detect_spike
)

__all__ = [
    'TemperatureRecord',
    'convert',
    'average_temperature_across_days',
    'hottest_day',
    'detect_extreme_days',
    'temperature_range_for_each_day',
    'temperature_trend',
    'detect_spike'
]