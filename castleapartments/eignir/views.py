from django.shortcuts import render, get_object_or_404
from eignir.models import Eign
from opinhus.models import opinhus
from datetime import datetime
from user.models import leitarsaga


def index(request):
    context = {'eignir': Eign.objects.all()}
    return render(request, 'eignir/index.html', context)

def uppl_um_eign(request, id):
    eign = get_object_or_404(Eign, pk=id)
    dagur = datetime.now()
    opidhus = opinhus.objects.filter(eign=eign)
    if request.user.is_authenticated:
        historylog(request, eign)
    return render(request, 'eignir/eignir_upplysingar.html', {
        'eign': eign, 'opidhus': opidhus, 'dagur': dagur
    })

def alphebeticallySortedEignDesc(request):
    context = {'eignir': Eign.objects.order_by('heimilisfang')}
    return render(request, 'eignir/index.html', context)

def alphebeticallySortedEignAsc(request):
    context = {'eignir': Eign.objects.order_by('-heimilisfang')}
    return render(request, 'eignir/index.html', context)

def priceSortedEignDesc(request):
    context = {'eignir': Eign.objects.order_by('-verd')}
    return render(request, 'eignir/index.html', context)

def priceSortedEignAsc(request):
    context = {'eignir': Eign.objects.order_by('verd')}
    return render(request, 'eignir/index.html', context)

def historylog(request ,eign):
    logs = leitarsaga(notandanafn_id=request.user.id, eign_id=eign.id)
    logs.save()
