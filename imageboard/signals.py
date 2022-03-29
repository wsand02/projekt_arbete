from django.db.models.signals import post_delete
from django.dispatch import receiver
from .helpers import delete_file

from .models import Thread


@receiver(post_delete, sender=Thread)
def clean_files(sender, instance, **kwargs):
    if instance.image:
        delete_file(instance.image.path)
