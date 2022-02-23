# Generated by Django 4.0.2 on 2022-02-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(verbose_name='First Name')),
                ('last_name', models.TextField(verbose_name='Last Name')),
                ('company_name', models.TextField(verbose_name='Company Name')),
                ('city', models.TextField(verbose_name='City')),
                ('state', models.TextField(verbose_name='State')),
                ('web', models.TextField(verbose_name='Website')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('zip', models.PositiveIntegerField(verbose_name='Zipcode')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Id')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
