from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    """
    Template: templates/members/login.html
        POST요청을 처리하는 form
        내부에는 input 2개를 가지며, 각각 username, password로 name을 가짐
    URL: /members/login/  (members.urls를 사용, config.urls에 include하여 사용)
            name: members:login (url namespace를 사용)
    POST요청시, 예제를 보고 적절히 로그인 처리한 후, index로 돌아갈 수 있도록 한다
    로그인에 실패하면 다시 로그인페이지로 이동
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:  # 유효한 사용자일 경우
            login(request, user)  # 사용자를 로그인 시킨다.
            return redirect('posts:post-list')
        else:  # 유효한 사용자가 아닐 경우
            return redirect('members:login')  # 로그인 페이지로 돌아온다
    else:
        return render(request, 'members/login.html')
