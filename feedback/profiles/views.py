from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
import os

# Create your views here.

def store_file(file):
    import ipdb; ipdb.set_trace()
    temp_path = os.path.join(os.path.dirname(os.getcwd()), 'temp/image.jpg')
    with open(temp_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            print(f'Storing file: {chunk} of {file} ({file.name})')

class CreateProfileView(View):
    def get(self, request):
        return render(request, 'profiles/create_profile.html')

    def post(self, request):
        store_file(request.FILES.get('image'))
        return HttpResponseRedirect('/profiles')