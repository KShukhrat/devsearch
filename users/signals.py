from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import User

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.name,
            email=user.email,
            name=user.first_name,
        )
def deleteuser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteuser, sender=Profile)