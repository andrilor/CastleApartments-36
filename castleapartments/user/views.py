from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
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
            return redirect('index-mittsvaedi')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })

def newUser(request):
    return render(request, 'user/newUserProfile.html', {})

def newUser_upplysingar(request):
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