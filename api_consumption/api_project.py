import requests 
from random import choice

url = "https://icanhazdadjoke.com/search"
user_choice = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
        url, 
        params={
            "term": user_choice,
        },
        headers={"Accept":"application/json"}
    )

results = response.json()['results']
amount_of_results = len(results)

if amount_of_results == 0:
    print(f"Sorry, I don't know anything about {user_choice}")
else:  
    print(f"I found {amount_of_results} jokes. Here's one:")
    print(choice(results)['joke'])