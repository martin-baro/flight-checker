import requests
import json

def flight_search(dest, f_date, t_date):
    base_url = "https://api.skypicker.com/flights?"
    url = "".join([base_url, "fly_from=BUD", "&fly_to=", dest, "&date_from=", f_date, "&date_to=", t_date])
    print(url)
    response = requests.get(url)
    jData = json.loads(response.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print(key + " : " + jData[key])