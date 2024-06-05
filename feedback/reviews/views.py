from django.shortcuts import render

# Create your views here.
def review(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        context = {'username':username}
        return render(request, 'reviews/thanks_you.html', context)
    return render(request, 'reviews/review.html')