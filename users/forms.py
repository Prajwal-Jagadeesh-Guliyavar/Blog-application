from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email =forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email =forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    remove_image = forms.BooleanField(required=False, label='take off that ugly shit')
    class Meta:
        model = Profile
        fields = ['image']
    
    def save(self, commit=True):
        profile = super().save(commit = False)
        if self.cleaned_data.get('remove_image'):
            if profile.image.name != 'default.jpg':
                profile.image.delete(save = False)
            profile.image = 'default.jpg'

        if commit : 
            profile.save()
        return profile