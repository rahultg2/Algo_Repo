from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Algomination/try4.html')

def search(request):
    return render(request, 'Algomination/search.html')