from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(label='Your Name', max_length=100, error_messages={
        'required': 'Please enter your name',
    })
    review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=200, help_text='Write your review here')
    rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)