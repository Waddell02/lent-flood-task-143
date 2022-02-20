from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    assert stations_level_over_threshold(stations, 0.8)[0][1] > 0.8
    assert stations_level_over_threshold(stations, 0.8)[5][1] > 0.8
    assert stations_level_over_threshold(stations, 0.8)[20][1] > 0.8