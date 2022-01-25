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
        distance_list += (station, haversine(p, station.coord))
    # Sort list using existing function
    return sorted_by_key(distance_list, 1)
    
