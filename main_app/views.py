from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def moods_index(request):
  return render(request, 'moods/index.html', {
    'moods': moods
  })