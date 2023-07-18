import csv
with open("customers.csv", 'r') as old:
    read= csv.reader(old)

    with open("customer_country.csv", "w") as n:
        write = csv.writer(n)
        for column in read:

            write.writerow(column[1], column[2], column[4])
