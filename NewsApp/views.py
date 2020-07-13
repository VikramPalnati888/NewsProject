from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
import pytz
import json
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
import uuid
from django.db.models import Q
from NewsApp.models import *

@login_required
def home(request):
	return render(request, 'home.html')


def login(request):
	if request.method == "POST":
		username, password = request.POST['username'], request.POST['password']
		user = authenticate(request,username=username, password=password)
		if user is not None:
			auth_login(request, user)
			user_name = request.user
			return render(request, 'home.html', {'user': user_name})
		else:
			messages.error(request, 'Invalid Login Credentials')
			return redirect('login')
	else:
		user_name = request.user
		return render(request, 'login.html', {'user': user_name})

def Logout(request):
    logout(request)
    return redirect('login')

@login_required
def NewsPost(request):
	if request.method == "POST":
		News.objects.create(Title= request.POST['Title'],Description=request.POST['Description'],Image=request.FILES['Image'])
		return redirect('news_get')
	return render(request, 'news_post.html', {'message':"data stored successful"})

@login_required
def NewsGet(request):
	if request.method == "GET":
		data = {}
		data_list = []
		news_qs = News.objects.all().order_by('-id')
		for dt in news_qs:
			data[dt.id] = {
							"Title": dt.Title,
							"Description": dt.Description,
							"Image": dt.Image.url,
							"Likes": dt.Likes,
							"Posted": dt.PostedDate.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d"),
							}
		data_list.append(data)
		return render(request, 'news.html', {'response':data_list})
