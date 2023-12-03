from django.db import models
from django.contrib.auth.models import User



# class Like(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	Event = models.ForeignKey('Event', on_delete=models.CASCADE)
# 	created_at = models.DateTimeField(auto_now_add=True)


class UserVisit(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	last_visit = models.DateTimeField(auto_now=True)


class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=120)
	address = models.CharField(max_length=300)
	zip_code = models.CharField('Zip Code', max_length=15)
	phone = models.CharField('Contact Phone', max_length=25, blank=True)
	web = models.URLField('Website Address', blank=True)
	email_address = models.EmailField('Email Address', blank=True)
	owner = models.ForeignKey(User, verbose_name=("Venue Owner"), on_delete=models.CASCADE)
	venue_image = models.ImageField(null=True, blank=True, upload_to="images/")

	def __str__(self):
		return self.name
	
class MyClubUser(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField('User Email')

  def __str__(self):
    return self.first_name + ' ' + self.last_name


class Event(models.Model):
	name  = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	#venue = models.CharField(max_length=150)
	#manager = models.CharField(max_length=60)
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(MyClubUser, blank=True)
	likes = models.IntegerField(default=0)

	def increment_likes(self):
		self.likes += 1
		self.save()

	def __str__(self):
		return self.name
    
    
# class Like(models.Model):
# 	event = models.ForeignKey(Event, on_delete=models.CASCADE)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	created_at = models.DateTimeField(auto_now_add=True)

