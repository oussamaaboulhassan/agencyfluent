from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "app/index.html")

def exe(request):
    return render(request, "app/exe.html")