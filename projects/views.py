from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login

import projects
from .models import Profile,Project
from .forms import NewProjectForm,ProfileUpdateForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from django.contrib import auth
from django.contrib import messages

from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.
def register(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user = User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        profile=Profile.objects.create(user=user,email=user.email)
        
        # form = RegisterForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     raw_password = form.cleaned_data.get('password1')
        #     user = authenticate(username=username, password=raw_password)
        #     login(request, user)
        #     user.save()
        # 	login(request, user)
        # 	messages.success(request, "Registration successful." )
        # 	return redirect('home')
        # messages.error(request, "Unsuccessful registration. Invalid information.")
        return redirect('login')
    else:
        form = RegisterForm()

    return render (request,"registration/registration_form.html", context={"form":form})

def home(request):
    projects=Project.objects.all()
    return render(request,'projects/home.html',{'projects':projects})

@login_required(login_url='/accounts/login/') 
def rate_project(request,project_id):
    project=Project.objects.get(id=project_id)
    return render(request,"projects/project.html",{"project":project})

@login_required(login_url='/accounts/login/') 
def view_profile(request):
    projects=request.user.profile.project_set.all() 
    profile=request.user.profile
    
    form=ProfileUpdateForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    context={
        'form':form,
        'projects':projects,
    }
    return render(request,"projects/profile.html",context=context)


# def register(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         password1=request.POST['password1']
#         password2=request.POST['password2']
#         user = User.objects.create_user(username=username,email=email,password=password1)
#         user.save()
#         Profile=Profile.objects.create(user=user,email=user.email)
        
#         return redirect('login')
#     else:
#         return render(request,'registration/registration_form.html')



@login_required(login_url='/accounts/login/') 
def search_project(request):
    if "project" in request.GET and request.GET["project"]:
        search_term=request.GET.get("project")
        searched_projects=Project.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'projects/search.html',{"message":message, "projects":searched_projects, "project":search_term})
    
    else:
        message = "Please enter search name"

        return render(request, 'projects/search.html',{"message":message})

@login_required(login_url='/accounts/login/')     
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
        
    else:
        form = NewProjectForm()
    return render(request, 'projects/new_project.html', {"form":form, "current_user":current_user})

def single_project(request,id):
    project = Project.objects.get(id=id)
    return render(request,'projects/project.html', {'project': project})
    
@login_required(login_url='/accounts/login/')   
def api_page(request):
    return render(request,'projects/api_page.html')



class ProfileList(APIView):
    def get(self, request, fromat=None):
        all_profiles =Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self, request, fromat=None):
        all_projects =Project.objects.all()
        serializers =ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)