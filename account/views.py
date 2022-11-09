from django.shortcuts import render


def reg(request):
    return render(request, 'account/reg.html')


def entry(request):
    return render(request, 'account/entry.html')


def confirm(request):
    return render(request, 'account/confirm.html')


def exit(request):
    return render(request, 'account/exit.html')


def profile(request):
    return render(request, 'account/profile.html')


def reset(request):
    return render(request, 'account/reset.html')


