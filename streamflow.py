# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""

    data = np.genfromtxt(
        filename,
        delimiter=',',
        dtype=str,
        skip_header=1
    )

    dates = data[:, 0].astype('datetime64')
    flows = data[:, 1:6].astype(float)

    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""

    colors = ['purple', 'blue', 'green', 'orange', 'red']

    for i in range(len(sites)):
        plt.plot(dates, flows[:, i], label=sites[i], color=colors[i])

    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.title('Provo River Streamflow Data (2021)')
    plt.grid(True)
    plt.legend(title='Site Numbers', loc='upper right')

    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
)

plot_streamflow(dates, flows, sites)