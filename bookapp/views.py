from django.shortcuts import render
from django.http import HttpResponse
import requests

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
