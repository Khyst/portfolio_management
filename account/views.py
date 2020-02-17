from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import MyUser
from django.contrib import auth
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def login(request):
    if request.method == 'POST': #POST 요청
        username = request.POST['username']
        password = request.POST['password']

        #user 인증 실행
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            print(user, 'login 작업 실행')
            auth.login(request, user)
            return redirect('dashboard')
        else :
            print(user, '로그인 실패')
            return render(request, 'login.html', {'error' : '사용자 이름 혹은 패스워드가 일치하지 않습니다.'})

    else: #GET 요청
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = MyUser.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error' : '!! 사용자가 이미 존재 합니다. !!'})
            except MyUser.DoesNotExist:
                user = MyUser.objects.create_user(
                    request.POST['username'], request.POST['email'], request.POST['password1']
                )
                auth.login(request, user)
                return redirect('dashboard')
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다.'})            
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('dashboard')
    return render(request, 'signup.html')

def profile(request):
    if request.method == 'POST':
        user_obj = request.user

        """
        user_obj.username = request.POST.get('username')
        user_obj.email = request.POST.get('email')
        user_obj.first_name = request.POST['first_name']
        user_obj.last_name = request.POST.get('last_name')
        """

        user_obj.statue = request.POST['statue']
        user_obj.county = request.POST['county']
        user_obj.postcode = request.POST['postcode']
        user_obj.address = request.POST['address']

        user_obj.save()

    return render(request, 'profile.html')