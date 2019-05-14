from django.shortcuts import render, get_object_or_404
from eignir.models import Eign
from opinhus.models import opinhus

def index(request):
    context = {'eignir': Eign.objects.all()}
    return render(request, 'eignir/index.html', context)

def uppl_um_eign(request, id):
    eign = get_object_or_404(Eign, pk=id)
    opidhus = opinhus.objects.get(eign=eign)
    return render(request, 'eignir/eignir_upplysingar.html', {
        'eign': eign, 'opidhus': opidhus
    })
