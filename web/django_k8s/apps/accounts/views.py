from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin # Login required to see page

class ProfileView(LoginRequiredMixin, TemplateView): # inherit the TemplateView class and mix in the login-required constraint.
    template_name = 'accounts/profile.html' # rename template to 'accounts/profile.html'