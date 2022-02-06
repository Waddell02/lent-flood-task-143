from floodsystem.geo import rivers_with_station, stations_by_distance, stations_within_radius, stations_by_river, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
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

def test_rivers_by_station_number():
    """1E test"""
    # Create test data
    stations = []
    stations.append(MonitoringStation("test-s-id-1", "test-m-id-1", "1", (0,1), (1,2), "river-1", ""))
    stations.append(MonitoringStation("test-s-id-2", "test-m-id-2", "2", (0,2), (1,2), "river-2", ""))
    stations.append(MonitoringStation("test-s-id-3", "test-m-id-3", "3", (0,1.5), (1,2), "river-2", ""))
    stations.append(MonitoringStation("test-s-id-4", "test-m-id-4", "4", (0,-1.75), (1,2), "river-3", ""))

    rivers_stations_number = rivers_by_station_number(stations, 1)
    # Test for rivers with the same number of stations will be returned
    assert rivers_stations_number[0][1] == 2

    # General testing
    rivers_stations_number = rivers_by_station_number(stations, 2)
    assert len(rivers_stations_number) == 3
