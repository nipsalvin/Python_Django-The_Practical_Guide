from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.
def review(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     print(username)
    #     if username == '':
    #         has_error = True
    #         return render(request, 'reviews/review.html', {'has_error': has_error})
    #     return HttpResponseRedirect('/thank_you/')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return HttpResponseRedirect('/thank_you/')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {'form': form})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')