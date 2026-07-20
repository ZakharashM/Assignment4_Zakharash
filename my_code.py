import csv
import json
with open("global_sales.csv", "r", encoding="utf-8") as file:
    sales = list(csv.DictReader(file))
with open("regional_tariffs.json","r", encoding="utf-8") as file:
    regional_tariffs = json.load(file)
print(regional_tariffs)
