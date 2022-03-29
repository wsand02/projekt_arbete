from django.db import models
from django.shortcuts import reverse
from PIL import Image
from .helpers import random_file_name
from django.contrib.sessions.models import Session


class Thread(models.Model):
    name = models.CharField(max_length=80, default='Anonymous')
    session_key = models.CharField(max_length=255)
    subject = models.CharField(max_length=300)
    comment = models.TextField(max_length=10000, blank=True)
    image = models.ImageField(upload_to=random_file_name, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'threads'
        ordering = ['-date_created']

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('thread', args=(self.pk,))


class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=255)
    name = models.CharField(max_length=80, default='Anonymous')
    comment = models.TextField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'replies'
        ordering = ['-date_created']

    def __str__(self):
        return self.thread.subject + " / " + self.comment[:50]

    def get_absolute_url(self):
        return reverse('thread', args=(self.thread.pk,))
