from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm


def account(request):
    if request.user:                                                     # if user is logged in
        username = request.user.get_username()
    else:
        username = "Error: you need to login"
    print("username: " + username)
    context = {'username': username}
    return render(request, '../templates/account/account.html', context)


def logout_view(request):
    user = request.user
    if user:
        logout(request)
        return render(request, '../templates/account/account.html')
    else:
        return render(request, '../templates/account/account.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {'form': form,
                           'username': username}

                return render(request, '../templates/account/account.html', context)
            else:
                context = {'form': form,
                           'error': 'The username and password combination is incorrect'}

                return render(request, '../templates/account/login.html', context)

        else:
            context = {'form': form}
            return render(request, '../templates/account/login.html', context)
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, '../templates/account/login.html', context)


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')

            login(request, user)
            context = {'username': username}
            return redirect('account')
    else:
        form = ExtendedUserCreationForm()

    context = {'form': form}
    return render(request, '../templates/account/register.html', context)
