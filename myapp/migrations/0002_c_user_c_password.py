# Generated by Django 5.0.6 on 2024-05-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_user',
            name='c_password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]