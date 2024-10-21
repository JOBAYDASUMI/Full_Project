from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        user_type=request.POST.get("user_type")
        username=request.POST.get("username")
        email=request.POST.get("email")
        age=request.POST.get("age")
        contact_no=request.POST.get("contact_no")
        Profile_Pic=request.FILES.get("Profile_Pic")
        gender_type=request.POST.get("gender_type")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                user_type=user_type,
                username=username,
                email=email,
                Age=age,
                Contact_No=contact_no,
                profile_pic=Profile_Pic,
                Gender=gender_type,
                password=password,      
            )
            
            if user_type=='viewers':
                viewersProfileModel.objects.create(user=user)
                
            elif user_type=='blogers':
                bologerProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")
