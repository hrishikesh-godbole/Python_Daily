import json
import requests as rq
import calendar
def getData(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load url")

def loadJson(data):
    if not data is None:
        j = json.loads(data)

        title = j["results"][0]["name"]["title"]
        fname = j["results"][0]["name"]["first"]
        lname = j["results"][0]["name"]["last"]
        email = j["results"][0]["email"]
        gender = j["results"][0]["gender"]
        
        return title, fname, lname, email, gender

def main():
    url = "https://randomuser.me/api"

    values = loadJson(getData(url))

    if not values is None:
        print("Name: ",values[0] + ". " + values[1] + " " + values[2])
        # print("Title: ",values[0])
        # print("First name: ", values[1])
        # print("Last name: ", values[2])
        print("Email: ", values[3])
        print("Gender: ", values[4])

if __name__ == "__main__":
    main()

