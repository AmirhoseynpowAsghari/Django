# Generated by Django 4.2.5 on 2023-11-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_uservisit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservisit',
            name='last_visit',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
