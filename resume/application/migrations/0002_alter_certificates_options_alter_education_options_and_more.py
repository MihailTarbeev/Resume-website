# Generated by Django 4.2.5 on 2023-09-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificates',
            options={'ordering': ('sort_key', 'title'), 'verbose_name': 'Сертификат', 'verbose_name_plural': 'Сертификаты'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('sort_key', 'organization'), 'verbose_name': 'Образование', 'verbose_name_plural': 'Образование'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ('sort_key', 'company'), 'verbose_name': 'Опыт', 'verbose_name_plural': 'Опыт'},
        ),
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Информация', 'verbose_name_plural': 'Информация'},
        ),
        migrations.AlterModelOptions(
            name='petprojects',
            options={'ordering': ('sort_key', 'title'), 'verbose_name': 'Пет-проект', 'verbose_name_plural': 'Пет-проекты'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'ordering': ('sort_key', 'name_skill'), 'verbose_name': 'Навык', 'verbose_name_plural': 'Навыки'},
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Медиа', 'verbose_name_plural': 'Медиа'},
        ),
        migrations.AddField(
            model_name='education',
            name='profession',
            field=models.CharField(default=1, max_length=150, verbose_name='Профессия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='info',
            name='photo',
            field=models.ImageField(upload_to='photos/avatars/%Y/%m/%d/', verbose_name='Фотография'),
        ),
    ]