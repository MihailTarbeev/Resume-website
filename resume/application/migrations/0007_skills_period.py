# Generated by Django 4.2.5 on 2023-09-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_addinformation_info_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='period',
            field=models.CharField(blank=True, max_length=150, verbose_name='Период'),
        ),
    ]