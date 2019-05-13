from django.shortcuts import render
from opinhus.models import opinhus


def index(request):
    context = {'opinhus': opinhus.objects.all()}
    return render(request, 'opinhus/index.html', context)