#!/usr/bin/python3
import csv
import json
def convert_csv_to_json(filename):
    try:
        with open(filename,'r') as f:
            data=list(csv.DictReader(f))
        with open("data.json",'w') as f:
            new_data=json.dump(data,f)
        return True
    except:
        return False
