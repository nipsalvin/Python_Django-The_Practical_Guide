from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def january(request):
    return HttpResponse('Run atleast 50 KM this month')


def february(request):
    return HttpResponse('Walk for atleast 20 mins each day!')

def march(request):
    return HttpResponse('Learn python for atleast 20 mins each day!')

def monthly_challenges(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Run atleast 50 KM this month'
    elif month == 'february':
        challenge_text = 'Walk for atleast 20 mins each day!'
    elif month == 'march':
        challenge_text = 'Learn python for atleast 20 mins each day!'
    else:
        return HttpResponseNotFound('This is not a valid month')
    return HttpResponse(challenge_text)
