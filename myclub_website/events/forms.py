from django import forms  
from django.forms import ModelForm
from .models import Venue, Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Admin SuperUser Event Form
# class EventFormAdmin(ModelForm):
# 	class Meta:
# 		model = Event
# 		fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
# 		labels = {
# 			'name': '',
# 			'event_date': 'YYYY-MM-DD HH:MM:SS',
# 			'venue': 'Venue',
# 			'manager': 'Manager',
# 			'attendees': 'Attendees',
# 			'description': '',			
# 		}
# 		widgets = {
# 			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
# 			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
# 			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
# 			'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
# 			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
# 			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
# 		}

# # User Event Form
# class EventForm(ModelForm):
# 	class Meta:
# 		model = Event
# 		fields = ('name', 'event_date', 'venue', 'attendees', 'description')
# 		labels = {
# 			'name': '',
# 			'event_date': 'YYYY-MM-DD HH:MM:SS',
# 			'venue': 'Venue',
# 			'attendees': 'Attendees',
# 			'description': '',			
# 		}
# 		widgets = {
# 			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
# 			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
# 			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
# 			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
# 			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
# 		}



# forms.py



class EventFormAdmin(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'manager': 'Manager',
			'attendees': 'Attendees',
			'description': '',			
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
			'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# Create a venue form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'description', 'attendees')
		labels = {
			'name': '',
			'event_date': '',
			'venue': 'Venue',
			'description': '',
			'attendees': '',		
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'venue': forms.Select(attrs={'class':'form-control', 'placeholder':'Venue'}),
			'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
		}


class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields = ('name', 'address', 'zip_code', 'phone','owner', 'web', 'email_address', 'venue_image')
		labels = {
			'name': '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'owner' : 'Owner',
			'web': '',
			'email_address': '',
			'venue_image': '',			
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
			'owner': forms.Select(attrs={'class':'form-control', 'placeholder':'owner'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
			'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
		}
