# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    # Test typical_range = None
    assert not MonitoringStation("test-s-id-1", "test-m-id-1", "1", (0,1), None, "", "").typical_range_consistent()
    # Test typical_range = invalid
    assert not MonitoringStation("test-s-id-2", "test-m-id-2", "2", (0,2), (5,2), "", "").typical_range_consistent()
    # Test typical_range = valid
    assert MonitoringStation("test-s-id-3", "test-m-id-3", "3", (0,1.5), (1,2), "", "").typical_range_consistent()

def test_relative_water_levels():
    Hypothetical = MonitoringStation("", "", "test", (0,0), (0, 5), "", "")

    Hypothetical.latest_level = 5
    assert Hypothetical.relative_water_level() == 1

    Hypothetical.latest_level = 0
    assert Hypothetical.relative_water_level() == 0

    Hypothetical.latest_level = 2.5
    assert Hypothetical.relative_water_level() == 0.5