from django.shortcuts import render, get_object_or_404
from eignir.models import Eign
from starfsmenn.models import Starfsmenn

def index(request):
    context = {'eignir': Eign.objects.all(), 'starfsmenn': Starfsmenn.objects.all().order_by('nafn')}
    return render(request, 'forsida/index.html', context)

def get_eign_by_id(request, id):
    return render(request, 'eignir/eignir_upplysingar.html', {
        'eign': get_object_or_404(Eign, pk=id)
    })

def get_starfsmenn_by_id(request, id):
    return render(request, 'starfsmenn/starfsmadur_upplysingar.html', {
        'starfsmenn': get_object_or_404(Starfsmenn, pk=id)
    })