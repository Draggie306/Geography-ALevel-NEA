import csv
import time
import time
import math
import pandas as pd
from scipy.stats import spearmanr

# Read data from File 1 and File 2
file1_data = []
file2_data = []

unknown_postcodes = 0
valid_postcodes = 0
notfound_postcodes = []

valid_distances = 0


def log(msg):
    time.sleep(0.001)
    print(f"{msg}")


with open(r"D:\OneDrive - Notre Dame High School\SpearmanPostcodes.csv", 'r') as file1:
    reader = csv.reader(file1)
    for row in reader:
        try:
            file1_data.append(row)
        except Exception as e:
            log(f"\tERROR: {e}")
            file1_data.append("err")

with open(r"D:\OneDrive - Notre Dame High School\nr.csv", 'r') as file2:
    reader = csv.reader(file2, delimiter=',')
    for row in reader:
        file2_data.append(row)

#  dictionary to store eastings and northings data from File 2
postcode_data = {}
for row in file2_data:
    postcode, eastings, northings = row[0], row[2], row[3]
    postcode_data[postcode] = (eastings, northings)

# update eastings/northings data in file 1
for row in file1_data:
    postcode = row[0]
    if postcode.lower() == 'n/a':
        row[1] = 'unk'
        row[2] = 'unk'
    else:
        try:
            first_part = postcode.split()[0].upper()
            second_part = '1AA' if len(postcode) < 6 else postcode.split()[1].upper() # exception will be called if no postcode
            log(f"log: postcode: {postcode}, second_part: {second_part}")
            full_postcode = f"{first_part} {second_part}"
            try:
                if postcode_data[full_postcode]:
                    log(f"log: postcode: {postcode} found in postcode_data")
                    row[1] = postcode_data[full_postcode][0]
                    row[2] = postcode_data[full_postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
            except KeyError as e:
                log(f"keyerror: {e} is not in postcode_data")
                # if it starts with NR14
                postcode = postcode.split()[0].upper()
                # too lazy to do this properly with subroutines
                if postcode.upper().startswith('NR14'):
                    postcode = "NR14 7PZ"
                    log(f"log: swicthed nr14 postcode: {postcode} starts with NR14")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper().startswith('NR8'):
                    postcode = "NR8 6HW"
                    log(f"log: postcode: {postcode} starts with NR8")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper().startswith('NR5'):
                    postcode = "NR5 0PX"
                    log(f"log: postcode: {postcode} starts with NR5")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper().startswith('NR6'):
                    postcode = "NR6 5NF"
                    log(f"log: postcode: {postcode} starts with NR6")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper().startswith('NR4'):
                    postcode = "NR4 7TJ"
                    log(f"log: postcode: {postcode} starts with NR4")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper().startswith('NR13'):
                    postcode = "NR13 6JY"
                    log(f"log: postcode: {postcode} starts with NR13")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper().startswith('NR2'):
                    postcode = "NR2 4SX"
                    log(f"log: postcode: {postcode} starts with NR2")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper().startswith('NR11'):
                    postcode = "NR11 6JG"
                    log(f"log: postcode: {postcode} starts with NR11")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper().startswith('NR10'):
                    postcode = "NR10 3JU"
                    log(f"log: postcode: {postcode} starts with NR10")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]} for postcode: {postcode}")
                    valid_postcodes += 1
                elif postcode.upper() == 'NR7':
                    postcode = "NR7 8RN"
                    log(f"log: postcode: {postcode} is NR7")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]}")
                    valid_postcodes += 1
                elif postcode.upper() == 'NR9':
                    postcode = "NR9 3DL"
                    log(f"log: postcode: {postcode} is NR9")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]}")
                    valid_postcodes += 1
                elif postcode.upper() == 'NR18':
                    postcode = "NR18 0QW"
                    log(f"log: postcode: {postcode} is NR18")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: northings: {row[1]}, eastings: {row[2]}")
                    valid_postcodes += 1
                elif postcode.upper() == 'NR32':
                    postcode = "NR32 2NB"
                    log(f"log: postcode: {postcode} is NR32")
                    row[1] = postcode_data[postcode][0]
                    row[2] = postcode_data[postcode][1]
                    log(f"log: {row[1]}, {row[2]}")
                    valid_postcodes += 1    
                else:
                    log(f"\tERROR - unknown postcode: {postcode}")
                    row[1] = 'unk'
                    row[2] = 'unk'
                    unknown_postcodes += 1
                    notfound_postcodes.append(postcode)
        except Exception as e:
            log(f"\tERROR: {e}")
            row[1] = 'err'
            row[2] = 'err'
            unknown_postcodes += 1
            notfound_postcodes.append(postcode)

filename = f"z:\\data_{time.strftime('%Y%m%d-%H%M%S')}.csv"
# Write updated data back to File 1
with open(filename, 'w', newline='') as updated_file:
    writer = csv.writer(updated_file)
    writer.writerows(file1_data)

log(f"Data updated and saved to {filename}")

# now compute distance between two points

log("info: now computing distance between two points")

AngliaSquareEastings = 623068
AngliaSquareNorthings = 309381


def compute_distance(easting1, northing1, easting2, northing2):
    dx = easting2 - easting1
    dy = northing2 - northing1
    distance = math.sqrt(dx**2 + dy**2)
    return distance


distances = []  # List to store computed distances

with open(filename, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)  # Read data into a list
    header = data[0]  # Extract header row
    header.append("Distance")  # Add a new column header for distances
    distances.append(header)  # Add header row to distances list

    for row in data[1:]:
        postcode = row[0].strip()
        easting = row[1]
        northing = row[2]

        try:
            if int(easting) and int(northing):
                log(f"info: postcode: {postcode} has valid easting and northing")
                easting = int(easting)
                northing = int(northing)

                distance = compute_distance(AngliaSquareEastings, AngliaSquareNorthings, easting, northing)
                row.append(distance)  # Add distance to the current row
                distances.append(row)  # Add updated row to distances list
                valid_distances += 1
        except Exception as e:
            log(f"\tERROR: {e}")
            row.append("")  # Add a placeholder for invalid data
            distances.append(row)  # Add updated row to distances list

# Write the distances list back to the CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(distances)

log("Distances have been written to the CSV file.") 

log(f"Stats:\n\n\tValid Postcodes: {valid_postcodes}\n\tUnknown Postcodes: {unknown_postcodes}\n\tValid Distances: {valid_distances}")
log(f"\n\nNot found postcodes:\n\n{notfound_postcodes}")


data = {
    'OverallScore': ['2', '4', '6', '3', '5', '5', '2', '6', '6', '5', '5', '4', '3', '4', '7', '4', '3', '4', '1', '1', '1', '5', '5', '1', '6', '1', '6', '4', '7', '2', '2', '9', '9', '4', '6', '4', '4', '5', '7', 
'2', '3', '3', '1', '5', '6', '6', '1', '2', '3', '3', '8', '7', '6', '8', '4', '2', '1', '2', '7', '3', '5', '1', '6', '4', '6', '1', '8', '3', '5', '1', '5', '7', '1', '4', '5', '4', '4', '4', '8', '5', '3', '7', '3', '5', '7', '7', '5', '6', '6', '1', '2', '5', '9', '5', '5', '5', '3', '3', '4', '3', '3', '7', '9', '1', '2', '2', '4', '3', '6', '3', '6', '4', '4', '7', '1', '8', '1', '5', '5', '5', '3', '4', '5', '1', '3', '3', '1', '7', '5', '3', '3', '7', '4', '5', '3', '5', '7', '9', '3', '3', '5', '6', '1', '5', '8', '4', '7', '1', '7', '3', '1', '7', '4', '8', '2', '7', '7', '3', '4', '5', '2', '5', '8', '2', '6', '2', '3', '4', '2', '2', '3', '5', '2', '1', '5', '3', '7', '8', '2', '6', '3', '4', '4', '2', '8', '10', '7'],  # Fill in the complete list of OverallScore values
    'Distance': ['3961.039889', '3961.039889', '1438.355311', '6042.9511', '664.1084249', '2291.757622', '104.5466403', '14120.77052', '34914.86418', '5589.213272', '10064.88356', '7713.403723', '1438.355311', '17052.88304', '14762.72935', '1438.355311', '17612.29025', '1438.355311', '6690.094469', '6690.094469', '32826.16903', '5589.213272', '3916.674227', '664.1084249', '6690.094469', '664.1084249', '104.5466403', '5589.213272', '3384.663794', '2860.534391', '104.5466403', '104.5466403', '598.0008361', '104.5466403', '14762.72935', '1438.355311', '9225.197776', '664.1084249', '104.5466403', '6033.056025', '3961.039889', '9225.197776', '1438.355311', '9225.197776', '3916.674227', '1650.709242', '1060.317405', '1438.355311', '3961.039889', '24289.47509', '1589.637695', '104.5466403', '664.1084249', '104.5466403', '24369.48528', '3961.039889', '104.5466403', '5589.213272', '664.1084249', '3916.674227', '10064.88356', '3939.889973', '2154.417323', '8698.684096', '104.5466403', '664.1084249', '104.5466403', '6033.056025', '664.1084249', '104.5466403', '22176.08667', '9225.197776', '6042.9511', '5589.213272', '1438.355311', '3939.889973', '378.208937', '386.9185961', '2401.068096', '2019.546979', '6033.056025', '3916.674227', '3939.889973', '10064.88356', '9225.197776', '3939.889973', '664.1084249', '664.1084249', '1438.355311', '1438.355311', '9225.197776', '5589.213272', '453.1942189', '6033.056025', '3969.513446', '6690.094469', '14120.77052', '104.5466403', '3961.039889', '9225.197776', '1438.355311', '9225.197776', '104.5466403', '104.5466403', '6033.056025', '3916.674227', '4049.060138', '664.1084249', '104.5466403', '5095.677384', '664.1084249', '104.5466403', '1438.355311', '14120.77052', '1624.054494', '644.4850658', '724.4101048', '6690.094469', '3961.039889', '8210.921081', '6631.95484', '6690.094469', '6690.094469', '6690.094469', '664.1084249', '6690.094469', '1438.355311', '6690.094469', '6690.094469', '6690.094469', '6690.094469', 
'11287.15522', '9225.197776', '6690.094469', '3916.674227', '6690.094469', '11729.75541', '8697.184947', '6690.094469', '6690.094469', '6690.094469', '6690.094469', '6690.094469', '6690.094469', '9082.37513', '3939.889973', '1438.355311', '6690.094469', '8419.777016', '7299.912671', '11287.15522', '6690.094469', '104.5466403', '11728.33599', '6690.094469', '6690.094469', '1438.355311', '1438.355311', '3939.889973', '6690.094469', '6690.094469', '6690.094469', '6690.094469', '6690.094469', '1436.412893', '6690.094469', '6690.094469', '11287.15522', '24042.59797', '6690.094469', '2059.423463', '1438.355311', '664.1084249', '7781.273996', '8610.750954', '29288.59498', '1589.426626', '6690.094469', '6690.094469', '104.5466403', '104.5466403', '6690.094469', '7062.685962', '1398.661146', '1438.355311', '3916.674227', '2997.971481']  # Fill in the complete list of Distance values
}

# dataframe from data dict
df = pd.DataFrame(data)

# calc spearman's rank correlation coefficient
correlation, _ = spearmanr(df['OverallScore'], df['Distance'])

log(f"\nFINAL RESULT\n\nSpearman's Rank Correlation Coefficient: {correlation}")

log(f"Degrees of Freedom: {len(data['OverallScore']) - 2}")
log(f"Degrees of Freedom: {len(data['Distance']) - 2}")

data = """
3961.039889
3961.039889
1438.355311
6042.9511

664.1084249
2291.757622

104.5466403
14120.77052
34914.86418
5589.213272
10064.88356
7713.403723
1438.355311
17052.88304
14762.72935
1438.355311
17612.29025
1438.355311
6690.094469
6690.094469
32826.16903


5589.213272

3916.674227
664.1084249

6690.094469
664.1084249

104.5466403
5589.213272
3384.663794
2860.534391
104.5466403
104.5466403
598.0008361
104.5466403
14762.72935


1438.355311

9225.197776
664.1084249
104.5466403
6033.056025
3961.039889
9225.197776
1438.355311
9225.197776


3916.674227
1650.709242

1060.317405
1438.355311
3961.039889
24289.47509
1589.637695
104.5466403
664.1084249
104.5466403
24369.48528
3961.039889
104.5466403
5589.213272



664.1084249
3916.674227
10064.88356
3939.889973
2154.417323
8698.684096
104.5466403

664.1084249
104.5466403
6033.056025
664.1084249
104.5466403
22176.08667

9225.197776
6042.9511
5589.213272

1438.355311
3939.889973
378.208937
386.9185961

2401.068096
2019.546979
6033.056025
3916.674227
3939.889973
10064.88356

9225.197776
3939.889973

664.1084249
664.1084249
1438.355311
1438.355311
9225.197776

5589.213272
453.1942189
6033.056025
3969.513446

6690.094469
14120.77052
104.5466403
3961.039889
9225.197776
1438.355311

9225.197776

104.5466403
104.5466403
6033.056025
3916.674227
4049.060138
664.1084249
104.5466403
5095.677384
664.1084249
104.5466403
1438.355311
14120.77052
1624.054494
644.4850658
724.4101048
6690.094469
3961.039889
8210.921081
6631.95484
6690.094469
6690.094469
6690.094469
664.1084249
6690.094469
1438.355311
6690.094469
6690.094469
6690.094469

6690.094469
11287.15522
9225.197776
6690.094469
3916.674227
6690.094469
11729.75541
8697.184947
6690.094469
6690.094469
6690.094469
6690.094469
6690.094469
6690.094469
9082.37513
3939.889973
1438.355311

6690.094469
8419.777016
7299.912671
11287.15522
6690.094469
104.5466403
11728.33599
6690.094469
6690.094469


1438.355311
1438.355311
3939.889973
6690.094469
6690.094469
6690.094469

6690.094469

6690.094469
1436.412893
6690.094469
6690.094469
11287.15522
24042.59797
6690.094469
2059.423463
1438.355311
664.1084249
7781.273996
8610.750954
29288.59498
1589.426626
6690.094469

6690.094469
104.5466403
104.5466403

6690.094469
7062.685962
1398.661146
1438.355311
3916.674227
2997.971481




"""

# uncomment to generate a list from the data string if needed
"""data = data.splitlines()
data = [x for x in data if x]
log(data)"""