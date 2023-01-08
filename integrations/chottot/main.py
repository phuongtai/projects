from dataclasses import fields
import csv
from .interface import Property

import os
from .client import Client

from dotenv import load_dotenv
load_dotenv()

script_dir = os.path.dirname(__file__)
# print(script_dir)
def main():
    client = Client(base_url=os.getenv('base_url'))
    # https://gateway.chotot.com/v1/public/ad-listing?limit=10&protection_entitlement=true&cg=1040&region_v2=13000&st=s,k&key_param_included=true
    data_list = client.realEstate.list(params={'limit': 20, 'page': 1, 'cg': 1020, 'o': 20, 'st':'s,k'})
    list_fields = [field.name for field in fields(Property)]
    file_path = 'data/{}/property.csv'.format(1020)
    with open(os.path.join(script_dir, file_path), '+w', encoding='UTF8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list_fields)
        writer.writeheader()
        writer.writerows(data_list)
