from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from photoalbum.forms import AddPhotoForm, LoginForm
from photoalbum.models import Photo


class MainView (LoginRequiredMixin, View):
    login_url = "/login"
    def get(self, request):
        form = AddPhotoForm()
        photos = Photo.objects.all()
        return render(request, "main.html", {"photos":photos, "form":form})

    def post(self, request):
        form = AddPhotoForm(request.POST, request.FILES)
        photos = Photo.objects.all()
        if form.is_valid():
            path = form.cleaned_data['path']
            user = request.user
            image = form.files['image']
            Photo.objects.create(path=path, user=user, image=image)
            return redirect('/')
        else:
            return render(request, "main.html", {"photos":photos, "form":form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", context={"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.get(email=email)
            user = authenticate (username=user.username, password=password)
            if user is not None:
                login (request, user)
                return redirect (reverse ("main_view"))
            else:
                return HttpResponse ("bledy login lub haslo")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect (reverse ("login_view"))