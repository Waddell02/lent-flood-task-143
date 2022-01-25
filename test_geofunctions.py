from floodsystem.geo import rivers_with_station, stations_by_distance, stations_within_radius, stations_by_river
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

# Build station list
stations = build_station_list()

def test_stations_by_distance():
    """Test building list of stations"""
    test_distance_list = stations_by_distance(stations, (52.2053, 0.1218))
    # Test if the function is called
    assert len(test_distance_list) > 0
    # Test if the function is working correctly
    assert test_distance_list[0][0].name == "Cambridge Jesus Lock"


def test_stations_within_radius():
    """Test building list of stations within radius"""
    # Define centre
    centre = (52.2053, 0.1218)
    test_radius_list = stations_within_radius(stations, centre, 10)
    # Test that a list is built
    assert len(test_radius_list) > 0
    # Test that all stations are within the range
    for n in range(len(test_radius_list)):
        assert haversine(centre, test_radius_list[n].coord) < 10

def test_rivers_with_station():
    """1D Unit Test"""
    assert "River Cam" in rivers_with_station(stations)
    assert type(rivers_with_station(stations)) == set

def test_stations_by_river():
    """1D Unit Test"""
    assert "Cambridge Jesus Lock" in stations_by_river(stations)["River Cam"]