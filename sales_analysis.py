import csv

sales_numbers = []
days = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        days.append(row["day"])
        sales_numbers.append(int(row["sales"]))

total_sales = sum(sales_numbers)
average_sales = total_sales / len(sales_numbers)

best_sale = max(sales_numbers)
worst_sale = min(sales_numbers)

best_day = days[sales_numbers.index(best_sale)]
worst_day = days[sales_numbers.index(worst_sale)]

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Best Day:", best_day, best_sale)
print("Worst Day:", worst_day, worst_sale)
