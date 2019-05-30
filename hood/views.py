from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
# from .models import Image, Comment, Profile, Contact, Like
# from .forms import *
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

def index(request):
    '''
    View function to user registration page
    '''
    return render(request, 'index.html')

def home(request):
    '''
    View function to landing page
    '''
    return render(request, 'home.html')

def profile(request):
    '''
    View function for profile page
    '''
    return render(request, 'profile.html')

def services(request):
    '''
    View function for services page
    '''
    return render(request, 'services.html')

def business(request):
    '''
    View function for business page
    '''
    return render(request, 'business.html')

def about(request):
    '''
    View function for about page
    '''
    return render(request, 'about.html')

def admin(request):
    '''
    View function for admin Page
    '''
    return render(request, 'admin.html')
