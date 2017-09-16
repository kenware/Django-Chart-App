# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Channel, Chat
from .forms import *
from datetime import datetime
# Create your views here.
def index(request):
    clear_search= "";
    if request.method == 'POST':
        if "create_channel" in request.POST:  
          form = ChannelForm(request.POST);
          if form.is_valid():
            channel_name = form.cleaned_data['channel']
            category = form.cleaned_data['category']
            date = datetime.now()
            Channel.objects.create(channel_text=channel_name, date_created=date,category=category)
            channel = Channel.objects.all().order_by("-date_created");
        if "search_data" in request.POST:
            form2 = SearchForm(request.POST);
            if form2.is_valid():
              search=form2.cleaned_data["search"];
              channel = Channel.objects.filter(channel_text__icontains=search).order_by("-date_created");
              form = ChannelForm();
              clear_search= "**clear Search";
    else:
        form = ChannelForm();
        channel = Channel.objects.all().order_by("-date_created");
    categories = Channel.objects.all();
    cat=[];
    cat2=[];
    for category in categories:
        if category.category not in cat2:
           cat2.append(category.category);
           cat.append(category.id);
    form2 = SearchForm();
    context = {"channel":channel, "form": form, "form2":form2,"clear_search":clear_search, "cat":cat}
    return render(request, 'chart/index.html', context)
    
def room(request, channel_id):
    if request.method == 'POST':
       form=ChatForm(request.POST);
       if form.is_valid():
          message = form.cleaned_data['message']
          username = form.cleaned_data['username']
          date=datetime.now();
          Channel.objects.get(pk=channel_id).chat_set.create(chat_text=message,username=username,date_chat=date);
    channel = Channel.objects.get(pk=channel_id);
    form=ChatForm();
    context = {"channel":channel,"form":form,"channel_id":channel_id}
    return render(request, 'chart/chat.html', context)

def category(request, channel_id):
    channel = Channel.objects.get(pk=channel_id);
    channel = channel.category
    channel = Channel.objects.filter(category=channel).order_by("-date_created");
    form = ChannelForm();
    form2 = SearchForm();
    categories = Channel.objects.all();
    cat=[];
    cat2=[];
    for category in categories:
        if category.category not in cat2:
           cat2.append(category.category);
           cat.append(category.id);
    context = {"channel":channel, "form": form, "form2":form2, "cat":cat}
    return render(request, 'chart/index.html', context)


def Help(request):
    return render(request, 'chart/help.html')

def thought(request):
    return render(request, 'chart/thought.html')
    
