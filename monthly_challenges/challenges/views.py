from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


monthly_challenges = {
    'january': 'Run atleast 50 KM this month',
    'february': 'Walk for atleast 20 mins each day!',
    'march': 'Learn python for atleast 20 mins each day!',
    'april': 'Read 5 pages of a book daily',
    'may': 'Run atleast 50 KM this month',
    'june': 'Walk for atleast 20 mins each day!',
    'july': 'Learn python for atleast 20 mins each day!',
    'august': 'Read 5 pages of a book daily',
    'september': 'Run atleast 50 KM this month',
    'october': 'Walk for atleast 20 mins each day!',
    'november': 'Learn python for atleast 20 mins each day!',
    'december': 'Read 5 pages of a book daily',
}


def index(request):
    months_list = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.title()
        month_path = reverse(viewname='month-challenge', args=[month])
        months_list += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    response_data = f'<ul>{months_list}</ul>'
    return HttpResponse(content=response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        respose_data = f'<h1>{month.title()}: {challenge_text.title()}</h1>'
        return HttpResponse(respose_data)
    except:
        return HttpResponseNotFound('<h1>This is not a valid month</h1>')


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        challenge_month = months[month - 1]
        redirect_path = reverse(
            viewname='month-challenge', args=[challenge_month])
        # return HttpResponseRedirect(redirect_to='/challenges/' + challenge_month) # Instead of this
        # We can do this
        return HttpResponseRedirect(redirect_to=redirect_path)
    except:
        return HttpResponseNotFound(content='<h1>This is not a valid month</h1>')
