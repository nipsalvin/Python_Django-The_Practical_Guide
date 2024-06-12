from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
import os

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

# def store_file(file):
#     temp_path = os.path.join(os.path.dirname(os.getcwd()), 'temp/image.jpg')
#     with open(temp_path, 'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)
#             print(f'Storing file: {chunk} of {file} ({file.name})')

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, 'profiles/create_profile.html', {'form': form})

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES.get('user_image'))
#             profile.save()
#             store_file(request.FILES.get('user_image'))
#             return HttpResponseRedirect('/profiles')

#         return render(request, 'profiles/create_profile.html', {'form': submitted_form})

class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles/profiles_list/'

class ProfilesView(ListView):
    template_name = 'profiles/user_profiles.html'
    model = UserProfile
    context_object_name = 'profiles'