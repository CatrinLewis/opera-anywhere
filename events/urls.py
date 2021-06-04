from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name="list"),
    path('<id>/', views.event_detail, name="detail"),
]
