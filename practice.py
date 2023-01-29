import matplotlib.pyplot as plt
import csv

file = "/Users/tomcheung/Downloads/Bank - Agency - data.csv"

data = open(file, encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

bank_shifts = [int(_[1]) for _ in data_lines[1:61]]
agency_shifts = [int(_[2]) for _ in data_lines[1:61]]
month = [_[0] for _ in data_lines[1:61]]

fig, ax = plt.subplots()

ax.plot(month, bank_shifts, agency_shifts, linewidth=2)


ax.set_title("Bank and agency shifts", fontsize=10)
ax.set_xlabel("Month", fontsize=10)
ax.set_ylabel("Shifts", fontsize=10)
ax.tick_params(axis="both", labelsize=5)

plt.show()