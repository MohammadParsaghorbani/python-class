import csv

rows = []
ston = []
many = int(input("hpw many rows? "))
for i in range (many):
    row_name = input(f"enter row {i+1}: ")
    rows.append(row_name)
with open("data.csv" , "w" , encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(rows)
    for i in rows:
        s_value = input(f"what is your value for {i}?")
        ston.append(s_value)
    writer.writerow(ston)
        