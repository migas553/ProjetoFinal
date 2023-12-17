from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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


@login_required
def my_account(request):
    return render(request, 'UsersManagement/my_account.html')



@login_required
def edit_my_account(request):
    if request.method =='POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('my_account')
        
    return render(request, 'UsersManagement/edit_my_account.html')