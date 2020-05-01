import os
import shutil
import csv
import json
import itertools
from collections import OrderedDict

try:
    shutil.rmtree(os.path.join("initdb", "csv"))
except FileNotFoundError:
    pass

os.mkdir(os.path.join("initdb", "csv"))

with open(os.path.join("initdb", "json", "people.json")) as f:
    records = json.load(f)
    employees = []
    favourite_food = []
    friends = []
    for record in records:
        employee = OrderedDict()
        employee["index"] = record["index"]
        employee["name"] = record["name"]
        employee["age"] = record["age"]
        employee["address"] = record["address"]
        employee["phone"] = record["phone"]
        employee["eyeColor"] = record["eyeColor"]
        employee["has_died"] = 1 if record["has_died"] else 0
        employee["company_id"] = record["company_id"]
        employees.append(employee)
        favourite_food = favourite_food + [
            {"employee_id": x, "food_name": y}
            for x, y in zip(itertools.cycle([record["index"]]), record["favouriteFood"])
        ]
        friends = friends + [
            {"employee_id": x, "friend_id": y}
            for x, y in zip(
                itertools.cycle([record["index"]]), [d["index"] for d in record["friends"]]
            )
        ]

with open(os.path.join("initdb", "json", "companies.json")) as f:
    records = json.load(f)
    companies = []
    for record in records:
        company = OrderedDict()
        company["index"] = record["index"]
        company["company"] = record["company"]
        companies.append(company)


def write_csv(records, path):
    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=",")
        for r in records:
            writer.writerow(r.values())


write_csv(companies, os.path.join("initdb", "csv", "companies.csv"))
write_csv(employees, os.path.join("initdb", "csv", "employees.csv"))
write_csv(favourite_food, os.path.join("initdb", "csv", "favourite_food.csv"))
write_csv(friends, os.path.join("initdb", "csv", "friends.csv"))
