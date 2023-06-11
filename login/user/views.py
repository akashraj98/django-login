from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as djangologin
from django.contrib.auth import logout


# Create your views here.

def home(request):
    context = {
        'msg': request.user.username
    }
    return render(request,'home.html',context)

def login(request):
    return render(request,'login.html')
class SignUp(View):
    def get(self,request):
        if not request.user.is_anonymous:
            return render(request,'home.html')
        return render(request,'signup.html')
    
    def post(self, request):
        request_data = request.POST
        nickname = request_data.get('nick_name')
        password = request_data.get('password')
        if not(nickname or password):
            return redirect('signup')
        try:
            if User.objects.filter(username = nickname).first():
                # messages.error(request, "This username is already taken")
                return redirect('login')
            usr = User.objects.create_user(username=nickname,password=password)
            usr.save()
            djangologin(request, usr)
            return render(request,'home.html',{'msg':usr.username})
        except Exception as e:
            print("something went wrong",e)
            return redirect('signup')

class LoginUser(View):
    def get(self,request):
        if not request.user.is_anonymous:
            return redirect('user_home')

        return render(request,'login.html')
    
    def post(self,request):
        request_data = request.POST
        nickname = request_data.get('nick_name')
        password = request_data.get('password')
        if not(nickname or password):
            return redirect('login')
        user = authenticate(username=nickname,password=password)
        if user:
            djangologin(request, user)
            return redirect('user_home')
        else:
            return redirect('login')

class SignoutUser(View):
    def get(self,request):
        logout(request)
        return redirect('login')
