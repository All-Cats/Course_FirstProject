from django.shortcuts import render, redirect
from .models import RequestForm


def index(request):
    if request.method == "POST":
        RequestForm.objects.create(
            give_currency=request.POST['give_currency'],
            get_currency=request.POST['get_currency'],
            telegram=request.POST['telegram_login']
        )
        return redirect('index')

    return render(request, "blog/index.html")
