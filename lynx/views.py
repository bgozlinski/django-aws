from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from .models import Profile

from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'lynx/index.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Query User credentials by using commit=False
            current_user = form.save(commit=False)
            form.save()
            # Linking default profile picture to User(FK)
            profile = Profile.objects.create(user=current_user)

            return redirect('lynx:my-login')

    context = {'form': form}
    return render(request, 'lynx/register.html', context=context)


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('lynx:dashboard')

    context = {'form': form}
    return render(request, 'lynx/my-login.html', context=context)


@login_required(login_url='lynx:my-login')
def dashboard(request):
    return render(request, 'lynx/dashboard.html')


@login_required(login_url='lynx:my-login')
def profile_management(request):
    return render(request, 'lynx/profile-management.html')


def user_logout(request):
    auth.logout(request)
    return redirect('lynx:')
