import requests

uri = "https://api.coindesk.com/v1/bpi/currentprice.json"

resp = requests.get(uri,verify=True)

print(resp.json())