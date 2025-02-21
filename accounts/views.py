from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .models import CustomUser


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["google_login_url"] = reverse_lazy("social:begin", args=["google-oauth2"])
        return context


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("falcon:product_list")


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CustomUserRegistrationForm

def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("falcon:product_list")
    else:
        form = CustomUserRegistrationForm()

    google_login_url = reverse_lazy("social:begin", args=["google-oauth2"])

    return render(request, "accounts/register.html", {"form": form, "google_login_url": google_login_url})



class CustomUserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone_number", "date_of_birth", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
