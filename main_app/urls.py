from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('moods/', views.moods_index, name='index'),
  path('moods/<int:mood_id>/', views.moods_detail, name='detail'),
  path('moods/create/', views.MoodCreate.as_view(), name='moods_create'),
  path('moods/<int:pk>/update/', views.MoodUpdate.as_view(), name='moods_update'),
  path('moods/<int:pk>/delete/', views.MoodDelete.as_view(), name='moods_delete'),
  path('', views.favorites, name='favorites'),
  path('favorites/<int:id>/', views.mood_favorite_list, name='mood_favorite_list'),
  path('moods/my_moods', views.my_moods, name='my_moods'),
]