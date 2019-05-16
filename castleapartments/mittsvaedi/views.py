from django.shortcuts import render, get_object_or_404
from user.models import Profile, leitarsaga


def index(request):
    return render(request, 'mittsvaedi/index.html')

def get_profile_by_id(request, id):
    return render(request, 'mittsvaedi/index.html', {
        'profile': get_object_or_404(Profile, pk=id),
    })

def leitar_saga(request):
    context = {'leitarsaga': leitarsaga.objects.filter(profile_id=request.user.id)}
    return render(request, 'mittsvaedi/leitarsaga.html', context)
