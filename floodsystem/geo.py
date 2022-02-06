# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

# a function that, given a list of station objects and a coordinate p
# returns a list of (station, distance) tuples, where distance (float) is the distance
# of the station (MonitoringStation) from the coordinate p. The returned list should be sorted by distance.

def stations_by_distance(stations, p):
    """Returns a list of tuples sorted by distance"""
    # Create empty list
    distance_list = []
    # Add a tuple for every station in stations list using haversine formula
    for station in stations:
        distance = haversine(station.coord, p)
        distance_list.append((station, distance))
    # Sort list using existing function
    return sorted_by_key(distance_list, 1)


def stations_within_radius(stations, centre, r):
    """Returns a list of all stations within radius r of a geographic coordinate x"""
    # Build empty list
    radius_list = []
    # Check if each station is within r of centre
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            radius_list.append(station)
    # No sort required yet
    return radius_list


def rivers_with_station(stations):
    """Returns a set with the names of the rivers with monitoring stations"""
    # Build empty set
    rivers = set()
    # Add the river of every station, and duplicates are removed automatically
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    """Returns a dictionary that maps river names to a list of their respective stations"""
    # Build empty dictionary
    station_river_dict = {}
    # Build river list
    rivers = rivers_with_station(stations)
    # For every river in river list create a list of associated stations
    for river in rivers:
        associated_stations = []
        for station in stations:
            if station.river == river:
                associated_stations.append(station.name)
        # Add to dictionary
        station_river_dict[river] = associated_stations
    return station_river_dict

def rivers_by_station_number(stations, N):
    """Returns a list of (river name, number of stations) tuples, sorted by the number of stations"""
    # Get stations by river dictionary
    station_river_dict = stations_by_river(stations)
    # Create list of tuples wirth river and number of stations associated
    rivers_stations_number = [(river,len(stations)) for river, stations in station_river_dict.items()]
    # Sort list by number of stations
    sorted_list = sorted_by_key(rivers_stations_number, 1, True)

    # Check N isn't higher that list length
    if N+1 > len(sorted_list):
        return sorted_list

    # Get number of stations for Nth river
    number = sorted_list[N-1][1]

    for i in range(N, len(sorted_list)):
        if sorted_list[i][1] < number:
            return sorted_list[:i]
    return sorted_list