from importlib import import_module
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpRequest, SimpleCookie
from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("newUserProfile")
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            u = request.user
            u.email = profile.netfang
            u.save()
            return redirect('index-mittsvaedi')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })

def newUser(request):
    #Tekkur þig til að sjá from-ið annars virkar ekki að inserta upplisingar fyrir newUser_upplysingat -Andri
    return render(request, 'user/newUserProfile.html', {})

def newUser_upplysingar(request):
    #eins og profile nema er nottað í lokuðu umhverfi og linkar a önnur url -Andri
    newUser_upplysingar = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=newUser_upplysingar, data=request.POST)
        if form.is_valid():
            newUser_upplysingar = form.save(commit=False)
            newUser_upplysingar.user = request.user
            newUser_upplysingar.save()
            return redirect('index-forsida')
    return render(request, 'user/newUser_upplysingar.html', {
        'form': ProfileForm(instance=newUser_upplysingar)
    })

"""
#logout og delete_user áttu að vera nýtt til að leifa user að hætta við að búa til notenda en fékk það ekki til að virka -Andri 
def logout(self, username):
    
    from django.contrib.auth import get_user, logout

    u = User.objects.get(username=username)

    request = HttpRequest()
    engine = import_module(settings.SESSION_ENGINE)
    if self.session:
        request.session = self.session
        request.user = get_user(request)
    else:
        request.session = engine.SessionStore()
    logout(request)
    self.cookies = SimpleCookie()
    delete_user(u)

def delete_user(request, username):
    context = {}
    try:
        u = User.objects.get(username=username)
        u.delete()
        context['msg'] = 'The user is deleted.'
    except User.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = e.message

    return render(request, 'forsida/index.html', context=context)
"""
