# Generated by Django 3.1.3 on 2020-11-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminstuff',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
