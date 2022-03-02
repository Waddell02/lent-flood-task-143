from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from random import choice
from datetime import datetime, timedelta
import numpy as np

stations = build_station_list(use_cache=True)
update_water_levels(stations)

station = choice(stations)

def test_polyfit():
    dt = 10
    degree = 4
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, degree)
    assert poly
    assert d0