from django.shortcuts import render
from django.http import HttpResponse
import requests, aladhan

def users(request):
    """We'll use this to pull data from the rest API"""

    # pulling the data
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users'
    )

    # let's convert the response into json
    users = response.json()
    # print(users)

    return render(request, "users.html", {'users': users})

def hijriCal(request):
    """We'll use this to consume the Hijri calendar api
    
    Find more info: 
        * https://aladhan.com/islamic-calendar-api
    """

    parsed_date = []
    # pulling data for the current date
    # to convert today's date to HijriCalendar Date
    today_response = requests.get(
        'http://api.aladhan.com/v1/gToH/16-05-2023'
    )

    # let's convert this to JSON
    today = today_response.json()

    return render(request, "today.html", {'today': today})

def prayer_times(request):
    """We'll use the aladhan API to get Prayer Times for this View"""

    country = aladhan.City("Nairobi", "KE")