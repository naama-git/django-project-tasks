from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Member


def home(request):
    return render(request, "homePage.html")



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            team = form.cleaned_data['team']

            Member.objects.create(
                user=user,
                team=team
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("logged in")
            return redirect('home')
    else:

        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



def tasksList(request):
   if request.user.is_authenticated:
         member = Member.objects.get(user=request.user)
         tasks = member.team.memebers.all()
         return render(request, 'tasksList.html', {'tasks': tasks})
   else:
       return redirect('login')
   

    