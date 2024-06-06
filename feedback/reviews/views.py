from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        if username == '':
            has_error = True
            return render(request, 'reviews/review.html', {'has_error': has_error})
        return HttpResponseRedirect('/thank_you/')
    return render(request, 'reviews/review.html', {'has_error': False})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')