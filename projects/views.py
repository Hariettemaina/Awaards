from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
# from .forms import NewProjectForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'projects/home.html',{'projects':projects})

@login_required(login_url='/accounts/login/') 
def rate_project(request,project_id):
    project=Project.objects.get(id=project_id)
    return render(request,"projects/project.html",{"project":project})