from django.shortcuts import render
from starfsmenn.models import  Starfsmadur


def index(request):
    context = {'starfsmenn': Starfsmadur.objects.all().order_by('name')}
    return render(request, 'starfsmenn/index.html', context)