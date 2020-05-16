from django.shortcuts import render
from django.http import JsonResponse
from django_redis import get_redis_connection

from user.forms.account import LoginForm, RegisterForm, SendSmSForm


# def register(request):
#     return render(request, 'user/register1.html')


def login(request):
    """短信登录"""
    if request.method == 'GET':
        login_form = LoginForm()
        # captcha = CaptchaForm()

        # return render(request, 'login.html', {'form': login_form, 'capt': captcha})
        return render(request, 'user/login.html', {'form': login_form})

    if request.method == 'POST':
        """表单提交"""
        login_form = LoginForm(request.POST)
        # capt = CaptchaForm(request.POST)
        capt = None

        if not capt.is_valid():
            return JsonResponse({'status': False, 'error': capt.errors})

        if not login_form.is_valid():
            return JsonResponse({'status': False, 'error': login_form.errors})

        # 在forms中直接写了返回用户模型对象
        user_object = login_form.cleaned_data['mobile_phpne']

        request.session['user_id'] = user_object.id
        request.session.set_expiry(60 * 60 * 24 * 14)

        return JsonResponse({'status': True, 'data': '/web/index'})


def register(request):
    """用户注册"""
    if request.method == 'GET':
        # 显示
        return render(request, 'user/register.html')

    elif request.method == 'POST':
        # 处理提交
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return JsonResponse({'status': False, 'error': form.errors[0]})
        user = form.save()
        conn = get_redis_connection()
        conn.delete(user.mobile_phpne)

        request.session['user_id'] = user.id
        request.session.set_expiry(60*60*24*14)

        return JsonResponse({'status': True, 'data': 'loginsms'})


def send_sms(request):
    """发送验证码"""
    form = SendSmSForm(request, data=request.GET)
    if form.is_valid():
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})