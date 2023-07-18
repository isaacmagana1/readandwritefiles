import csv

with open("sales.csv", "r") as old:
    reader = csv.reader(old)

    with open("salesreport.csv", "w", newline='') as n:
        writer = csv.writer(n)
        writer.writerow(["customer_id", "total_sales"])

        for column in reader:
            customer_id = column[0]
            quantity = int(column[1])
            price = float(column[2])
            total_sales = quantity * price

            writer.writerow([customer_id, total_sales])

