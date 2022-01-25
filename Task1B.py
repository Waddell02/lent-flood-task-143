from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B """
    # Create the list of stations
    stations = build_station_list()
    # Coordinate for Cambridge City Centre
    p = (52.2053, 0.1218)

    full_distance_list = stations_by_distance(stations, p)
    # Create empty list
    modified_list = []
    # Add station names and towns
    for station, distance in full_distance_list:
        modified_list.append((station.name, station.town, distance))
    # First and last 10 entries converted to strings and printed 
    print("The 10 closest stations are: " + str(modified_list[:10]))
    print("The 10 furthest stations are: " + str(modified_list[-10:]))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()