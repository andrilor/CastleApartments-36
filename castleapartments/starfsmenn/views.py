from django.shortcuts import render


def index(request):
    return render(request, 'starfsmenn/index.html')