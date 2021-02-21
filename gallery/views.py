from . forms import *
from .models import *
from django.shortcuts import render
from django.contrib.auth.models import User as authUser
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.views import View
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


def register(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = SignUpForm(request.POST or None)
    return render(request, 'register.html', {'form': form})

def upload_image(request):
	form = ImagesForm(request.POST or None,request.FILES or None)
	template = 'imageForm.html'
	context = {"form": form}
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/')
	else: 
		form = ImagesForm(request.POST or None,request.FILES or None)   
	return render(request, template, context)

def gallery(request):
	template = 'gallery.html'
	data_count = Images.objects.all().count()
	data = Images.objects.all().order_by('-id')
	context = {
				'data':data,
				'data_count':data_count,
				}
	return render(request, template, context)

def filtergalleryData(request,image_type=None):
	template = 'gallery.html'
	data_count = Images.objects.filter(image_type=image_type).count()
	data = Images.objects.filter(image_type=image_type).order_by('-id')
	context = {
				'data':data,
				'data_count':data_count,
				}
	return render(request, template, context)
