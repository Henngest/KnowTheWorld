# Generated by Django 4.1 on 2022-08-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_quizresults'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresults',
            name='result',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
