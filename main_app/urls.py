from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('moods/', views.moods_index, name='index'),
  path('moods/<int:mood_id>/', views.moods_detail, name='detail'),
]