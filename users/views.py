from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import json
import folium

# auth
from django.contrib.auth.decorators import login_required

# models
from . models import *

# FORMS CONFIG FILE
from .forms import CreateUserForm
# from notifications.models import *

# Create your views here.
def login_view(req):
    if req.user.is_authenticated:
        return redirect('/dashboard')
    else:
        if  req.method == "POST":
            username = req.POST['username']
            password = req.POST['password']
            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                return redirect('dashboard/')
            else:
                messages.success(req, ( "There was an error, try again" ))
                return redirect('/')

        else:
            return render(req, 'auth/login.html')


def register_view(req):
    return render(req, 'auth/register.html')


@login_required(login_url = '/')
def dashboard_view(req):
    user = req.user
    profile = Profile.objects.get(user=user)
    if (profile) {
        ...
    } else {
        newProfile = Profile(phone_number='add phone number',home_address='add home address', latitude=0.0,longitude=0.0)
        newProfile.save()

    }
    context = {
        'user_obj': user,
    }
    return render(req, 'dashboard/dashboard.html', context)


@login_required(login_url = '/')
def userProfileView(req):
    return render(req, 'dashboard/profile.html')


@login_required(login_url = '/')
def userProfileEdit(req):
    return render(req, 'dashboard/profile-edit.html')


@login_required(login_url = '/')
def userProfileUpdate(req):
    user = req.user
    profile = Profile.objects.get(user=user)
    if  req.method == "POST":
        profile.phone_number     = req.POST.get("phone_number")
        profile.home_address     = req.POST.get("home_address")
        profile.save()

        user.username            = req.POST.get("username")
        user.first_name          = req.POST.get("first_name")
        user.last_name           = req.POST.get("last_name")
        user.email               = req.POST.get("email")
        user.save()

    return redirect('/profile/view')


@login_required(login_url = '/')
def userProfileLocation(req):
    user = req.user
    profile = Profile.objects.get(user=user)
    if  req.method == "POST":
        profile.latitude         = float(req.POST.get("latitude"))
        profile.longitude        = float(req.POST.get("longitude"))
        profile.save()

    return HttpResponse('')


@login_required(login_url = '/')
def usersLocationMap(req):
    profile = Profile.objects.get(user=req.user)
    m = folium.Map(location=[0, 10], zoom_start=3)
    folium.Marker([profile.latitude, profile.longitude]).add_to(m)
    m = m._repr_html_()
    context = {
    'm': m,
    }
    return render(req, 'dashboard/map.html', context)


def userSignup(req):
    if req.user.is_authenticated:
        return redirect('/dashboard')
    else:
        form = CreateUserForm()

        if req.method == 'POST':
            form = CreateUserForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

    context = {'form': form}
    return render(req, 'auth/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')