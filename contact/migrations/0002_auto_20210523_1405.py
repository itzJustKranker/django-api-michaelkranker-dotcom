# Generated by Django 3.2.3 on 2021-05-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='requestforproposal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
