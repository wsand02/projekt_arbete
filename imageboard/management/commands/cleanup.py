from django.core.management import BaseCommand, CommandError
from imageboard.models import Thread
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Cleans up old threads'

    def handle(self, *args, **kwargs):
        twelve_h_ago = timezone.now()-timedelta(hours=12)
        OldThreads = Thread.objects.filter(date_created__lt=twelve_h_ago)
        objectsremoved = len(OldThreads)
        try:
            OldThreads.delete()
        except:
            raise CommandError("Reeeeeee!")
        self.stdout.write(
            f'Deleted {objectsremoved} threads. Mr. Clean did it again!')
