from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D """
    # Build station list
    stations = build_station_list()
    # Build river list
    rivers = rivers_with_station(stations)
    # First deliverable
    print(len(rivers))
    print(sorted(list(rivers))[:10])

    # Build dictionary
    river_station_dict = stations_by_river(stations)
    # Second deliverable
    print("River Aire:")
    print(river_station_dict["River Aire"])
    print("River Cam:")
    print(river_station_dict["River Cam"])
    print("River Thames:")
    print(river_station_dict["River Thames"])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()