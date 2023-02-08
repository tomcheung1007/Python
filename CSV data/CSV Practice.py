import csv
import matplotlib.pyplot as plt
# make csv file accessible
file = "/Users/tomcheung/Python/CSV data/Employee Details.csv"
data = open(file, encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

# BANK STAFF LOCATION - COUNTY, TOWNS - NESTED DICTIONARY
# empty nested dictionary to store info
locations = {
    "berks": {}, "berks_towns": {},
    "bucks": {}, "bucks_towns": {},
    "herts": {}, "herts_towns": {},
    "other": {}, "other_towns": {}
}

# list to store locations. Used later in for loop to count number of staff in each location
berks = []
bucks = []
herts = []
other = []

for _ in data_lines[1:]:
    if _[6] == "Berkshire":
        berks.append(_)
        locations["berks"].setdefault(_[6], 0)  # add instance of county to dictionary
        locations["berks_towns"].setdefault(_[5], 0)  # add instance of town to dictionary
    elif _[6] == "Buckinghamshire":
        bucks.append(_)
        locations["bucks"].setdefault(_[6], 0)
        locations["bucks_towns"].setdefault(_[5], 0)
    elif _[6] == "Hertfordshire":
        herts.append(_)
        locations["herts"].setdefault(_[6], 0)
        locations["herts_towns"].setdefault(_[5], 0)
    else:
        if _[6] != "Berkshire" or "Buckinghamshire" or "Hertfordshire":
            other.append(_)
            locations["other"].setdefault(_[6], 0)
            locations["other_towns"].setdefault(_[6], 0)

# count each item in list and add count to dictionary
for _ in berks:
    if _[6] in locations["berks"]:
        locations["berks"][_[6]] += 1
    if _[5] in locations["berks_towns"]:
        locations["berks_towns"][_[5]] += 1
for _ in bucks:
    if _[6] in locations["bucks"]:
        locations["bucks"][_[6]] += 1
    if _[5] in locations["bucks_towns"]:
        locations["bucks_towns"][_[5]] += 1
for _ in herts:
    if _[6] in locations["herts"]:
        locations["herts"][_[6]] += 1
    if _[5] in locations["herts_towns"]:
        locations["herts_towns"][_[5]] += 1

# AVERAGE AGE OF BANK
overall_age = []
berks_age = []
bucks_age = []
herts_age = []

for _ in data_lines[1:]:
    overall_age.append(int(_[4]))
av_age = sum(overall_age) / len(overall_age)
for _ in berks:
    berks_age.append(int(_[4]))
berks_ave_age = sum(berks_age) / len(berks_age)
for _ in bucks:
    bucks_age.append(int(_[4]))
bucks_ave_age = sum(bucks_age) / len(bucks_age)
for _ in herts:
    herts_age.append(int(_[4]))
herts_ave_age = sum(herts_age) / len(herts_age)


# print(f"Overall average age:\t{round(av_age)}")
# print(f"Overall Berks age:\t{round(berks_ave_age)}")
# print(f"Overall Bucks age:\t{round(bucks_ave_age)}")
# print(f"Overall Herts age:\t{round(herts_ave_age)}")

# AGE OF BANK REPRESENTED IN SCATTER GRAPH
fig, ax = plt.subplots()
ax.scatter(range(0, 157), bucks_age, c="red", s=5)
ax.scatter(range(0, 80), herts_age, c="blue", s=5)
ax.scatter(range(0, 52), berks_age, c="green", s=5)

ax.set_title("Age of Bank Staff", fontsize=15)
ax.set_xlabel("Staff", fontsize=10)
ax.set_ylabel("Age", fontsize=10)

plt.show()

