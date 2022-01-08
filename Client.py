import requests
import json

#Define URL to send data and door
URL = "http://127.0.0.1:5000/predict"

if __name__ == "__main__":
    #Test data
    data=json.dumps({"data" : "0@1@2@3@4@5@6/0@1@2@3@4@5@6/0@1@2@3@4@5@6/0@1@2@3@4@5@6"})
    #Send request
    response = requests.post(URL, json=data )

    #Print response
    print(str(response))