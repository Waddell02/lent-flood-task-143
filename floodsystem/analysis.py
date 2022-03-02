import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates
import numpy as np
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

def polyfit(dates, levels, p):
    ds = matplotlib.dates.date2num(dates)
    d0 = ds[0]
    ds -= d0
    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(ds, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return(poly, d0)