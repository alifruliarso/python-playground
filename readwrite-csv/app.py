import csv
from urllib.request import urlopen
import json
from tempfile import NamedTemporaryFile
import shutil


def get_status(id: str):
    url = f'https://jsonplaceholder.typicode.com/todos/{id}'
    with urlopen(url) as response:
        body = response.read()
        item = json.loads(body)
        print(item)
        return item['completed']

tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

with open('a.csv', mode='r') as csv_file, tempfile:
    csv_reader = csv.DictReader(csv_file)
    fieldnames = ['name', 'dept', 'birth_month', 'id', 'completed']
    writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            writer.writeheader()
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
        completed_status = get_status(row["id"])
        writer.writerow({
            'name':row['name'],
            'dept':row['department'],
            'birth_month':row['birthday month'],
            'id':row['id'],
            'completed':completed_status
        })

    print(f'Processed {line_count} lines.')

shutil.move(tempfile.name, "new_a.csv")
