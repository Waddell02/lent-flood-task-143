from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime

def run():
    N = 5
    stations = build_station_list()
    update_water_levels(stations)
    stations_with_highest_levels_list = stations_highest_rel_level(stations, N)
    dt = 10
    stations_with_highest_levels = []

    for station_list in range(len(stations_with_highest_levels_list)):
        for station in stations:
            if station == stations_with_highest_levels_list[station_list][0]:
                stations_with_highest_levels.append(station)
                break
    print(stations_with_highest_levels)

    for station in stations_with_highest_levels:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station.name, dates, levels)

if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()

