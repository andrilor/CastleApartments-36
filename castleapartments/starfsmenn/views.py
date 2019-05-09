from django.shortcuts import render
from starfsmenn.models import  Starfsmenn


def index(request):
    context = {'starfsmenn': Starfsmenn.objects.all().order_by('name')}
    return render(request, 'starfsmenn/index.html', context)