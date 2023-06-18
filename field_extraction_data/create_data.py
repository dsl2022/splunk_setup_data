import csv
import random
from datetime import datetime, timedelta

# Generate synthetic dataset


def generate_dataset(num_entries):
    dataset = []
    start_date = datetime(2023, 1, 1)  # Modify the start date as needed
    usage_options = ["Borderline Business", "Personal", "Unknown", "Violation"]
    for i in range(num_entries):
        timestamp = start_date + timedelta(minutes=i)
        source_ip = f"192.168.0.{random.randint(1, 254)}"
        destination_ip = f"10.0.0.{random.randint(1, 254)}"
        url = f"http://www.example.com/page{i}.html"
        response_code = random.choice([200, 404, 500])
        usage = random.choice(usage_options)
        # Modify the range of byte numbers as needed
        sc_bytes = random.randint(100, 10000)
        dataset.append([timestamp, source_ip, destination_ip,
                       url, response_code, usage, sc_bytes])
    return dataset

# Save dataset to CSV file


def save_dataset_to_csv(dataset, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['timestamp', 'source_ip', 'destination_ip',
                        'url', 'response_code', 'usage', 'sc_bytes'])
        writer.writerows(dataset)


# Example usage
num_entries = 1000  # Modify the number of entries as desired
dataset = generate_dataset(num_entries)
save_dataset_to_csv(dataset, 'cisco_was_squid_dataset.csv')
