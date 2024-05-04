from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    'december': None,
}


def index(request):
    context_data = {}
    months = list(monthly_challenges.keys())
    context_data['months'] = months
    return render(request, 'challenges/index.html', context_data)


def monthly_challenge(request, month):
    try:
        context_data = {}
        challenge_text = monthly_challenges[month]
        context_data['text'] = challenge_text
        context_data['month'] = month
        return render(request=request, template_name='challenges/challenge.html', context=context_data)
    except:
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
        raise Http404() #When using `raise Http404`, you need to set Debug=False


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
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(content=response_data)
        raise Http404() #When using `raise Http404`, you need to set Debug=False
