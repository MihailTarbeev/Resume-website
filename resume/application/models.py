from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(150)], verbose_name='Возраст')
    photo = models.ImageField(upload_to='photos/avatars/%Y/%m/%d/', verbose_name='Фотография')
    profession = models.CharField(max_length=150, verbose_name='Профессия')
    habitation = models.CharField(max_length=150, verbose_name='Место проживания')
    email = models.CharField(max_length=150, verbose_name='Почта')
    file_resume = models.FileField(upload_to='resume', blank=True)
    details = models.TextField(blank=True, verbose_name='Детали')

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'


class Education(models.Model):
    organization = models.CharField(max_length=150, verbose_name='Организация')
    profession = models.CharField(blank=True, max_length=150, verbose_name='Профессия')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(blank=True, verbose_name='Дата окончания', null=True)
    details = models.TextField(blank=True, verbose_name='Детали')
    sort_key = models.IntegerField(default=0, verbose_name='Приоритет сортировки')

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'
        ordering = ('sort_key', 'organization',)


class Experience(models.Model):
    company = models.CharField(max_length=150, verbose_name='Компания')
    post = models.CharField(blank=True, max_length=150, verbose_name='Должность')
    start_date = models.DateTimeField(verbose_name='Дата трудоустройства')
    end_date = models.DateTimeField(blank=True, verbose_name='Дата увольнения')
    details = models.TextField(blank=True, verbose_name='Детали')
    sort_key = models.IntegerField(default=0, verbose_name='Приоритет сортировки')

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'
        ordering = ('sort_key', 'company',)


class Skills(models.Model):
    name_skill = models.CharField(max_length=150, verbose_name='Навык')
    url = models.CharField(blank=True, max_length=250, verbose_name='Ссылка на проект')
    period = models.CharField(blank=True, max_length=150, verbose_name='Период')
    sort_key = models.IntegerField(default=0, verbose_name='Приоритет сортировки')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ('sort_key', 'name_skill',)


class PetProjects(models.Model):
    title = models.CharField(max_length=150, verbose_name='Имя проекта')
    type = models.CharField(max_length=150, verbose_name='Тип проекта')
    photo = models.ImageField(upload_to='photos/projects/%Y/%m/%d', verbose_name='Фотография')
    description = models.TextField(blank=True, verbose_name='Описание')
    url = models.CharField(max_length=250, verbose_name='Ссылка на проект')
    sort_key = models.IntegerField(default=0, verbose_name='Приоритет сортировки')

    class Meta:
        verbose_name = 'Пет-проект'
        verbose_name_plural = 'Пет-проекты'
        ordering = ('sort_key', 'title',)


class Certificates(models.Model):
    title = models.CharField(max_length=150, verbose_name='Имя сертификата')
    photo = models.ImageField(upload_to='photos/certificates/%Y/%m/%d', verbose_name='Фотография')
    sort_key = models.IntegerField(default=0, verbose_name='Приоритет сортировки')

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        ordering = ('sort_key', 'title',)


class SocialMedia(models.Model):
    title = models.CharField(max_length=150, verbose_name='Имя социальной сети')
    url = models.CharField(max_length=250, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'


class AddInformation(models.Model):
    content = models.TextField(max_length=550, verbose_name='Контент')
    sort_key = models.IntegerField(default=0, verbose_name='Приоритет сортировки')

    class Meta:
        verbose_name = 'Доп. информация'
        verbose_name_plural = 'Доп. информация'
        ordering = ('sort_key', 'content',)
