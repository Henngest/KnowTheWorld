# Generated by Django 4.1 on 2022-08-26 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'verbose_name_plural': 'subcategories',
            },
        ),
    ]