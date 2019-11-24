from django.shortcuts import render, redirect, reverse
from .forms import UserSignupForm, StudentDetailForm, AlumniDetailForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            profile = form.cleaned_data.get('profile')
            if profile=='student':
                return redirect('student_profile')
            else:
                return redirect('alumni_profile')

    else:
        form = UserSignupForm()

    context = {'form': form}
    return render(request, 'authentication/signup.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('addpost'))
            else:
                return HttpResponse("Your registration was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'authentication/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('login'))


def student_profile(request):
    if request.method == 'POST':
        form = StudentDetailForm(request.POST)
        if form.is_valid:
            student_form = form.save(commit=False)
            student_form.user = request.user
            student_form.save()
            return redirect(reverse('addpost'))
    else:
        form = StudentDetailForm()

    return render(request, 'authentication/student_profile.html', {'form':form})


def alumni_profile(request):
    if request.method == 'POST':
        form = AlumniDetailForm(request.POST)
        if form.is_valid:
            alumni_form = form.save(commit=False)
            alumni_form.user = request.user
            alumni_form.save()
            return redirect(reverse('addpost'))
    else:
        form = AlumniDetailForm()

    return render(request, 'authentication/student_profile.html', {'form':form})


