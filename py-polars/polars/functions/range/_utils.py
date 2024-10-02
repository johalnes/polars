from __future__ import annotations

from datetime import timedelta
from typing import Union, List

from polars._utils.convert import parse_as_duration_string


def parse_interval_argument(interval: Union[str, timedelta, List[Union[str, timedelta]]]) -> List[str]:
    """Parse the interval argument(s) as a list of Polars duration strings."""
    if not isinstance(interval, list):
        interval = [interval]

    parsed_intervals = []
    for intv in interval:
        if isinstance(intv, timedelta):
            parsed_intervals.append(parse_as_duration_string(intv))
        else:
            if " " in intv:
                intv = intv.replace(" ", "")
            parsed_intervals.append(intv.lower())

    return parsed_intervals
