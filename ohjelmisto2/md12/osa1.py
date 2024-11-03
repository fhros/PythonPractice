import requests

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        joke = data["value"]
        print(joke)
    except requests.exceptions.RequestException as e:
        print("fail:", e)

get_joke()
