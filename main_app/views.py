from django.shortcuts import render

cats = [
  {'name': 'Happy', 'description': 'happy'},
  {'name': 'Blue', 'description': 'sad'},
]

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def moods_index(request):
  return render(request, 'moods/index.html', {
    'moods': moods
  })
