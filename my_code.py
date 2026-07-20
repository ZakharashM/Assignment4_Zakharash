import csv
import json
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
print(regional_tariffs)
print(sales)