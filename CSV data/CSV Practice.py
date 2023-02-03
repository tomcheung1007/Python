import csv

file = "/Users/tomcheung/Python/CSV data/Employee Details.csv"
data = open(file, encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

# BANK STAFF LOCATION - COUNTY, TOWNS - NESTED DICTIONARY
locations = {
    "berks": {}, "berks_towns": {},
    "bucks": {}, "bucks_towns": {},
    "herts": {}, "herts_towns": {},
}

berks = []
bucks = []
herts = []
other = []

for _ in data_lines[1:]:
    if _[6] == "Berkshire":
        berks.append(_[6])
        locations["berks"].setdefault(_[6], 0)
        berks.append(_[5])
        locations["berks_towns"].setdefault(_[5], 0)

    elif _[6] == "Hertfordshire":
        herts.append(_[6])
        locations["herts"].setdefault(_[6], 0)
        herts.append(_[5])
        locations["herts_towns"].setdefault(_[5], 0)

    elif _[6] == "Buckinghamshire":
        bucks.append(_[6])
        locations["bucks"].setdefault(_[6], 0)
        bucks.append(_[5])
        locations["bucks_towns"].setdefault(_[5], 0)
    else:
        pass
    # Other areas that don't fit within Bucks, Berks, Herts

for _ in berks:
    if _ in locations["berks"]:
        locations["berks"][_] += 1
    elif _ in locations["berks_towns"]:
        locations["berks_towns"][_] += 1
for _ in bucks:
    if _ in locations["bucks"]:
        locations["bucks"][_] += 1
    elif _ in locations["bucks_towns"]:
        locations["bucks_towns"][_] += 1
for _ in herts:
    if _ in locations["herts"]:
        locations["herts"][_] += 1
    elif _ in locations["herts_towns"]:
        locations["herts_towns"][_] += 1

print(locations["berks_towns"])



# AVERAGE AGE OF BANK
age = []
for _ in data_lines[1:]:
    age.append(int(_[4]))

average_age = sum(age) / len(age)

# print(f"\nAverage age of Bank staff: {round(average_age)}")
