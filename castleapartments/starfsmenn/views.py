from django.shortcuts import render, get_object_or_404
from starfsmenn.models import Starfsmenn

def index(request):
    context = {'starfsmenn': Starfsmenn.objects.all().order_by('nafn')}
    return render(request, 'starfsmenn/index.html', context)

def get_starfsmenn_by_id(request, id):
    return render(request, 'starfsmenn/starfsmadur_upplysingar.html', {
        'starfsmenn': get_object_or_404(Starfsmenn, pk=id)
    })