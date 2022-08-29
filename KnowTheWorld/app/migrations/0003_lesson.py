# Generated by Django 4.1 on 2022-08-27 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_category_options_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.CharField(max_length=200)),
                ('lesson_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subcategory')),
            ],
        ),
    ]