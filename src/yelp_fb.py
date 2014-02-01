from yelp_util import *
import fb
import sys
import json

def preprocess(search_term):
    search_parts = search_term.split()
    search_plussed = ''
    for s in search_parts[:-1]:
        search_plussed += s + "+"
    search_plussed += search_parts[-1] 
    return search_plussed


# Notes: There are several duplicate names
# TODO: based on "full_address" in the businees file, plausible fb pages can 
#        be detected, however, the problem remains for chain brands.

# TODO: some businesses have "&" in their names it affects the REST query,
#       the corresponding codes should be replaced with such codes.



def main():
    business_json_file = sys.argv[1]
    business = extract_business_names(business_json_file)
    fb_pages = {}
    json_data = []
    for b in business:
        print business[b], preprocess(business[b])
        possible_results = fb.searchplace(preprocess(business[b]))
#        print possible_results
        fb_pages[b] = possible_results
        json_rec = json.dumps({"business_id": b, "business_name":business[b], "fb_pages": json.loads(possible_results)})
        json_data.append(json.loads(json_rec))
        print possible_results
        
    open("fb.json", 'w').write(json.dumps(json_data, indent = 2))
    


main()
    
    
