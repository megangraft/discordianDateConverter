from django.shortcuts import render
from django.http import JsonResponse
import datetime
from GregToDiscApp import discordianDate

# Create your views here.
def index(request):
    t = datetime.datetime.now()
    today_disc = discordianDate.discordianDate(datetime.date(t.year,t.month,t.day))
    return render(request, "home.html", {"today": "Today is " + str(today_disc)})

def result(request):
    month = request.GET.get('month', False)
    day = request.GET.get('day', False)
    year = request.GET.get('year', False)

    try:
        res = discordianDate.discordianDate(datetime.date(int(year),int(month),int(day)))
    except ValueError:
        res = "You must provide a valid date!"

    return JsonResponse({"result": res})
