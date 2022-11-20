from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail



def reg(request):
    if request.method == 'GET':
        return render(request, 'account/reg.html')
    elif request.method == "POST":
        # 1. Зчитуємо із форми реєстраційні дані
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        # 2. Сценарій реєстрації
        report = dict()
        new_user = User.objects.create_user(login, email, pass1)
        if new_user is None:
            report['mess'] = 'У реєстрації відмовлено!'
        else:
            report['mess'] = 'Ви успішно зареєстровані!'
            # 3. Готуємо поштове повідомлення для підтвердження реєстрації
            url = f'http://localhost:8000/account/confirm?email={email}'
            subject = 'Підтвердження реєстрації на сайті Univer'
            body = f"""
                <hr />
                <h3>Для підтвердження реєстрації перейдіть за посиланням</h3>
                <h4>
                    <a href="{url}">{url}</a>
                </h4>
                <hr />
            """
            # 4.Відправляємо поштове повідомлення
            success = send_mail(subject, '', 'Site_Univer', [email], fail_silently=False, html_message=body)
            if not success:
                report['info'] = 'Ваша пошта не дійсна!'
            else:
                report['info'] = f"""
                На вказаний Вами при реєстрації E-mail {email} <br>
                відправлено повідомлення
            """
        # !. Завантажуємо звіт на сторінку результатів

        return render(request, 'account/reg_res.html', context=report)


def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html')
    elif request.method == "POST":
        # 1. Зчитуємо із форми авторізаційні дані
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')
        # 2. Сценарій авторизації
        report = dict()
        check_user = authenticate(request, username=_login, password=_pass1)
        if check_user is None:
            report['mess'] = 'Користувач не знайдений!'
        else:
            report['mess'] = 'Ви успішно авторизовані!'
            login(request, check_user)
            
        return render(request, 'account/entry_res.html', context=report)
    


def confirm(request):
    # Считуємо Email від якого прийшло підтверждення (з get параметра в def reg(request)
    # )
    email = request.GET.get('email')

    # Знаходимо користувача із отриманим email
    user = User.objects.filter(email=email)

    # Додаємо користувача до групи ConfirmedUser
    group = User.groups.filter(name="ConfirmedUser")
    User.groups.add(group)

    # Треба створити в адмінці таку групу
    return render(request, 'account/confirm.html')


def exit(request):
    logout(request)
    return redirect('/home')


def profile(request):
    return render(request, 'account/profile.html')


def reset(request):
    return render(request, 'account/reset.html')


