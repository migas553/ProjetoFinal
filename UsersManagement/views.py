from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form=SignUpForm()
    return render(request, 'UsersManagement/signup.html', {'form' : form})

# Frontpage temporaria
def frontpage(request):    
    return render(request, 'UsersManagement/frontpage.html')