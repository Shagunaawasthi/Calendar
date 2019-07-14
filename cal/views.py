from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.dateparse import parse_datetime
import calendar
from datetime import timezone
from pandas.tseries import offsets


import pytz


from .models import *
from .utils import Calendar
from .forms import EventForm

def index(request):
    context = { }
    page= render(request, 'cal/index.html',context)
    return page
   
    


    
        
        


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        d = get_date(self.request.GET.get('month',None))
        
        
        
        #datetime.fromtimestamp(timestamp)
        cal = Calendar(self.request,d.year, d.month)
        cal.setfirstweekday(calendar.SUNDAY)
        
        html_cal = cal.formatyear(d.year)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_year(d)
        context['next_month'] = next_year(d)
        context['current_year'] = datetime.today().year
        context['calendar_year'] = d.year
    
        return context



#def prev_month(d):
 #   first = d.replace(day=1)
  #  prev_month = first - timedelta(days=1)
   # month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    #return month
def get_date(req_year):

    if req_year:
        year = int(req_year)  #(int(x) for x in req_year)
        return date(year, month=1, day=1)
    return datetime.today()

   

def prev_year(d):
    first = d.replace(month=1)
    
    prev_year = first.year-1
    prev_month=first.month
    month =  str(prev_year) # + '-' + str(prev_month)
    return month


def next_year(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_year = last.year + 1
    next_month=last.month
    month =  str(next_year)  #+ '-' + str(next_month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = {
        "title" : "not found",
        "description": "not found"
        }
    return render(request, 'cal/event.html', {'context' : instance})

def event_list(request):
    output=""
    day = request.GET.get('day')
   
    month = request.GET.get('month')
 
    year =request.GET.get('year')
    
    if len(day) < 2:
        day = '0'+day
    if len(month) < 2:
        month = '0'+ month
    
    s = year+'-'+ month+'-'+day
    
    events_per_day =  Event.objects.filter(start_time__date=datetime.strptime(s, "%Y-%m-%d").date())
    if events_per_day:
        
        context = {'events_per_day' : events_per_day  }
        output= render(request, 'cal/event_list.html',context)
    else:
        
        context={}
        output= render(request, 'cal/event.html',context)

    return output  