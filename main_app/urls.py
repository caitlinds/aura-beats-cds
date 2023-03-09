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
  # path('moods/favorites/', views.favorites, name='favorites'),
  # path('favorites/<int:id>/', views.mood_favorite_list, name='mood_favorite_list'),
  path('moods/my_moods', views.my_moods, name='my_moods'),
  path('moods/', views.SongList.as_view(), name='songs'),
  path('songs/<int:pk>/', views.SongDetail.as_view(), name='songs_detail'),
  path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
  path('songs/search/', views.search_video, name='search_video'),
  path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
  path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
  path('add_to_mood/', views.add_to_mood, name='add_to_mood'),
  path('moods/<int:mood_id>/add_photo/', views.add_photo, name='add_photo'),
]