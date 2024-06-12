from django import forms

class ProfileForm(forms.Form):
    # user_image = forms.FileField()
    user_image = forms.ImageField()