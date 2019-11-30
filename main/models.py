from django.db import models

# Create your models here.

LOT_TYPES = (
    (1, 'Пластик'),
    (2, 'Бумага'),
    (3, 'Железо'),
    (4, 'Техника'),
    (5, 'Батарейки'),
    (6, 'Мебель'),
    (7, 'Иное'),
)

class Zhilishniki(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назнавание")

    class Meta:
        verbose_name = "Жилищник"
        verbose_name_plural = "Жилищники"

    def __str__(self):
        return self.name


class UserLow(models.Model):
    fio = models.CharField(max_length=200, verbose_name="ФИО")
    phone = models.CharField(max_length=200, verbose_name="Телефон")
    zh_id = models.ForeignKey(Zhilishniki, models.CASCADE, verbose_name="Жилищник", related_name="zhilishnik_users")

    class Meta:
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"

    def __str__(self):
        return self.fio


class UserBussines(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    phone = models.CharField(max_length=200, verbose_name="Почта")

    class Meta:
        verbose_name = "Бизнес"
        verbose_name_plural = "Бизнесы"

    def __str__(self):
        return self.name


class Request(models.Model):
    bussines = models.ForeignKey(UserBussines, models.CASCADE, null=True, blank=True, verbose_name="Бизнес",
                                 related_name="bussines_requests")
    lot_type = models.PositiveSmallIntegerField(verbose_name='Тип мусора', default=7, choices=LOT_TYPES)
    took_away = models.BooleanField('Забрали', default=False)
    weight_need = models.IntegerField('Вес', default=0)
    datetime_send = models.DateTimeField('Дата когда забрали', null=True, blank=True)
    datetime_money_back_1 = models.DateTimeField('Дата получения денег жилищниками', null=True, blank=True)
    datetime_money_back_2 = models.DateTimeField('Дата получения денег людьми', null=True, blank=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return '{} - {}'.format(self.pk, self.get_lot_type_display())


class Trichcode(models.Model):
    code = models.CharField(max_length=200, verbose_name="Код")
    user_low = models.ForeignKey(UserLow, models.CASCADE, null=True, blank=True, verbose_name="Пользователь", related_name="user_trichcodes")
    request = models.ForeignKey(Request, models.CASCADE, null=True, blank=True, verbose_name="Заявка", related_name="request_trches")
    accessed = models.BooleanField(default=False, verbose_name='Обработан')
    lot_type = models.PositiveSmallIntegerField(verbose_name='Тип мусора', default=7, choices=LOT_TYPES)
    weight = models.IntegerField('Вес', default=0)

    class Meta:
        verbose_name = "Штрихкод"
        verbose_name_plural = "Штрихкоды"

    def __str__(self):
        return '{}'.format(self.code)