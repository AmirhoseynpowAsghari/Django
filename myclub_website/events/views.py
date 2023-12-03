from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
import calendar
from .models import Event
from .models import Venue
from .forms import VenueForm, EventForm, SignUpForm, EventFormAdmin
from calendar import HTMLCalendar
from datetime import datetime
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


from django.http import HttpResponse
from django.shortcuts import render
from .models import Venue

from django.core.paginator import Paginator

from django.http import JsonResponse
from django.urls import reverse

from django.contrib.auth.decorators import login_required

#I added datetime library to check the time of every events in my code
from datetime import date

# 
from django.http import QueryDict
# def like_event(request, event_id):
#     #event_id = request.POST['event_id'] # Get the event ID from the AJAX request
#     event = get_object_or_404(Event, id=event_id)
#     event.like += 1
#     event.save()
#     return JsonResponse({'like': event.like})

# @login_required
# def like_event(request, event_id):
# 	event = get_object_or_404(Event, id=event_id)
# 	if Like.objects.filter(event=event, user=request.user).exists():
# 		return JsonResponse({'message': 'You have already liked this event.'})
# 	like = Like(event=event, user=request.user)
# 	like.save()
# 	return JsonResponse({'message': 'Event liked successfully.'})


def like_event(request, event_id):
	event = Event.objects.get(id=event_id)
	event.increment_likes()
	return redirect('list-events')

def My_venue(request):
	user = request.user
	if user.is_authenticated:
		My_venue = Venue.objects.filter(owner=user)
		return render(request, 'events/My_venue.html', {'My_venue' : My_venue})
	else:
		messages.success(request, "You must logged in first")
		return redirect('home')


def My_event(request):
	user = request.user
	if user.is_authenticated:
		My_event = Event.objects.filter(manager=user)
		return render(request, 'events/My_events.html', {'My_event' : My_event})
	else:
		messages.success(request, "You must logged in first")
		return redirect('home')

def sign_up(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'events/sign_up.html', {'form': form})


def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=Venues.txt'
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'{venue.name}\n {venue.address}\n {venue.zip_code}\n {venue.phone}\n {venue.web} \n {venue.email_address}')

    response.writelines(lines)
    return response



def delete_event(request, event_id):
	event = get_object_or_404(Event, pk=event_id)

	if request.user == event.manager:
		event.delete()
		messages.success(request, ("Your post was deleted"))
		return redirect('list-events')
		
	else:
		messages.success(request, ("Your are not authorized to delete this event"))
		return redirect('list-events')
	

def Edit_Event(request, Event_id):
	event = Event.objects.get(pk=Event_id)
	if request.user.is_superuser:
		form = EventFormAdmin(request.POST or None, instance=event)
	else:
		form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('list-events')

	return render(request, 'events/event_edit.html', {'event': event, 'form': form})
	


def Edit_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('venue-list')
	return render(request, 'events/venue_edit.html', {"venue" : venue, "form" : form})
      
      
                 
            
      
      

# def venue_search(request):
	
# 	if request.method == "POST":
# 		searched = request.POST['searched']
# 		venues = Venue.objects.filter(name__contains=searched)
# 		return render(request, 'events/search_venue.html', {"searched" : searched, "venues" : venues})
# 	else:
# 		return render(request, 'events/search_venue.html')



def venue_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()
        if searched:
            query = Q(name__icontains=searched)
            words = searched.split()
            for word in words:
                query |= Q(name__icontains=word)
            
            venues = Venue.objects.filter(query)
        else:
            venues = Venue.objects.none()
            
        return render(request, 'events/search_venue.html', {"searched": searched, "venues": venues})
    else:
        return render(request, 'events/search_venue.html')

def event_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()
        if searched:
            query = Q(name__icontains=searched)
            words = searched.split()
            for word in words:
                query |= Q(name__icontains=word)
            
            events = Event.objects.filter(query)
        else:
            events = Event.objects.none()
            
        return render(request, 'events/search_events.html', {"searched": searched, "events": events})
    else:
        return render(request, 'events/search_events.html')
	
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()
        if searched:
            query = Q(name__icontains=searched)
            words = searched.split()
            for word in words:
                query |= Q(name__icontains=word)
            
            venues = Venue.objects.filter(query)
            events = Event.objects.filter(query)
        else:
            venues = Venue.objects.none()
            events = Event.objects.none()
            
        return render(request, 'events/search.html', {"searched": searched, "venues": venues, "events": events})
    else:
        return render(request, 'events/search.html')

def show_venues(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    user = request.user  # Assuming you have user authentication implemented
    context = {
        'venue': venue,
        'user': user,
    }
    return render(request, 'events/show_venues.html', context)

def show_events(request, event_id):
	show_events = Event.objects.get(pk=event_id)
	context = show_events
	return render(request, 'events/show_events.html', {"context" : context})

def venue_list(request):
	#venue_list = Venue.objects.all().order_by('name')
	#context = venue_list
	items_per_page = 2
	data = Venue.objects.all()
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'events/venue_list.html', {"page_obj" : page_obj})

def add_event(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = EventFormAdmin(request.POST)
			if form.is_valid():
					form.save()
					return 	HttpResponseRedirect('/add_event?submitted=True')	
		else:
			form = EventForm(request.POST)
			if form.is_valid():
				#form.save()
				event = form.save(commit=False)
				event.manager = request.user # logged in user
				event.save()
				return 	HttpResponseRedirect('/add_event?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = EventFormAdmin
		else:
			form = EventForm

		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})


def add_venue(request):
	submitted = False
	if request.method == "POST":
		form = VenueForm(request.POST, request.FILES)
		venue = form
		if form.is_valid():
			form.save()
			#venue.owner = request.user.id # logged in user
			venue.save()
			form.save()
			return 	HttpResponseRedirect('/add_venue?submitted=True')	
	else:
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})

# def add_venue(request):
#     submitted = False
#     if request.method == "POST":
#         form = VenueForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/add_venue?submitted=True")
#     else:
#         form = VenueForm
#         if 'submitted' in request.GET:
#             submitted = True
          
#     return render(request, 'events/form.html', {"form" : form, "submitted" : submitted})
     
    

# def events_order_by_likes(request):
# 	event_list = Event.objects.all().order_by('-like')
# 	context = event_list 
# 	return render(request, 'events/event_list.html', {"context" : context})

def all_events(request):
    event_list = Event.objects.all()
    today = date.today()
    context = {"event_list": event_list, "today": today}
    return render(request, 'events/event_list.html', context)
    

def home(request,  year=datetime.now().year, month=datetime.now().strftime('%B')):
	name = "John"
	month = month.capitalize()
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	now = datetime.now()
	current_year = int(now.year)
	cal = HTMLCalendar().formatmonth(
		year, 
		month_number)
	popular_events = Event.objects.order_by('-likes')[:6] 
		
	return render(request, 
		'events/home.html', {"cal" : cal, "name" : name, "current_year" : current_year, 'popular_events' : popular_events})