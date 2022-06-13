from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.home,name='home'),
    path('projects/project/',views.rate_project,name='rate-project'),
    path('pojects/profile',views.view_profile,name='view-profile'),
    path('search/', views.search_project, name='search_project'),
    path('new/project', views.new_project, name='new_project'),
    path('projectsapi/api/profile/', views.ProfileList.as_view(),name='api-profile'),
    path('projectsapi/api/project/', views.ProjectList.as_view(),name='api-project'),
    path('projectsapi/',views.api_page,name='api-page'),
    path('register/',views.register, name='register'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)