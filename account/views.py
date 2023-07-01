from django.shortcuts import render,redirect
from account.models import AccountModel,ContactModel
from BlogApp.models import CategoryModel
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.http import Http404

def checkpassword(newpassword1):
    if len(newpassword1)>=8:
        return True
    return False


def check_validation(newpassword2):
    has_digit, has_alpha, has_upper_case = False, False

    for i in newpassword2:
        if i.isdigit():
            has_digit =  True
        elif i.isalpha():
            has_alpha = True
        elif i.isalpha() and i.isupper():
            has_upper_case = True
    return has_digit and has_alpha and has_upper_case

class SignupView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"signup.html")
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        newpassword1 = request.POST.get("newpassword1")
        newpassword2 = request.POST.get("newpassword2")

        if not User.objects.filter(username=username).exists():
            if  newpassword1 != newpassword2:
                messages.info(request, "There is a password mismatch")
            elif not checkpassword(newpassword1):
                messages.info(request,"Password must be at least 8 symbols")
            elif not check_validation(newpassword1):
                messages.info(request,"Password must contain both characters and numbers")
            else:
                User.objects.create_user(
                    username=username,
                    newpassword1=newpassword1,
                    newpassword2 = newpassword2
                )
                user = authenticate(request, username = username, newpassword1 = newpassword1)
                if user is not None:
                    login(request,user)
                    messages.success(request, "You logged in")
                    return redirect ("home")
        else:
            messages.info(request, "Username has been taken")
            return redirect("signup")
        
#-----------------------------------------------------------------------------------------------------
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        newpassword1 = request.POST.get("newpassword1")

        user = authenticate(request, username = username, newpassword1 = newpassword1)
        if user is not None:
            login(request,user)
            messages.success(request, "You logged in")
            return redirect("home")
        else:
            if not User.objects.filter(username = username).exists():
                messages.info(request,"Please enter correct username")
            else:
                messages.info(request, "Please enter correct password")
            return redirect("login")
#-----------------------------------------------------------------------------------------
def logoutUser(request):
    logout(request)
    return redirect("login")
#------------------------------------------------------------------------------------------
class ChangepasswordView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'changepassword.html')
    
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            raise Http404
        username = request.POST.get("username")
        newpassword1 = request.POST.get("newpassword1")
        newpassword2 = request.POST.get("newpassword2")
        user = User.objects.get(username=username)

        if newpassword1 == newpassword2:
            user.set_password(newpassword1)
            user.save()
            messages.success(request,"Password changed")

        return redirect("login")
#-----------------------------------------------------------------------------------------------------
class ContactView(View):
    def get(self,request,*args,**kwargs):
        categories = CategoryModel.objects.all()

        context = {
            "categories" : categories
        }

        return render(request,"contact.html",context)
    
    def post(self,request,*args,**kwargs):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactModel.objects.create(
            name = name,
            surname = surname,
            telephone = telephone,
            email = email,
            message = message
        )

        messages.success(request,"Message sent")

        return redirect("contact")
        
        

