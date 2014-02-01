import json

business = {}
reviews  = {}
def extract_business_names(file_name):
    #TODO error handling
    bus_data_file = open(file_name) 
    for line in bus_data_file.readlines():
        json_dec = json.loads(line)
        business_id   =  json_dec["business_id"]
        business_name = json_dec["name"]
        business[business_id] = business_name
    return business

def extract_reviews(file_name):
    #TODO error handling
    rev_data_file = open(file_name) 
    for line in rev_data_file.readlines():
        json_dec = json.loads(line)
        business_id = json_dec["business_id"]
        text = json_dec["text"]
        if business_id not in reviews:
            reviews[business_id] = [text]
        else:
            reviews[business_id].append(text)
    return reviews


