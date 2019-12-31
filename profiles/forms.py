from django import forms

from profiles import models


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('username', 'password', 'max_ip',)
