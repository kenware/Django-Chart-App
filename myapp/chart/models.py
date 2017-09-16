# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Channel(models.Model):
    channel_text = models.CharField(max_length=200)
    category = models.CharField(default='other',max_length=500)
    date_created = models.DateTimeField()
    def __str__(self):
        return self.channel_text
    

class Chat(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    chat_text = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    date_chat = models.DateTimeField()
    def __str__(self):
        return self.chat_text
