import csv
import random
from datetime import datetime, timedelta

# List of 10 different SQL commands
sql_commands = [
    "SELECT * FROM users",
    "UPDATE products SET price = price * 1.1",
    "INSERT INTO orders (customer_id, product_id, quantity) VALUES (1, 2, 5)",
    "DELETE FROM customers WHERE id = 10",
    "CREATE TABLE employees (id INT, name VARCHAR(50))",
    "ALTER TABLE products ADD COLUMN description TEXT",
    "DROP TABLE orders",
    "SHOW TABLES",
    "SELECT COUNT(*) FROM products",
    "UPDATE users SET password = 'new_password' WHERE id = 5"
]

# Generate the dataset
dataset = []
start_date = datetime.now() - timedelta(days=365)  # Start date is 1 year ago
for _ in range(100):  # Generate 100 records
    command = random.choice(sql_commands)
    # Random duration between 1 and 10 seconds
    duration = random.randint(1, 10)
    command_type = "SELECT" if command.startswith(
        "SELECT") else "UPDATE" if command.startswith("UPDATE") else "OTHER"
    # Random timestamp within the last 1 year
    timestamp = start_date + timedelta(seconds=random.randint(0, 31536000))
    dataset.append([command, duration, command_type, timestamp])

# Write the dataset to a CSV file
with open("db_audit.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Command", "Duration", "Type",
                    "Timestamp"])  # Write the header
    writer.writerows(dataset)  # Write the data
