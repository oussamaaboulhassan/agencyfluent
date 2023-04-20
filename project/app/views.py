from django.shortcuts import render
def index(response):
    return render(response, "app/index.html")
# Create your views here.
