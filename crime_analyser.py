
# This script outputs a list of crime types and their average count per month
# for any given area (in this case, Norwich 007E) from Oct 2020 to Sept 2023. You can change the area and time period
# by changing the folder_path variable in the for loop.

# Download the data from https://data.police.uk/data/ and extract it to a folder.

import os
import csv
from collections import defaultdict

crime_counts = defaultdict(int)
total_months = 0
matched_records = 0
total_crimes = 0

# Lower layer Super Output Areas - this is the lowest level of geography that the data is available for
# Get the LSOA from https://data-communities.opendata.arcgis.com/datasets/6bced6c6f81448cf9692ed3f472b11ce/explore?location=52.636587%2C1.294561%2C16.76
# Uses the same as Index of Multiple Deprivation 2019 data

lsoa_code_to_filter = "Norwich 007A"

# Anglia Square: 007E


# main loop for all folders from Oct 2020 to Septmber 2023
for year in range(2020, 2024):
    for month in range(10, 13) if year == 2020 else range(1, 10):
        folder_path = f"D:\\Downloads\\111e972c53e9f130d6716ff42d2b89ae171d64dc\\{year:04d}-{month:02d}"  # change this from hardcode to input
        file_path = os.path.join(folder_path, f"{year:04d}-{month:02d}-norfolk-street.csv")

        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                csvreader = csv.reader(csvfile)
                next(csvreader)  # Skip header row
                for row in csvreader:
                    lsoa_code = row[8]  # Column I - LSOA code
                    crime_type = row[9]  # Column J - Crime type

                    if lsoa_code == lsoa_code_to_filter:
                        crime_counts[crime_type] += 1
                        matched_records += 1
                        total_crimes += 1
                    else:
                        total_crimes += 1

            total_months += 1

# dict comprehension to get the average crime count per month in a ncie format
average_crime_counts = {crime_type: count / total_months for crime_type, count in crime_counts.items()}
sorted_crime_counts = dict(sorted(crime_counts.items(), key=lambda item: item[1], reverse=True))

# for the end stats
average_count_total = sum(average_crime_counts.values()) / len(average_crime_counts)
total_crime_count = sum(crime_counts.values())

print("\n\nAnalytics:")
print(f"Found {matched_records:,} crime records across {total_months} months.")
print(f"{len(crime_counts)} different crime types matched the LSOA code {lsoa_code_to_filter}.")
print(f"Total crimes in Norfolk: {total_crimes:,}\n\n")

print("Crime Type\t\t\tTotal Count\t\tAverage crimes/month")
print("-----------------------------------------------------------------------------")
for crime_type, count in sorted_crime_counts.items():
    average_count = average_crime_counts[crime_type]
    print(f"{crime_type.ljust(31)}{count}\t\t\t{average_count:.2f}")

print(f"\n{total_crime_count:,} crimes in total, average of {(total_crime_count/total_months):.2f} crimes per month.")
