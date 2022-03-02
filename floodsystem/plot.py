import matplotlib.pyplot as plt
import matplotlib
from matplotlib.dates import date2num
import numpy as np
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station)
    plt.tight_layout()

def plot_water_level_with_fit(station, dates, levels, p):
    """ Plot water level vs date for a station, with a best fit polynomial """

    # Plot data
    plt.plot(dates, levels)

    # Evaluate polynomial
    poly, d0 = polyfit(dates, levels, p)

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    ds = date2num(dates)

    x1 = np.linspace(ds[0], ds[-1], 30)
    # Plot polynomial
    plt.plot(x1, poly(x1 - d0))

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station)

    plt.tight_layout()


