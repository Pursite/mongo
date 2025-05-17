
from pymongo import MongoClient

# اتصال به MongoDB (در اینجا به سرور محلی)
client = MongoClient("mongodb://localhost:27017/")

# ساخت/اتصال به دیتابیس و کالکشن
db = client["mydatabase"]
collection = db["users"]

# ---------- CREATE ----------
new_user = {"name": "Ali", "age": 25, "email": "ali@example.com"}
insert_result = collection.insert_one(new_user)
print("Inserted ID:", insert_result.inserted_id)

# ---------- READ ----------
print("\nAll users:")
for user in collection.find():
    print(user)

# ---------- UPDATE ----------
collection.update_one(
    {"name": "Ali"},
    {"$set": {"age": 26}}
)

# ---------- DELETE ----------
collection.delete_one({"name": "Ali"})
