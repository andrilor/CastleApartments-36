from django.shortcuts import render, get_object_or_404
from eignir.models import Eign
from opinhus.models import opinhus
from datetime import datetime
from user.models import leitarsaga



def index(request):

    eignir = Eign.objects.all()

    if request.GET:

        baejarfelag = Eign.objects.none()
        count = 0

        if 'reykjavik' in request.GET:
            baejarfelag = baejarfelag.union(Eign.objects.filter(baejarfelag__exact='REYKJAVÍK'))
        else:
            count = count +1

        if 'kopavogur' in request.GET:
            baejarfelag = baejarfelag.union(Eign.objects.filter(baejarfelag__exact='KÓPAVOGUR'))
        else:
            count = count + 1

        if 'akranes' in request.GET:
            baejarfelag = baejarfelag.union(Eign.objects.filter(baejarfelag__exact='AKRANES'))
        else:
            count = count + 1

        if 'selfoss' in request.GET:
            baejarfelag = baejarfelag.union(Eign.objects.filter(baejarfelag__exact='SELFOSS'))
        else:
            count = count + 1

        if count == 4:
            baejarfelag = Eign.objects.all()

        count = 0
        tegund = Eign.objects.none()

        if 'einbyli' in request.GET:
            tegund = tegund.union(Eign.objects.filter(tegund__exact='Einbýli'))
        else:
            count = count + 1

        if 'fjolbyli' in request.GET:
            tegund = tegund.union(Eign.objects.filter(tegund__exact='Fjölbýli'))
        else:
            count = count + 1

        if 'radhus' in request.GET:
            tegund = tegund.union(Eign.objects.filter(tegund__exact='Raðhús'))
        else:
            count = count + 1

        if 'haed' in request.GET:
            tegund = tegund.union(Eign.objects.filter(tegund__exact='Hæð'))
        else:
            count = count + 1

        if 'sumarhus' in request.GET:
            tegund = tegund.union(Eign.objects.filter(tegund__exact='Sumarhús'))
        else:
            count = count + 1

        if count == 5:
            tegund = Eign.objects.all()

        postnumer = Eign.objects.none()
        count = 0

        if 'hoe' in request.GET:
            postnumer = postnumer.union(Eign.objects.filter(postnumer__exact='101'))
        else:
            count = count + 1

        if 'hos' in request.GET:
            postnumer = postnumer.union(Eign.objects.filter(postnumer__exact='107'))
        else:
            count = count + 1

        if 'ah' in request.GET:
            postnumer = postnumer.union(Eign.objects.filter(postnumer__exact='800'))
        else:
            count = count + 1

        if 'hof' in request.GET:
            postnumer = postnumer.union(Eign.objects.filter(postnumer__exact='105'))
        else:
            count = count + 1

        if 'hot' in request.GET:
            postnumer = postnumer.union(Eign.objects.filter(postnumer__exact='112'))
        else:
            count = count + 1

        if 'hofj' in request.GET:
            postnumer = postnumer.union(Eign.objects.filter(postnumer__exact='104'))
        else:
            count = count + 1

        if 'hoth' in request.GET:
            postnumer = postnumer.union(Eign.objects.filter(postnumer__exact='113'))
        else:
            count = count + 1

        if count == 7:
            postnumer = Eign.objects.all()



        nidurstada = Eign.objects.none()

        if 'search' in request.GET:
            leitar_ord = request.GET['search']
            nidurstada = nidurstada.union(Eign.objects.filter(heimilisfang__icontains=leitar_ord))
        else:
            nidurstada = Eign.objects.all()

        eignir = baejarfelag.intersection(tegund, nidurstada, postnumer)


    context = {'eignir': eignir}
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

#Sortar eignum eftir réttri bókstafsröð - Fannar
def alphebeticallySortedEignDesc(request):
    context = {'eignir': Eign.objects.order_by('heimilisfang')}
    return render(request, 'eignir/index.html', context)

#Sortar eignum eftir öfugri bókstafsröð - Fannar
def alphebeticallySortedEignAsc(request):
    context = {'eignir': Eign.objects.order_by('-heimilisfang')}
    return render(request, 'eignir/index.html', context)

#Sortar eignum eftir verði, hæst fyrst - Fannar
def priceSortedEignDesc(request):
    context = {'eignir': Eign.objects.order_by('-verd')}
    return render(request, 'eignir/index.html', context)

#Sortar eignum eftir verði, lægst fyrst - Fannar
def priceSortedEignAsc(request):
    context = {'eignir': Eign.objects.order_by('verd')}
    return render(request, 'eignir/index.html', context)

def historylog(request ,eign):
    # þegar notandi ýttir á eign og er login þa kemur færsla í history log svo hægt er að halda utan um leitar sögu notenda -Andri
    logs = leitarsaga(notandanafn_id=request.user.id, eign_id=eign.id)
    logs.save()
