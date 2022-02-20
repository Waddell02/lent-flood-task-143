from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Generates a list of tuples with the station name and relative water level, in order of most to least risk"""
    risk_list = []
    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                risk_list.append((station, station.relative_water_level()))
    return sorted_by_key(risk_list, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    """Builds a list of the N stations with the highest relative water level"""
    risk_list = []
    for n in range(0, N):
        risk_list.append(stations_level_over_threshold(stations, -999999)[n])
    return risk_list

