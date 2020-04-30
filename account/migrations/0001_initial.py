# Generated by Django 3.0.5 on 2020-04-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('password', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=400)),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('birth', models.CharField(max_length=20)),
                ('email_confirm', models.BooleanField()),
                ('text_confirm', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
