from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""
    # Build list of stations
    stations = build_station_list()
    # Update water level data
    update_water_levels(stations)
    risk_list = stations_level_over_threshold(stations, 0.8)
    for station, level in risk_list:
        print(station.name, level)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()