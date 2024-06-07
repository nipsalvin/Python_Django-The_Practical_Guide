from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(label='Your Name', max_length=100, error_messages={
        'required': 'Please enter your name',
        'max_length': 'Your name is too long'
    })
    