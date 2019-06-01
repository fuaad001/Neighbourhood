from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Neighbourhood, User, Business, Category, News, Service
from .forms import *
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def index(request):
    '''
    View function to user registration page
    '''
    current_user=request.user
    user=User.objects.filter(name = current_user).all()

    if user:
        return redirect('home')

    else:
        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save(commit=False)
                user.name = current_user
                user.save()
            return redirect('profile')
        else:
            form = UserForm()

    return render(request, 'index.html',{"form":form})

@login_required(login_url="/accounts/login/")
def home(request):
    '''
    View function to landing page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id
    news = News.objects.filter(neighbourhood_id = neighbourhood).all()
    businesses = Business.objects.filter(neighbourhood_id = neighbourhood).all()
    services = Service.objects.filter(neighbourhood_id = neighbourhood).all()

    return render(request, 'home.html', {'news':news,'current_user':current_user, "main_user":user, "businesses":businesses, "services":services})

@login_required(login_url="/accounts/login/")
def profile(request):
    '''
    View function for profile page
    '''
    title = request.user.username
    try:
        current_user=request.user
        profile=User.objects.get(name = current_user)
        neighbourhood = profile.neighbourhood_id

        if request.method == 'POST':
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                news = form.save(commit=False)
                news.user = current_user
                news.neighbourhood_id = neighbourhood
                news.save()
            return redirect('profile')
        else:
            form = NewsForm()

    except Exception as e:
        raise Http404()

    return render(request,"profile.html",{'profile':profile, "title":title, "form":form})

@login_required(login_url="/accounts/login/")
def services(request):
    '''
    View function for services page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id
    services = Service.objects.filter(neighbourhood_id = neighbourhood).all()

    return render(request, 'services.html', {'current_user':current_user, "main_user":user, "services":services})

def business(request):
    '''
    View function for business page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id
    businesses = Business.objects.filter(neighbourhood_id = neighbourhood).all()

    return render(request, 'business.html', {'current_user':current_user, "main_user":user, "businesses":businesses})

@login_required(login_url="/accounts/login/")
def about(request):
    '''
    View function for about page
    '''
    return render(request, 'about.html')

@login_required(login_url="/accounts/login/")
def user_admin(request):
    '''
    View function for admin Page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id
    news = News.objects.filter(neighbourhood_id = neighbourhood).all()
    businesses = Business.objects.filter(neighbourhood_id = neighbourhood).all()
    services = Service.objects.filter(neighbourhood_id = neighbourhood).all()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = current_user
            news.neighbourhood_id = neighbourhood
            news.save()
        return redirect('profile')
    else:
        form = NewsForm()

    if request.method == 'POST':
        neighbourhoodform = NeighbourhoodForm(request.POST, request.FILES)
        if neighbourhoodform.is_valid():
            neighbourhood = neighbourhoodform.save(commit=False)
            neighbourhood.admin = current_user
            neighbourhood.occupants_count = 1
            neighbourhood.save()
        return redirect('profile')
    else:
        neighbourhoodform = NeighbourhoodForm()

    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            business = businessform.save(commit=False)
            business.user = current_user
            business.neighbourhood_id = neighbourhood
            business.save()
        return redirect('profile')
    else:
        businessform = BusinessForm()

    if request.method == 'POST':
        categoryform = CategoryForm(request.POST, request.FILES)
        if categoryform.is_valid():
            category = categoryform.save(commit=False)
            category.save()
        return redirect('profile')
    else:
        categoryform = CategoryForm()

    if request.method == 'POST':
        serviceform = ServiceForm(request.POST, request.FILES)
        if serviceform.is_valid():
            service = serviceform.save(commit=False)
            service.neighbourhood_id = neighbourhood
            service.save()
        return redirect('profile')
    else:
        serviceform = ServiceForm()

    return render(request, 'admin.html', {'news':news,'current_user':current_user, "main_user":user, "businesses":businesses, "services":services, "form":form, "neighbourhoodform":neighbourhoodform, "businessform":businessform, "categoryform":categoryform, "serviceform":serviceform})
