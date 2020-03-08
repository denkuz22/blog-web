from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
  if created:
    Profile.objects.create(user=instance)
#  When the user is created, and saved, it sends a signal with User instance in it, which is recieved by create_profile function which creates a profile accordingly.

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()