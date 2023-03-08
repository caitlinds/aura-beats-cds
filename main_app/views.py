import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Mood, User, Song, Video
from datetime import date
import requests


def home(request):
    return render(request, 'home.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credientals, please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def search_video(request):
    search_term = request.GET.get('q')
    response = requests.get(
        f'{os.environ["YOUTUBE_ROOT"]}q={search_term}&type=video&key={os.environ["YOUTUBE_API"]}&maxResults=10')
    data = response.json()
    videos = []
    for item in data['items']:
        title = item['snippet']['title']
        video = {
            'title': title,
            'thumbnail': item['snippet']['thumbnails']['default']['url'],
            'video_id': item['id']['videoId'],
            'description': item['snippet']['description'],
        }
        videos.append(video)
    moods = Mood.objects.filter(user=request.user)
    print(moods.count())
    return render(request, 'songs/search_song.html', {
        'videos': videos,
        'search_term': search_term,
        'moods': moods
    })


def search_page(request):
    return render(request, 'songs/search_page.html')


def about(request):
    return render(request, 'about.html')


@login_required
def moods_index(request):
    moods = Mood.objects.all().order_by('-id').values()
    return render(request, 'moods/index.html', {'moods': moods})


@login_required
def moods_detail(request, mood_id):
    mood = Mood.objects.get(id=mood_id)
    return render(request, 'moods/detail.html', {
        'mood': mood
    })

# def favorites(request, mood_id):
#     mood = get_object_or_404(Mood, pk=mood_id)
#     if mood.favorites.filter(id=request.user.ide).exist():
#         mood.favorites.remove(request.user)
#     else:
#         mood.favorites.add(request.user)
#     return render(request, 'moods/favorites.html')

# def mood_favorite_list(request, id):
#     user=request.user
#     favorite_moods = user.favorites.all()
#     context = {
#         'favorite_moods': favorite_moods
#     }
#     return render(request, 'moods/favorites.html', context)


@login_required
def my_moods(request):
    userz = request.user
    moods_list = Mood.objects.filter(
        user=request.user).order_by('-id').values()
    return render(request, 'main_app/mood_list.html', {'moods': moods_list, 'user': userz})


class MoodCreate(CreateView):
    model = Mood
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class MoodUpdate(UpdateView):
    model = Mood
    fields = ['description']


class MoodDelete(DeleteView):
    model = Mood
    success_url = '/moods'


class SongList(ListView):
    model = Song


class SongDetail(DetailView):
    model = Song


class SongCreate(CreateView):
    model = Song
    fields = '__all__'


class SongUpdate(UpdateView):
    model = Song
    fields = ['title', 'url']


class SongDelete(DeleteView):
    model = Song
    success_url = '/songs'


def add_to_mood(request):
    if request.method == "POST":
        try:
            video, created = Video.objects.get_or_create(
                video_id=request.POST.get(video_id),
                defaults={
                    "title": request.POST.get(video_title),
                    "thumbnail": request.POST.get(video_thumbnail),
                    "description": request.POST.get(video_description),
                }
            )
            mood_id = request.POST.get(mood_id)
            mood = Mood.objects.get(id=mood_id)
            mood.videos.add(video_id)
        except Exception as e:
            print(e)
    return redirect('search_video')
