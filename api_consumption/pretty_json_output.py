import requests
import json

game_steamid = "892970"
url = f"https://api.steamcmd.net/v1/info/{game_steamid}"

response = requests.get(
    url,
    headers={"Accept":"application/json"}
)

response_dict = response.json() 
print(json.dumps(response_dict, indent=4, sort_keys=True))