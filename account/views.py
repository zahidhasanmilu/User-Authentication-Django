from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'post':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        confirm_password = request.POST['password2']
        # return render(request,'signup.html')
        if password1 == confirm_password:
            user = User.objects.create_user( username=username ,first_name=first_name,last_name = last_name, email=email,password=password1)
            user.save()
            # messages.success(request, 'Your account has been created successfully')
            return redirect('/') 
        else:
            return render(request, 'error.html')