from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

# Create your models here.
class Profile(models.Model):
	user          = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
	phone_number  = models.CharField(max_length = 225)
	home_address  = models.CharField(max_length = 225)
	latitude      = models.FloatField(default=0.00)
	longitude     = models.FloatField(default=0.00)
	updated       = models.DateTimeField(auto_now = True)
	created       = models.DateTimeField(auto_now_add = True)


	def user_profile(phone_number, home_address, location, instance, *args, **kwargs):
		profile = instance
		phone_number = phone_number
		home_address = home_address
		# action = Feed(user=user, post=post, notification_type=1)
		# action.save()