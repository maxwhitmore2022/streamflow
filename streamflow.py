
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path


def load_streamflow(filename):
    array2 = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
    x = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in array2[:, 0]]
    flows = [array2[:, column].astype(float) for column in range(1, array2.shape[1])]
    return x, flows


def plot_streamflow(dates, flows, sites):
    plt.figure(figsize=(10, 6))
    for flow, site in zip(flows, sites):
        plt.plot(dates, flow, label=f'Site {site}')
    plt.xlabel('Date')
    plt.ylabel('Streamflow (cfs)')
    plt.title('Provo River Streamflow Data (2021)')
    plt.legend(title='Site Numbers', loc='upper right')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()


sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
filename = Path(__file__).with_name("June-2021-Provo-River-Streamflow-Rates.csv")
dates, flows = load_streamflow(filename)
plot_streamflow(dates, flows, sites)
plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")


