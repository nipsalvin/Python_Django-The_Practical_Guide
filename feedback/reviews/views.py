from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

# class ReviewView(FormView):
#     template_name = 'reviews/review.html'
#     form_class = ReviewForm
#     success_url = '/thank_you/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    
class ReviewView(CreateView):
    template_name = 'reviews/review.html'
    form_class = ReviewForm
    success_url = '/thank_you/'

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, 'reviews/review.html', {'form': form})
    
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save() #Since we are now using a ModelForm, we don't need to create an object, we can just save the form
#             return HttpResponseRedirect('/thank_you/')
#         return render(request, 'reviews/review.html', {'form': form})

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


# def thank_you(request):
#     return render(request, 'reviews/thank_you.html')

# class ThankYouView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank_you.html')

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context

# class ReviewListView(TemplateView):
#     template_name = 'reviews/review_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reviews'] = Review.objects.all()
#         return context

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        base_queryset = super().get_queryset()
        data = base_queryset.filter(rating__gte=1)
        return data

# class SingleReviewView(TemplateView):
#     template_name = 'reviews/single_review.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['pk']
#         context['review'] = Review.objects.get(id=review_id)
#         return context

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = int(favorite_id) == loaded_review.id
        return context
    
class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)