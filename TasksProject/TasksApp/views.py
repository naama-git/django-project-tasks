from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Member, Task


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



def tasksListView(request):
  
   if request.user.is_authenticated:
         if request.user.is_superuser:
             tasks=Task.objects.all()
             return render(request, 'tasksList.html', {'tasks': tasks})
         member = Member.objects.filter(user=request.user).first()
         if member:
            team= member.team
            tasks=Task.objects.filter(team=team)
            return render(request, 'tasksList.html', {'tasks': tasks, 'member': member, 'team': team})
         
   else:
       return redirect('login')
   

def update_task_member(request, task_id):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=task_id)
        member = Member.objects.filter(user=request.user).first()
        if not member:
            return redirect('tasksList')
        if task.team == member.team:
            task.assigned_employee =member
            member.tasks.add(task)
            task.save()
        
    return redirect('tasksList')

def update_task_status(request, task_id):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=task_id)
        status = request.POST.get('new_status')
        member = Member.objects.filter(user=request.user).first()
        if not member:
            return redirect('tasksList')
        if task.assigned_employee == member:
            task.status = status
            task.save()
        
    return redirect('tasksList') 


   

    