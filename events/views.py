from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/accounts/login/")
def event_list(request):
    events = Event.objects.all()
    #order by performance date not datestamp date!
    return render(request, 'events/event_list.html', {'events':events})
