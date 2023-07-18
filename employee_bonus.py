import csv

with open("employeePay.csv","r") as input_file:

    reader = csv.reader(input_file)

    for row in reader:
        dep = row[0]
        fname = row[1]
        lname = row[2]
        salary = row[3]
        bonus = row[4]


        print(f"Department: {dep}")
        print(f"First Name: {fname}")
        print(f"Last Name: {lname}")
        print(f"Salary: {salary}")
        print(f"Bonus: {bonus}")
