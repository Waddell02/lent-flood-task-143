from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

def test_stations_by_distance():
    """Test building list of stations"""
    # Build a list of stations
    stations = build_station_list()
    test_distance_list = stations_by_distance(stations, (52.2053, 0.1218))
    # Test if the function is called
    assert len(test_distance_list) > 0
    # Test if the function is working correctly
    assert test_distance_list[0][0].name == "Cambridge Jesus Lock"

def test_stations_within_radius():
    """Test building list of stations within radius"""
    # Build a list of stations
    stations = build_station_list()
    # Define centre
    centre = (52.2053, 0.1218)
    test_radius_list = stations_within_radius(stations, centre, 10)
    # Test that a list is built
    assert len(test_radius_list) > 0
    # Test that all stations are within the range
    for n in range(len(test_radius_list)):
        assert haversine(centre, test_radius_list[n].coord) < 10