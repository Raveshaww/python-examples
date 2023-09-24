import requests

url = "https://icanhazdadjoke.com/search"

response = requests.get(
        url, 
        params={
            "term": "cat",
            "limit": 1
        },
        headers={"Accept":"application/json"}
    )

print(response.json()["results"])

