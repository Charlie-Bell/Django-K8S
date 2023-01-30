import bleach
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail

from django_k8s.settings import DEFAULT_FROM_EMAIL
from .forms import ContactForm
# Create your views here.


def contact(request: HttpRequest) -> HttpResponse: # Request is a HttpRequest and returns a HttpResponse
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.clean(form.cleaned_data["name"])
            email = bleach.clean(form.cleaned_data["email"])
            message = bleach.clean(form.cleaned_data["message"])
            send_mail(f"{name} sent an email from {email}", message, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])
            send_mail(f"Message sent to Charlie Bell", f"Your message has been sent to Charlie Bell.\n\n Your message:\n{message}", DEFAULT_FROM_EMAIL, [email])
            return render(request, "contact.html", {"form": form, "success": True}) # Add "success" context variable. Very basic implementation.
    else:
        raise NotImplementedError

    return render(request, "contact.html", {"form": form}) # Add a form instance of class form