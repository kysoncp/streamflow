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

    # Excel values for 10163000:
    # MAX = 131 cfs
    # AVERAGE = 56.95 cfs

# this first line of code prints headers for our table
    print(f"{'Gauge':<10} {'Max (cfs)':>10} {'Date of max':>20} {'Min (cfs)':>10} {'Avg (cfs)':>10}")

# now we are going to open and write a file called streamflow_summary.csv
# we are also going to add the same headers to this file 
    with open("streamflow_summary.csv", "w") as file:
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

# now we are looping through our different sites, to calculate
# our max, min and average for each
        for i in range(len(sites)):
            max_flow = np.max(flows[:, i])
            min_flow = np.min(flows[:, i])
            avg_flow = np.mean(flows[:, i])

# now we are going to find the index of the max flow,
# and then use that index to find the date of the max flow
            max_index = np.argmax(flows[:, i])
            max_date = dates[max_index]

# now we print off the results for each site
            print(
                f"{sites[i]:<10} "
                f"{max_flow:10.1f} "
                f"{str(max_date):>20} "
                f"{min_flow:10.1f} "
                f"{avg_flow:10.1f}"
            )

# and we also add it to our file
            file.write(
                f"{sites[i]},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n"
            )

# first we ask for the user input, to determine what
# our threshold is 
threshold = float(input("Enter a flow threshold (cfs): "))

print(f"\nHours above {threshold} cfs:")

# now we are going to loop through our sites, and calculate
# how many hours the flow was above our threshold
# we're doing this with a simple greater than inside our loop
# we multiply our sum by 0.25 to get it in hours
for i in range(len(sites)):
    above_threshold = flows[:, i] > threshold
    hours = np.sum(above_threshold) * 0.25

    print(f"{sites[i]}: {hours:.2f} hours")

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