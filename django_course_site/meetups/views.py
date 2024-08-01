from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetup
from .forms import RegistrationForm

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'meetups' : meetups,
    })

def meetup_details(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    try:
        if request.method == 'GET':
            form = RegistrationForm()
            context = {
                'meetup': meetup,
                'meetup_found' : True,
                'form': form,
            }
        elif request.method == 'POST':
            form = RegistrationForm(request.POST)
            context = {
                'meetup': meetup,
                'meetup_found' : True,
                'form': form,
            }
            if form.is_valid():
                participant = form.save()
                meetup.participants.add(participant)
                return redirect('confirm_registration')
        return render(request, 'meetups/meetup-details.html', context)
    except Exception as exc:
        print(exc)
        context = {
            'meetup_found':False
        }
        return render(request, 'meetups/meetup-details.html', context)

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')