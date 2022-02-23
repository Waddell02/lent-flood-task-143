import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station)
    plt.tight_layout()
    return(plt.show())
