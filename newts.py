import requests
import pprint


response  = requests.get('https://contesttrackerapi.herokuapp.com/android/')
data = response.json()
print("####### List of upcoming contests ######")

pprint.pprint(data['result']['upcoming'])


print("####### List of ongoing contests ######")

pprint.pprint(data['result']['ongoing'])
