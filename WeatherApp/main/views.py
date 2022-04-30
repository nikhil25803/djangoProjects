# from unicodedata import name
from django.shortcuts import render
from .weather_function import weather
import json

# Create your views here.
def index(request):

    city_name = request.POST.get('city')

    weather(f"{city_name}")
    
    with open("json_file.json", "r") as f:

        data = json.load(f)

    # print(data["name"])
    context = {
        "name":data["name"],
        "temp":data["main"]["temp"]-273,
        "humidity":data["main"]["humidity"],
        "speed":data["wind"]["speed"],
    }

    return render(request, 'index.html', context)