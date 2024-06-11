from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
import os

from .forms import ProfileForm

# Create your views here.

def store_file(file):
    temp_path = os.path.join(os.path.dirname(os.getcwd()), 'temp/image.jpg')
    with open(temp_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            print(f'Storing file: {chunk} of {file} ({file.name})')

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'profiles/create_profile.html', {'form': form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            store_file(request.FILES.get('user_image'))
            return HttpResponseRedirect('/profiles')

        return render(request, 'profiles/create_profile.html', {'form': submitted_form})