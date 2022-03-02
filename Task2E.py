from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime
import matplotlib.pyplot as plt


def run():
    # Build station list
    stations = build_station_list()

    # Update water levels
    update_water_levels(stations)

    # Nested function with variables N, dt and iteration number to delete any stations with inconsistent data
    def iterate(N, dt, i):
        # Build list of tuples with stations with highest levels
        stations_with_highest_levels_list = stations_highest_rel_level(stations, N)
        stations_with_highest_levels = []
        iteration = i

        # Extract list of stations from list of tuples
        for station_list in range(len(stations_with_highest_levels_list)):
            for station in stations:
                if station == stations_with_highest_levels_list[station_list][0]:
                    stations_with_highest_levels.append(station)
                    break
        
        # Remove any stations with any inconsistent data
        if iteration != 0:
            del stations_with_highest_levels[iteration-1]

        # Fetch station level data and plot
        for station in stations_with_highest_levels:
            iteration += 1
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            # Check data inconsistencies and if so reiterate function
            if len(dates) == 0 or len(levels) == 0:
                iterate(N+1, dt, iteration)
                break
            else:
                 plot_water_levels(station, dates, levels)
                 plt.show()
    # Starting parameters for Task
    iterate(5, 10, 0)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

