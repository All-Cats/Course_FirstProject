from django.db import models


class RequestForm(models.Model):
    give_currency = models.CharField(max_length=255, verbose_name='Отдаёте при обмене')
    get_currency = models.CharField(max_length=255, verbose_name='Получаете при обмене')
    telegram = models.CharField(max_length=255, verbose_name='Телеграм')

    class Meta:
        verbose_name = 'Заявку с формы'
        verbose_name_plural = 'Заявки с формы'
