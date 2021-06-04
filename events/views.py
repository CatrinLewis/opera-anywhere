from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url="/accounts/login/")
def event_list(request):
    events = Event.objects.all()
    #order by performance date not datestamp date!
    return render(request, 'events/event_list.html', {'events':events})

@login_required(login_url="/accounts/login/")
def event_detail(request, id):
    # return HttpResponse(id)
    event = Event.objects.get(id=id)
    return render(request, 'events/event_detail.html', {'event':event})
