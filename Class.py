import csv
import json
import pickle

with open("machine.csv", mode="w", encoding="utf-8") as w_file:
    file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
    file_writer.writerow(["Model", "Year", "Horsepower", "Engine side"])
    file_writer.writerow(["80 1.6 specs", "1989", "69", "1595 cm3 (97.3 cu-in)"])
    file_writer.writerow(["80 1.6 specs", "1993", "102", "1595 cm3 (97.3 cu-in)"])
    file_writer.writerow(["80 1.8 specs", "1986", "75", "1781 cm3 (108.7 cu-in)"])
    file_writer.writerow(["80 1.8 specs", "1989", "90", "1781 cm3 (108.7 cu-in)"])
    file_writer.writerow(["80 1.8 S specs", "1986", "88", "1781 cm3 (108.7 cu-in)"])
    file_writer.writerow(["80 1.8 E specs", "1989", "113", "1847 cm3 (112.7 cu-in)"])
    file_writer.writerow(["80 1.8 E Quatro specs", "1986", "113", "1847 cm3 (112.7 cu-in)"])

with open('machine.csv', 'r', newline='') as w_file:
    reader = csv.reader(w_file, delimiter=';')
    for row in reader:
        print(row)

with open('machine.csv', 'r', newline='') as w_file:
    reader = csv.DictReader(w_file, delimiter=';')
    row = list(reader)

with open('machine.json', 'w', newline='') as w_file:
    json.dump(row, w_file)

with open('machine.json', "r", newline='') as w_file:
    json_w_file = json.load(w_file)

with open("pickle.txt", "wb") as w_file:
    pickle.dump(json_w_file, w_file)

with open("pickle.txt", "rb") as w_file:
    pickle_l = pickle.load(w_file)
