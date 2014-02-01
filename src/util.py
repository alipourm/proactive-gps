import json

CONFIG = "app.conf"
def read_data():
    conf_file = open(CONFIG)
    data = json.load(conf_file)
    conf_file.close()
    return data

def extract_data(site, item):
    data = read_data()
    return data[site][item]

