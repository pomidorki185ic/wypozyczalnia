# Generated by Django 3.1.3 on 2020-12-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilKlienta', '0003_auto_20201201_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='nr_telefonu',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]