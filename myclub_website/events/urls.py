from django.urls import path
from . import views

urlpatterns = [
	# Path Converters
	# int: numbers
	# str: strings
	# path: whole urls /
	# slug: hyphen-and_underscores_stuff
	# UUID: universally unique identifier

    path('', views.home, name="home"),
	path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
    path('add_venue', views.add_venue, name='add-venue'),
    path('add_event', views.add_event, name='add-event'),
    path('venue_list', views.venue_list, name='venue-list'),
    # path('venues/page/<int:page>/', views.venue_list, name='venue-list-page'),
    path('venue/<venue_id>', views.show_venues, name='show-venue'),
    path('event/<event_id>', views.show_events, name='show-event'),
    # path('search/', views.venue_search, name='venue-search'),
    # path('search/', views.event_search, name='event-search'),
    path('search/', views.search, name='search'),
    path('Edit_Event/<Event_id>', views.Edit_Event, name='Edit-Event'),
    path('Edit_venue/<venue_id>', views.Edit_venue, name='Edit-venue'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete-event'),
    path('venue_text', views.venue_text, name='venue-text'),
    path('sign_up', views.sign_up, name = "sign-up"),
    path('My_event', views.My_event, name = "My-event"),
    path('My_venue', views.My_venue, name = "My-venue"),
     path('like/<int:event_id>/', views.like_event, name='like'),
    # path('like/<int:event_id>/', views.like_event, name='like_event'),
    # path('events/order_by_date', views.events_order_by_likes, name="order-by-likes"),

]

