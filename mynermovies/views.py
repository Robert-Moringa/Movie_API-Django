from django.shortcuts import render
import requests

# Create your views here.
API_KEY='205149d875ac06e78139b835ea493bc5'
BASE_URL='https://api.themoviedb.org/3/'
def welcome(request):
    url=f'{BASE_URL}trending/movie/week?api_key={API_KEY}'
    trending=requests.get(url)
    result=trending.json()
    return render(request, 'index.html', {"movies": result})
