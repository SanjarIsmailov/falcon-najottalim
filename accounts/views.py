from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("falcon:product_list")


from django.shortcuts import render, redirect
from django.contrib.auth import login

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone_number", "date_of_birth", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


from django.shortcuts import render, redirect
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)  # Corrected form name
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("falcon:product_list")  # Ensure this URL name exists in urls.py
    else:
        form = CustomUserRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})
