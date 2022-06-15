from django.contrib import admin
from .models import Profile,Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)




# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         bio = request.POST.get('bio')
#         image = request.FILES.get('image')
        
#         user = User.objects.create_user(username=username, email=email, password=password)
#         profile = Profile.objects.create(user=user, profile_pic=image, bio=bio)
#         user.save()
#         profile.save()

#         if profile:
#             return redirect('login')

#     else:  
#         return render(request, 'registration/registration_form.html', {})   
#     form = RegisterForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=raw_password)
#         login(request, user)
#         user.save()
#         login(request, user)
        
#     return redirect('home')