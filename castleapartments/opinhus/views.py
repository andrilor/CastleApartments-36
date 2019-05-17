from django.shortcuts import render, get_object_or_404
from opinhus.models import opinhus
from django.utils import timezone

def index(request):
    #notað til að byrta öll opin hús -Andri
    context = {'opinhus': opinhus.objects.all(), 'curent_time': timezone.now()}
    return render(request, 'opinhus/index.html', context)

def check_if__opinhus_exists_by_eign(request, eign):
    return render(request, 'eignir/eignir_upplysingar.html', {
        'opidhus': opinhus.objects.filter(eign=eign)
    })