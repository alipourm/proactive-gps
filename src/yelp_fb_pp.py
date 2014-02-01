from yelp_util import *
import fb
import sys
from json import loads, dumps
import pp

max_bucket_size = 10
n_cpus = 8


def split(dictionary, bucket_size):
    list_view = dictionary.items()
    dict_list = []
    cur_bucket = []
    for l in list_view:
        if len(cur_bucket) < bucket_size:
            cur_bucket.append(l)
        else:
            dict_list.append(dict(cur_bucket))
            cur_bucket = []
    return dict_list
        

        



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
    dict_list = split(business, max_bucket_size)
    ppservers = ()
    job_server = pp.Server(n_cpus, ppservers=ppservers)
    i = 0
    print "Party is starting"
    
    jobs = []
    for d in dict_list: 
        
        j = job_server.submit(job, (d, i,), (preprocess,fb.searchplace,loads,dumps,), ("fb", "json",))
        i += 1
        jobs.append(j)

    for j in jobs:
        j()
    job_server.print_stats()



def job(business, i):
    json_data = []
    fb_pages = {}
    for b in business:
        print business[b], preprocess(business[b])
        possible_results = fb.searchplace(preprocess(business[b]))
#        print possible_results
        fb_pages[b] = possible_results
        json_rec = json.dumps({"business_id": b, "business_name":business[b], "fb_pages": json.loads(possible_results)})
        json_data.append(json.loads(json_rec))

        
    open("fb%s.json"%(i), 'w').write(json.dumps(json_data, indent = 2))
    print "%d done\n" % (i)
main()
