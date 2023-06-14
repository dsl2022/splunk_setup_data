import random
import csv
import datetime

# Generate random log entries
log_entries = []
for _ in range(10000):
    event_type = random.choice(["win_event", "access_event"])
    timestamp = datetime.datetime.now(
    ) - datetime.timedelta(minutes=random.randint(1, 10000))
    if event_type == "win_event":
        event_code = random.randint(540, 4624)
        log_entry = {"index": "security", "sourcetype": "win*", "EventCode": event_code,
                     "Event_Description": "", "timestamp": timestamp, "User": ""}
    else:
        log_entry = {"index": "security", "sourcetype": "history_access", "EventCode": "",
                     "Event_Description": "Access", "timestamp": timestamp, "User": ""}
    # Randomly assign 0 or 1 to badge_access field
    log_entry["badge_access"] = random.choice([0, 1])
    log_entries.append(log_entry)

# Write log entries to a CSV file
fieldnames = ["index", "sourcetype", "EventCode",
              "Event_Description", "timestamp", "User", "badge_access"]
with open("splunk_logfile.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(log_entries)

print("Log file generated successfully.")
