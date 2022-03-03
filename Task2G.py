from concurrent.futures.process import _system_limited
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import warning
import operator

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations_over_threshold_tuplets = stations_level_over_threshold(stations, 1.5)
    stations_over_threshold = []
    towns_in_danger = {}

    for station_list in range(len(stations_over_threshold_tuplets)):
        for station in stations:
            if station == stations_over_threshold_tuplets[station_list][0]:
                    stations_over_threshold.append(station)
                    break
    
    warning(stations_over_threshold)

    for station in stations_over_threshold:
        if station.town not in towns_in_danger:
            towns_in_danger[station.town] = station.warning_level
        else:
            if station.warning_level > towns_in_danger[station.town]:
                towns_in_danger[station.town] = station.warning_level
    
    no_risk_towns = []

    for town in towns_in_danger:
        if towns_in_danger[town] == 4:
            towns_in_danger[town] = "Severe"
        elif towns_in_danger[town] == 3:
            towns_in_danger[town] = "High"
        elif towns_in_danger[town] == 2:
            towns_in_danger[town] = "Moderate"
        elif towns_in_danger[town] == 1:
            towns_in_danger[town] = "Low"
        elif towns_in_danger[town] == None:
            no_risk_towns.append(town)

    for town in no_risk_towns:
        del towns_in_danger[town]
    
    sorted_towns_in_danger = sorted(towns_in_danger.items(), key=operator.itemgetter(1),reverse=True)
        
    for town in sorted_towns_in_danger:    
        print("Town name:", town[0])
        print("Warning level:", town[1])
        print("")

run()
