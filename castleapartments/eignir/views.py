from django.shortcuts import render, get_object_or_404
from eignir.models import Eign

def index(request):
    context = {'eignir': Eign.objects.all()}
    return render(request, 'eignir/index.html', context)

def get_eign_by_id(request, id):
    return render(request, 'eignir/eignir_upplysingar.html', {
        'eign': get_object_or_404(Eign, pk=id)
    })
