#I fortgot to do one of the Commits, that super my bad so take the points off you need to.
#I used co pilot to help me. I wil add comments wehre it make it and the rest was from my other assignment. 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
def load_streamflow(filename):
    array2 = np.genfromtxt(filename, delimiter=',',dtype=str,skip_header=1)
    x = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in array2[:, 0]]
    return x, array2[:, 1].astype(float), array2[:, 2].astype(float), array2[:, 3].astype(float), array2[:, 4].astype(float), array2[:, 5].astype(float)

#This is the summarize function that will print out the max, min, and average streamflow for each site. It will also write this information to a CSV file called "streamflow_summary.csv".
def summarize(dates, flows, sites):
  print("Gauge        Max (cfs)   Date of max          Min (cfs)   Avg (cfs)")
  with open("streamflow_summary.csv", "w") as summary_file:
    summary_file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")
    for site, flow in zip(sites, flows):
      max_index = np.argmax(flow)
      maximum = np.max(flow)
      minimum = np.min(flow)
      average = np.mean(flow)
      max_date = dates[max_index]
      print(
        f"{site:<12}{maximum:10.1f}   "
        f"{max_date:%Y-%m-%d %H:%M}   {minimum:10.1f}   {average:10.1f}"
      )
      summary_file.write(
        f"{site},{maximum:.1f},{max_date:%Y-%m-%d %H:%M},"
        f"{minimum:.1f},{average:.1f}\n"
      )


def plot_streamflow(dates, flows, sites):
  x, y_1, y_2, y_3, y_4, y_5 = load_streamflow('June-2021-Provo-River-Streamflow-Rates.csv')
  plt.figure(figsize=(10, 6))
  plt.plot(x, y_1, label='Site 10163000')
  plt.plot(x, y_2, label='Site 10155200')
  plt.plot(x, y_3, label='Site 10155500')
  plt.plot(x, y_4, label='Site 10154200')
  plt.plot(x, y_5, label='Site 10155000')
  plt.xlabel('Date')
  plt.ylabel('Streamflow (cfs)')
  plt.title('Provo River Streamflow Data (2021)')
  plt.legend(title='Site Numbers',loc='upper right')
  plt.grid(True)
  plt.xticks(rotation=45)
  plt.show()
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, *flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summarize(dates, flows, sites)
#This is the threshold input that will ask the user to input a flow threshold in cfs. It will then print out the number of hours above that threshold for each site.
threshold = float(input("Enter flow threshold (cfs): "))
print(f"\nHours above {threshold:.1f} cfs:")
for site, flow in zip(sites, flows):
  hours_above_threshold = np.sum(flow > threshold) * 0.25
  print(f"{site}: {hours_above_threshold:.2f} hours")

plot_streamflow(dates, flows, sites)





