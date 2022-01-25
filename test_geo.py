from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

def test_stations_by_distance():
    """Test building list of stations"""
    stations = build_station_list()
    test_distance_list = stations_by_distance(stations, (52.2053, 0.1218))
    assert len(test_distance_list) > 0
    assert test_distance_list[0][0].name == "Cambridge Jesus Lock"

test_stations_by_distance()