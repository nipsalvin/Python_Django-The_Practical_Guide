from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() #Since we are now using a ModelForm, we don't need to create an object, we can just save the form
            return HttpResponseRedirect('/thank_you/')
        return render(request, 'reviews/review.html', {'form': form})

# def review(request):
#     # if request.method == 'POST':
#     #     username = request.POST.get('username')
#     #     print(username)
#     #     if username == '':
#     #         has_error = True
#     #         return render(request, 'reviews/review.html', {'has_error': has_error})
#     #     return HttpResponseRedirect('/thank_you/')

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # review = Review(
#             #     username=form.cleaned_data['username'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating'],
#             # )
#             # review.save()
#             form.save() #Since we are now using a ModelForm, we don't need to create an object, we can just save the form
#             return HttpResponseRedirect('/thank_you/')
#     else:
#         form = ReviewForm()
#     return render(request, 'reviews/review.html', {'form': form})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')