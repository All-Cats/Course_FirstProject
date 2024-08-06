from django.shortcuts import render, redirect
from .models import RequestForm
from .forms import FormWithCaptcha


def index(request):
    captcha_form = FormWithCaptcha()
    if request.method == "POST":
        captcha_form = FormWithCaptcha(request.POST)
        if captcha_form.is_valid():
            RequestForm.objects.create(
                give_currency=request.POST['give_currency'],
                get_currency=request.POST['get_currency'],
                telegram=request.POST['telegram_login']
            )
            return redirect('index')
    return render(request, "blog/index.html", context={
        "captcha_form": captcha_form
    })
