from  util import extract_data
from pprint import pprint
import httplib2

app_id  = extract_data("facebook", "app_id")
app_sec = extract_data("facebook", "app_secret")


def searchplace(search):
    http = httplib2.Http()
    token_url = "https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials" %(app_id,app_sec) 
    url = "https://graph.facebook.com/"
    search_term = "search?q=%s&type=place&" % (search)
    response, access_token = http.request(token_url)
    response, search_results = http.request(url + search_term + access_token)
    return search_results
