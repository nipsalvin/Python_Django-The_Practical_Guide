from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(label='Your Name', max_length=100)
    review = forms.CharField(label='Your Review', widget=forms.Textarea, max_length=200)
    # submit = forms.submit(label='Submit')