from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'fullt_nafn':widgets.TextInput(attrs={'class': 'form-control'}),
            'kennitala':widgets.NumberInput(attrs={'class': 'form-control'}),
            'heimilisfang': widgets.TextInput(attrs={'class': 'form-control'}),
            'netfang': widgets.EmailInput(attrs={'class': 'form-control'}),
            'simi':widgets.TextInput(attrs={'class': 'form-control'}),
            'mynd':widgets.TextInput(attrs={'class': 'form-control'}),
        }