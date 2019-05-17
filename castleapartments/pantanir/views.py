from django.shortcuts import render
from eignir.models import Eign
from pantanir.models import Pantanir
import datetime



def stadfesta(request, id):
    # þetta er til þess að við getum farið með kortaupplýsingarnar yfir á næstu síðu til staðfestingar
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
    eign = Eign.objects.get(id=id)
    #dagsetningin sem eignin er keypt
    date=datetime.date.today().strftime("%B %d, %Y")

    #þegar eign er keypt setjum við allar upplýsingar sem við þurfum um hana í pantanir töfluna
    instance = Pantanir.objects.create(heimilisfang=eign.heimilisfang, baejarfelag=eign.baejarfelag,
                                       postnumer=eign.postnumer, verd=eign.verd,
                                       brunabotamat=eign.brunabotamat, fasteignamat=eign.fasteignamat,
                                       tegund=eign.tegund, staerd=eign.staerd,
                                       byggingarar=eign.byggingarar, sett_a_solu=eign.sett_a_solu,
                                       fjoldi_svefnherberga=eign.fjoldi_svefnherberga,
                                       fjoldi_badherberga=eign.fjoldi_badherberga,
                                       fjoldi_herbergja=eign.fjoldi_herbergja, nafn_seljanda=eign.nafn_seljanda,
                                       simi_seljanda=eign.simi_seljanda, netfang_seljanda=eign.netfang_seljanda,
                                       starfsmenn=eign.starfsmenn, nafn_kaupanda=request.user.profile.fullt_nafn,
                                       simi_kaupanda=request.user.profile.simi, netfang_kaupanda=request.user.profile.netfang,
                                       kennitala_kaupanda=request.user.profile.kennitala,
                                       heimilisfang_kaupanda=request.user.profile.heimilisfang,
                                       borg_kaupanda=request.user.profile.borg, land_kaupanda=request.user.profile.land,
                                       postnr_kaupanda=request.user.profile.postnr, notandanafn=request.user)

    #eyðum eigninni út út eign töflunni þegar eignin er keypt
    context = {'eign': Eign.objects.filter(id=id).delete(),
               'pantanir': Pantanir.objects.all().last(),
               'date': date}
    return render(request, 'pantanir/kvittun.html', context)




