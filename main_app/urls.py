from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('moods/', views.moods_index, name='index'),

]