import csv
import requests
import json

api_key = "AIzaSyAQjMjG2j1-TgDvJzuPvp827LGjXn_BvG8"

def bruh():
    with open('input.csv','r') as file:
        csv_reader = csv.reader(file)
        base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        detail_url = "https://maps.googleapis.com/maps/api/place/details/json"
        for row in csv_reader:
            business_name = row[0]
            address = row[2]+row[1]
            city = row[3]
            code = row[5]
            query = f"{business_name}"
            if query != "Name":
                print("Sending for",query)
                #place_details = find_place_from_text(query,code)
                parameters = {
                    "input": f"{business_name}, {address}",
                    "inputtype": "textquery",
                    "key": api_key
                }
                print("sending..")
                response = requests.get(base_url, params=parameters)
                print("received, now parsing")
                results = json.loads(response.text)["candidates"]
                print("okay yayy pop off sis")
                if results:
                    place_id = results[0]["place_id"]
                    print("id ye hai",place_id)
                    parameters = {
                        "key": api_key,
                        "place_id": place_id,
                        "fields": "formatted_phone_number,international_phone_number,website,rating"
                    }
                    response = requests.get(detail_url, params=parameters)
                    print(response)
                    print(response.text)
                    place_details = json.loads(response.text)["result"]
                    print(place_details)
                else:
                    print("bhaya nanga punga hai")

def find_place_from_text(query,code):
    print("function called")
    base_url = "https://maps.googleapis.com/maps/api/place/queryautocomplete/json"
    parameters = {
        "input": query,
        "key": api_key,
        "components": "country:us"
    }
    print("requesting")
    response = requests.get(base_url, params=parameters)
    print("request sent")
    results = json.loads(response.text)["predictions"]
    print("request received Allah ka Shukar")
    if results:
        for i in results:
            print(i["description"]) 
            print(i["matched_substrings"])    
    else:
        print("nahi hoya bhaya")

bruh()