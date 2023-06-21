import csv
import random
from datetime import datetime, timedelta

# List of possible failure scenarios
failure_scenarios = [
    {
        "event": "Failed password for root",
        "user": "root",
        "source_ip": "223.205.219.67",
        "port": str(random.randint(1024, 65535))
    },
    {
        "event": "Failed password for invalid user",
        "user": random.choice(["perl", "test", "webuser"]),
        "source_ip": random.choice(["202.179.8.245", "10.20.30.40", "192.168.1.100"]),
        "port": str(random.randint(1024, 65535))
    },
    {
        "event": "Failed login from unknown user",
        "user": random.choice(["unknown", "guest", "nouser"]),
        "source_ip": random.choice(["172.16.0.10", "10.0.0.5", "192.168.0.20"]),
        "port": str(random.randint(1024, 65535))
    },
    {
        "event": "Failed SSH authentication",
        "user": random.choice(["user1", "user2", "user3"]),
        "source_ip": random.choice(["10.0.0.2", "192.168.1.20", "172.16.0.50"]),
        "port": str(random.randint(1024, 65535))
    }
]

# Generate the dataset
dataset = []
start_date = datetime(2018, 1, 1)  # Start date
end_date = datetime(2018, 12, 31)  # End date
date_range = (end_date - start_date).days + 1  # Total days in the date range
for _ in range(1000):  # Generate 1000 records
    # Random date within the range
    random_date = start_date + \
        timedelta(days=random.randint(0, date_range - 1))
    # Random timestamp within the selected date
    timestamp = random_date + timedelta(seconds=random.randint(0, 86400))
    failure = random.choice(failure_scenarios)
    event = f"{failure['event']} {failure['user']} from {failure['source_ip']} port {failure['port']} ssh2"
    source = f"/opt/log/{random.choice(['web', 'app', 'db'])}/secure.log"
    host = random.choice(['web01', 'app01', 'db01'])
    dataset.append([timestamp.strftime(
        '%m/%d/%y'), timestamp.strftime('%I:%M:%S.%f %p'), event, host, source, "linux_secure"])

# Write the dataset to a CSV file
with open("linux_secure.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["_time", "Event", "host", "source",
                    "sourcetype"])  # Write the header
    writer.writerows(dataset)  # Write the data
