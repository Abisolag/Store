from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#        profile= Profile.objects.create(user=instance)
#        profile.save()
def create_profile(sender, **kwargs):
     if kwargs['created']:
         user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()