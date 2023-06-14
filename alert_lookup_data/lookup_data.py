import csv
import random
import string

fieldnames = ['ip_address', 'field1', 'field2']
lookup_entries = 100

with open('lookup_table.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(lookup_entries):
        ip_address = '.'.join(str(random.randint(1, 255)) for _ in range(4))
        field1 = ''.join(random.choice(string.ascii_letters)
                         for _ in range(random.randint(5, 15)))
        field2 = ''.join(random.choice(string.ascii_letters)
                         for _ in range(random.randint(5, 15)))

        writer.writerow({'ip_address': ip_address,
                        'field1': field1, 'field2': field2})

print(f'{lookup_entries} lookup table entries generated and saved to lookup_table.csv.')
