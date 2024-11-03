import requests

def get(paikkakunta, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        kuvaus = data["weather"][0]["description"]
        kelvin = data["main"]["temp"]

        celsius = kelvin - 273.15

        print(f"sää {paikkakunta}ssa:")
        print(f"kuvaus: {kuvaus.capitalize()}")
        print(f"lämpötila: {celsius:.2f} °C")

    except requests.exceptions.RequestException as e:
        print("fail:", e)

paikkakunta = input("anna paikkakunnan nimi: ")

api_key = "669a2c88d7f66c4435a6e6045c1f7876"

get(paikkakunta, api_key)
