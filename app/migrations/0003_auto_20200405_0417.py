# Generated by Django 3.0.3 on 2020-04-04 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200404_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]