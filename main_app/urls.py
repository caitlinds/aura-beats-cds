from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('songs/search_page/', views.search_page, name='search_page'),
  path('accounts/signup/', views.signup, name='signup'),
  path('moods/', views.moods_index, name='index'),
  path('moods/<int:mood_id>/', views.moods_detail, name='detail'),
  path('moods/create/', views.MoodCreate.as_view(), name='moods_create'),
  path('moods/<int:pk>/update/', views.MoodUpdate.as_view(), name='moods_update'),
  path('moods/<int:pk>/delete/', views.MoodDelete.as_view(), name='moods_delete'),
  path('moods/my_moods', views.my_moods, name='my_moods'),
  path('songs/search/', views.search_video, name='search_video'),
  path('add_to_mood/', views.add_to_mood, name='add_to_mood'),
  path('moods/<int:mood_id>/add_photo/', views.add_photo, name='add_photo'),
]