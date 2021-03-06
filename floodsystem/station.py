# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

        self.warning_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """Check if station has consistent typical range value"""
        # Check if typical_range is None or first value of typical range is greater than the second value and return false if so
        return self.typical_range is not None and self.typical_range[0] <= self.typical_range[1]
    
    def relative_water_level(self):
        """Returns the latest water level as a fraction of the typical range"""
        if self.latest_level != None and self.typical_range_consistent():
            lower, upper = self.typical_range
            return (self.latest_level - lower)/(upper - lower)
        else:
            return None

def inconsistent_typical_range_stations(stations):
    """Returns all stations with inconsistent typical range in a list"""
    # Create a list
    inconsistent_station_data = []
    # Adds all stations with inconsistent typical range to the list
    for station in stations:
        if not station.typical_range_consistent():
            inconsistent_station_data.append(station.name)
    return inconsistent_station_data