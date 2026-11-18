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
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")

    plt.show()

def summarize(dates, flows, sites):

    print(f"{'Gauge':<10} {'Max (cfs)':>10} {'Date of max':>20} {'Min (cfs)':>10} {'Avg (cfs)':>10}")

    with open("streamflow_summary.csv", "w") as file:
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

        for i in range(len(sites)):
            max_flow = np.max(flows[:, i])
            min_flow = np.min(flows[:, i])
            avg_flow = np.mean(flows[:, i])

            max_index = np.argmax(flows[:, i])
            max_date = dates[max_index]

            print(
                f"{sites[i]:<10} "
                f"{max_flow:10.1f} "
                f"{str(max_date):>20} "
                f"{min_flow:10.1f} "
                f"{avg_flow:10.1f}"
            )

            file.write(
                f"{sites[i]},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n"
            )
  


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
)

plot_streamflow(dates, flows, sites)

# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

plot_streamflow(dates, flows, sites)

summarize(dates, flows, sites)