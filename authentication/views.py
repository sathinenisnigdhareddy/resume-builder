from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError

# Create your views here.
def usersignup(request):
    if request.method=='GET': 
        return render(request,'signup.html',{'form':UserCreationForm()})
    else:

       # print(request.POST["username"],request.POST["password1"],request.POST["password2"])
        username=request.POST["username"]
        password=request.POST['password1']
        if(len(password)<8):
                return render(request,'signup.html',{'form':UserCreationForm,'error':"Password should be greter than or equal to 8"})
        if(request.POST["password1"]==request.POST["password2"]):
            try:
                user=User.objects.create_user(request.POST["username"],password=request.POST["password1"])
                user.save()
                login(request,user)
                return redirect("resume_fill")
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm(),'message':"Please choose differentUsername"})
        else:
            return render(request,'signup.html',{'form':UserCreationForm,'error':"Password does't match"})


def userlogin(req):
    if req.method=='GET':
        return render(req,'login.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(username=req.POST["username"],password=req.POST["password"])
        if user is None:
            return render(req,'login.html',{'form':AuthenticationForm(),'error':"Username/Password Incorrect"})
        else:
            login(req,user)
            return redirect('resume_fill')

def userlogout(req):
    logout(req)
    return redirect('userlogin')



