from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3(action='login'))
