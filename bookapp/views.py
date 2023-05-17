from django.shortcuts import render
from django.http import HttpResponse
from .models import Month
import requests, aladhan, json

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

def hijri_today(request):
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
def hijri_month(request):
    """The goal of this function is to create a view of the whole month requested
    
    Process:
        1. Create forms for user to specify Gregorian month number and year
        2. Use this month and year to make a api call and pull data
            * Append the month and date to the necessary parts of the api call
        3. Display the month name at the top of the page
        4. Call the hijri_day function to give us the days of that month
        5. Fill in the days of the month to the created Month table.
    """
    
    #TODO Start from step 4 and start by answering the following question: 
    #   * How do we add numbers to the end of a url in Django?
    #   * How do we use this number as input for the month_num variable?

    # we'll start with default values then add a feature to allow user to change these:
    # USer can supply month number in url or in a form on the page
    year_num = 2023
    url = f'http://api.aladhan.com/v1/gToHCalendar/{1}/{year_num}'

    # pull the data
    month = requests.get(url)

    # convert the month to JSON
    month_data = month.json()

    '''
    count = 1
    months = []
    while count <= 12:
        url = f'http://api.aladhan.com/v1/gToHCalendar/{count}/{year_num}'

        # pull the data
        month = requests.get(url)

        # convert the month to JSON
        month_data = month.json()
        months.append(month_data)

        count += 1

    # making a JSON with info for all the 12 gregorian months of 2023
    # alongside their Hijri counterparts
    month_json = {}
    for i in range(1, 12):
        month_json = {f'{i}': month for month in months}

    month_fin = json.dumps(month_json)
    '''

    return render(request, "month.html", {'month': month_data})

def prayer_times(request):

    """We'll use the aladhan API to get Prayer Times for this View"""

    country = aladhan.City("Nairobi", "KE")
