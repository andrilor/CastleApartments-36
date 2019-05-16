from django.shortcuts import render
from eignir.models import Eign



def stadfesta(request, id):
    context = {'card': request.POST['cardnumber'],
               'name': request.POST['cardname'],
               'expmonth': request.POST['expmonth'],
               'expyear': request.POST['expyear'],
               'cvc': request.POST['cvv'],
               'eign': Eign.objects.get(id=id),
               }

    return render(request, 'pantanir/pontun_stadfesta.html', context)


def index(request, id):
    context = {'eign': Eign.objects.get(id=id)}
    return render(request, 'pantanir/index.html', context)



def kvittun(request,id):
    context = {'eign': Eign.objects.get(id=id)}
    return render(request, 'pantanir/kvittun.html', context)
