
import csv
import json
import os
import requests

from pathlib import Path
from dotenv import load_dotenv


# 1. Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

CSV_FILE = DATA_DIR / "employees.csv"
JSON_FILE = DATA_DIR / "employees.json"
HIGH_EARNERS_FILE = DATA_DIR / "high_earners.csv"
USERS_FILE = DATA_DIR / "users.json"


# 2. Load environment variables
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("API_KEY")

print("API Key loaded:", API_KEY is not None)


# 3. Read employees.csv
employees = []

with open(CSV_FILE, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["id"] = int(row["id"])
        row["salary"] = int(row["salary"])
        employees.append(row)


# 4. Filter employees earning above 50000
high_earners = [
    emp for emp in employees
    if emp["salary"] > 50000
]

print(
    f"Rows read: {len(employees)} | "
    f"High earners: {len(high_earners)}"
)


# 5. Save employees.json
with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)


# 6. Save high_earners.csv
with open(HIGH_EARNERS_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=employees[0].keys()
    )

    writer.writeheader()
    writer.writerows(high_earners)


# 7. Fetch users from API
API_URL = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()

    users = response.json()

    # Print first three users
    for user in users[:3]:
        print(
            user.get("id"),
            "-",
            user.get("name"),
            "-",
            user.get("email")
        )

    # Extract nested JSON data
    user_details = []

    for user in users:
        address = user.get("address", {})
        geo = address.get("geo", {})
        company = user.get("company", {})

        user_details.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "latitude": geo.get("lat"),
            "longitude": geo.get("lng"),
            "company": company.get("name")
        })

    # Save users.json
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(user_details, file, indent=4)

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)


# 8. Test 404 error handling
try:
    response = requests.get(
        f"{API_URL}/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()

except requests.exceptions.Timeout:
    print("404 test timed out")

except requests.exceptions.ConnectionError:
    print("404 test connection failed")

except requests.exceptions.HTTPError as error:
    print("404 test HTTP Error:", error)
