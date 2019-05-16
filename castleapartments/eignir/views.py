from django.shortcuts import render, get_object_or_404
from eignir.models import Eign
from opinhus.models import opinhus
from datetime import datetime

def index(request):

    if request:
        eignir = Eign.objects.none()

        if 'search' in request.GET:
            leitar_ord = request.GET['search']
            eignir += eignir.filter(heimilisfang__icontains=leitar_ord)

        if 'reykjavik' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='REYKJAVÍK')

        if 'kopavogur' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='KÓPAVOGUR')

        if 'akranes' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='AKRANES')

        if 'selfoss' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='SELFOSS')

        if 'einbyli' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='Einbýli')

        if 'fjolbyli' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='Fjölbýli')

        if 'radhus' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='Raðhús')

        if 'haed' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='Hæð')

        if 'sumarhus' in request.GET:
            eignir += eignir.filter(baejarfelag__exact='Sumarhús')

    else:
        eignir = Eign.objects.all()


    context = {'eignir': eignir}
    return render(request, 'eignir/index.html', context)

def uppl_um_eign(request, id):
    eign = get_object_or_404(Eign, pk=id)
    dagur = datetime.now()
    opidhus = opinhus.objects.filter(eign=eign)

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
