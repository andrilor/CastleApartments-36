from django.shortcuts import render, get_object_or_404
from opinhus.models import opinhus

def index(request):
    context = {'opinhus': opinhus.objects.all()}
    return render(request, 'opinhus/index.html', context)

def get_opinhus_by_id(request, id):
    return render(request, 'opinhus/opinhus_upplysingar.html', {
        'opidhus': get_object_or_404(opinhus, pk=id)
    })

def check_if__opinhus_exists_by_eign(request, eign):
    return render(request, 'eignir/eignir_upplysingar.html', {
        'opidhus': opinhus.objects.filter(eign=eign)
    })