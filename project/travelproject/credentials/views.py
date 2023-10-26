from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register_person(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["password1"]
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is taken")
                return redirect('reg')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                return redirect('log')
        else:
            messages.info(request,"password is incorrect")
            return  redirect('reg')

        return redirect('datas')

    return render(request,'register_form.html')


def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not  None:
            auth.login(request,user)
            return redirect('datas')
        else:
            messages.info(request,'invalid credentials')
            return redirect('reg')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('datas')