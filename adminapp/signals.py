from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings


@receiver(post_save, sender=User)
def mod_user(sender, instance, created, **kwargs):
    if created and settings.MOD_ADMIN:
        print('signal triggered.')
        instance.is_staff = True
        instance.is_superuser = True
        instance.save()
        settings.MOD_ADMIN = False
