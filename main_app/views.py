import os
import uuid
import boto3
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Mood, User, Video, Photo
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
    videos = []
    params = {
        'key': os.environ['YOUTUBE_API'],
        'q': search_term,
        'type': 'video',
        'part': 'snippet',
        'maxResults': 10,
    }
    response = requests.get(
        f'{os.environ["YOUTUBE_ROOT"]}search', params=params)
    data = response.json()
    if 'items' in data:
        for item in data['items']:
            title = item['snippet']['title']
            video = {
                'title': title,
                'thumbnail': item['snippet']['thumbnails']['high']['url'],
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


def add_to_mood(request):
    if request.method == "POST":
        video_id = request.POST.get('video_id')
        video_title = request.POST.get('video_title')
        video_thumbnail = request.POST.get('video_thumbnail')
        video_description = request.POST.get('video_description')
        mood_id = request.POST.get('mood_id')
        if video_id and video_title and video_thumbnail:
            try:
                video, created = Video.objects.get_or_create(
                    video_id=video_id,
                    defaults={
                        "title": video_title,
                        "thumbnail": video_thumbnail,
                        "description": video_description,
                    }
                )
                video.save()
                mood = Mood.objects.get(id=mood_id)
                mood.videos.add(video.id)
            except Exception as e:
                print(e)
    return redirect('search_video')


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
        'mood': mood,
    })

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

def add_photo(request, mood_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, mood_id=mood_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', mood_id=mood_id)
