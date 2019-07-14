from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
  
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^calendar/event/list/$', views.event_list, name='event_list'),
    url(r'', views.index, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
	
]

