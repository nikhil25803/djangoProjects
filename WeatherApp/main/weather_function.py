import requests
import json

def weather(name):

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid=01019b2042882a4a2cb94669f5e36552"

    r = requests.get(url=api_url)
    data = r.json()
    json_write = json.dumps(data, indent=4)

    with open("json_file.json", "w") as f:
        # data = json.loads(f)
        f.write(json_write)

# weather("Patna")