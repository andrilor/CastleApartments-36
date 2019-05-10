from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'netfang':widgets.EmailInput(attrs={'class': 'form-control'}),
            'nafn':widgets.TextInput(attrs={'class': 'form-control'}),
            'eftirnafn': widgets.TextInput(attrs={'class': 'form-control'}),
            'simi':widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_mynd':widgets.TextInput(attrs={'class': 'form-control'}),
        }

