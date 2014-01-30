import json
import sys
from pprint import pprint




rev_data_file = open(sys.argv[1])
bus_data_file = open(sys.argv[2])

business = {}
reviews  = {}
def extract_business_names():
    for line in bus_data_file.readlines():
        json_dec = json.loads(line)
        business_id   =  json_dec["business_id"]
        business_name = json_dec["name"]
        business[business_id] = business_name

def extract_reviews():
    for line in rev_data_file.readlines():
        json_dec = json.loads(line)
        business_id = json_dec["business_id"]
        text = json_dec["text"]
        if business_id not in reviews:
            reviews[business_id] = [text]
        else:
            reviews[business_id].append(text)


extract_reviews()
extract_business_names()
