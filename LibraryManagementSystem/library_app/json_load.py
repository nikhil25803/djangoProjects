import json

json_data = open('C:/Users/welcome/Desktop/Nikhil Raj/venv/static/books.json')
data1 = json.load(json_data)
data2 = json.dumps(data1)

print(data2['author'])