from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    return render(request,'home.html')

class SignUp(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self, request):
        request_data = request.POST
        nickname = request_data.get('nick_name')
        password = request_data.get('password')
        if not(nickname or password):
            return redirect('signup')
        try:
            usr = User.objects.create_user(username=nickname,password=password)
            usr.save()
            return redirect('login')
        except Exception as e:
            print("something went wrong",e)
            return redirect('signup')

class LoginUser(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        request_data = request.POST
        nickname = request_data.get('nick_name')
        password = request_data.get('password')
        if not(nickname or password):
            return redirect('login')
        user = authenticate(username=nickname,password=password)
        if user is not None:
            return render(request,'home.html')
        else:
            return redirect('login')
