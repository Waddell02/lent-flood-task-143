from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C """
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    range_list = stations_within_radius(stations, centre, 10)
    modified_range_list = []
    for station in range_list:
        modified_range_list.append(station.name)
    print(sorted(modified_range_list))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()