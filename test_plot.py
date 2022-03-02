from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def test_plot_water_levels():
    stations = build_station_list()
    update_water_levels(stations)

    # Choose a few random stations and test
    for N in [7, 29, 50, 435]:
        station = stations[N]
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

def test_plot_water_level_with_fit(p):
    stations = build_station_list()
    update_water_levels(stations)

    # Choose a few random stations and test
    for N in [2, 13, 234, 444]:
        station = stations[N]
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, p)