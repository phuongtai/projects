import os
import csv
from db import get_database
script_dir = os.path.dirname(__file__)


def get_csv_data():
    file_path = 'data/{}/property.csv'.format(1040)
    with open(os.path.join(script_dir, file_path), 'r', encoding='UTF8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            yield row

def main():
    try:
        db = get_database()
        collection = db['property']
        rows = [row for row in get_csv_data()]
        collection.insert_many(rows)
    except Exception as e:
        raise e

if __name__ == '__main__':
    main()
