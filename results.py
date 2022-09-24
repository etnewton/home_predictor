from parcel_extract import Parcel_Information

import csv

home = Parcel_Information("parcel address was here", "address", "tbd", "tbd")

parcels = []

with open('file_path_here', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    next(reader,None)
    for row in reader:
        new_parcel = Parcel_Information(row[0], row[1], row[2], row[3])
        parcels.append(new_parcel.get_info())

with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = list(parcels[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(home.get_info())
    for i in parcels:
        writer.writerow(i)

