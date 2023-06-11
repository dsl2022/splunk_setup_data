import csv
import random
import string

fieldnames = ['Timestamp', 'Event', 'Severity', 'Source', 'Message']
entries = 10000

with open('splunk_logs.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(entries):
        # Replace with your desired timestamp generation logic
        timestamp = "2023-06-10 00:00:00"
        event = ''.join(random.choice(string.ascii_letters)
                        for _ in range(random.randint(5, 15)))
        severity = random.choice(
            [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase)])
        source = ''.join(random.choice(string.ascii_lowercase)
                         for _ in range(random.randint(6, 12)))
        message = ''.join(random.choice(string.ascii_letters + string.digits + ' ')
                          for _ in range(random.randint(20, 50)))

        writer.writerow({'Timestamp': timestamp, 'Event': event,
                        'Severity': severity, 'Source': source, 'Message': message})

print(f'{entries} log entries generated and saved to splunk_logs.csv.')
