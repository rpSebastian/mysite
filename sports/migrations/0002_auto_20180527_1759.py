# Generated by Django 2.0.4 on 2018-05-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalscore',
            name='Score_Value',
            field=models.IntegerField(max_length=5),
        ),
    ]