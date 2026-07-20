import csv
import json
import pandas as pd
import matplotlib.pyplot as plt

with open("global_sales.csv", "r", encoding="utf-8") as file:
    sales = list(csv.DictReader(file))
with open("regional_tariffs.json","r", encoding="utf-8") as file:
    regional_tariffs = json.load(file)
for item in sales:
    if item["quantity"] == "N/A":
        item["quantity"] = 0
    if item["revenue"] == "N/A":
        item["revenue"] = 0
    item["quantity"] = int(item["quantity"])
    item["revenue"] = float(item["revenue"])
for key,value in regional_tariffs.items():
    if regional_tariffs[key] == "N/A":
        regional_tariffs[key] = 0
for sale in sales:
    for key,value in regional_tariffs.items():
        if sale["region"] == key:
            sale["net_profit"] = sale["revenue"] - (sale["revenue"]*(value/100))
            sale["net_profit"] = round(sale["net_profit"],2)
# with open("cleaned_sales_updated.csv", "w", encoding="utf-8", newline="") as file:
#     columns = list(sales[0].keys())
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(sales)

sum_net_profit = {}
for sale in sales:
    if sale["product_category"] not in sum_net_profit:
        sum_net_profit[sale["product_category"]] = 0
for sale in sales:
    value = sale["net_profit"]
    sum_net_profit[sale["product_category"]] += value
    sum_net_profit[sale["product_category"]] = round(sum_net_profit[sale["product_category"]],2)
sum_of_all_net_profits = 0
for key,value in sum_net_profit.items():
    sum_of_all_net_profits += value
average_net_profit = sum_of_all_net_profits / len(sum_net_profit)
average_net_profit = round(average_net_profit,2)
sums_more_than_average = [key for key,value in sum_net_profit.items() if value > average_net_profit]
top_categories = [(key, value) for key,value in sum_net_profit.items() if value > average_net_profit]
top_categories.sort(key=lambda x: x[1], reverse=True)
top_categories = dict(top_categories)
print(top_categories)

# with open("top_categories.json", "w", encoding="utf-8") as file:
#     json.dump(top_categories, file, ensure_ascii=False, indent=4)

top_table = pd.DataFrame(top_categories.items(), columns=["Category", "Total net profit"])
print(top_table)

