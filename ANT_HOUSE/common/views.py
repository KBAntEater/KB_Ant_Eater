from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #폼의 입력값을 개별적으로 얻고 싶은 경우
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 user_id=request.POST['username'],
#                 user_pwd=request.POST['password1'],
#                 user_email=request.POST['email'],)
#             auth.login(request, user)
#             return redirect('/')
#         return render(request, 'signup.html')
#     return render(request, 'signup.html')

# def signup(request):
#     if request.method =='POST':
#         user_id = request.POST.get('username')
#         user_pwd = request.POST.get('password1')
#         user_email = request.POST.get('email')

#         user = User
#         user.user_id = user_id
#         user.user_pwd = user_pwd
#         user.user_email = user_email

#         user.save()
#         return render(request, 'signup.html')
#     return render(request, 'signup.html')
