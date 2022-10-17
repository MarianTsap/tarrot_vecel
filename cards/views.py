from django.views import generic
from .models import Cards
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Q

def index(request):
    cards_list = Cards.objects.order_by('id')
    context = {
        'cards_list': cards_list,
        'moon_cycle_name': moon_cycle_name(),
        }
    return render(request, 'cards/index.html', context)

class NoteList(generic.ListView):
    queryset = Cards.objects.order_by('id')
    #paginate_by = 9  # if pagination is desired
    context_object_name = 'cards_list'
    template_name = 'cards/index.html'
    

def meaning(request):
    cards_array = request.POST['cards_array']
    cards_array = json.loads(cards_array)
    all_entries={}

    for item in cards_array:
       queryset = Cards.objects.filter(card=item).values()
       print((item))
       all_entries[queryset[0]['card']]=[queryset[0]['card_meaning'] , queryset[0]['card_meaning_ukr']]
    return JsonResponse(all_entries)

# calculate moon day
# https://www.subsystems.us/uploads/9/8/9/4/98948044/moonphase.pdf
#https://minkukel.com/en/various/calculating-moon-phase/
def moon_cycle_name():
    import datetime
    import math
    meaning_moon_cycle = {'New':(0,1),'Waxing Crescent':(1,6.38264692644001),'First Quarter':(6.38264692644001,8.38264692644),'Waxing Gibbous':(8.38264692644,13.76529385288),'Full':(13.76529385288,15.76529385288),'Waning Gibbous':(15.76529385288,21.14794077932),'Last Quarter':(21.14794077932,23.14794077932),'Waning Crescent':(23.14794077932,28.53058770576)}
    x = datetime.datetime.utcnow()
    New_moon = datetime.datetime(2000, 1, 6, 18,14)
    const = 29.53058770576
    moon_cicles = (x-New_moon)
    moon_cicles = float((moon_cicles.days+moon_cicles.seconds/3600/24))/const
    #moon_day = ((int(moon_days.days)+float(x.hour/24))%1)*const
    moon_day = round(moon_cicles%1*const,2) 
    
    #x = datetime.datetime(2017, 3, 1)
    Y = x.year
    M = x.month
    D = x.day
    if M == 1 or M == 2:
        Y = Y - 1
        M = M + 12
    A = math.floor(Y/100)
    B = math.floor(A/4)
    C = 2 - A + B
    E = math.floor(365.25 * (Y+4716))
    F = math.floor(30.6001 * (M+1))
    JD = C + D + E + F - 1524.5 
    Day_since_New = JD - 2451549.5
    New_Moons = Day_since_New / 29.53058770576
    Days_into_cycle = int(round((New_Moons % 1)*29.53058770576,0))
    for item in meaning_moon_cycle:
        if moon_day >= meaning_moon_cycle[item][0] and moon_day <= meaning_moon_cycle[item][1]:
            moon_cycle_name = item
    return (f"The Moon Phase - {moon_cycle_name}, {Days_into_cycle} - moon day into cycle ({moon_day})")



    
    