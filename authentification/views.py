from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import UserRegistrationForm
from .models import User


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'authentification/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            user = authenticate(request, email=email, password=password)
            if user is None:
                raise Exception

            login(request, user)

            return redirect('home')
        except Exception:
            messages.error(request, 'Invalid email or password')

            return render(request, 'authentification/login.html')


class RegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'authentification/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        res = super().form_valid(form)
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return res


class LogoutView(View):
    def get(self, request):
        logout(request)

        return render(request, 'authentification/login.html')
