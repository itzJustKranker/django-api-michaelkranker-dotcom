# Generated by Django 3.1.3 on 2020-11-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequestForProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=250)),
                ('company_overview', models.TextField()),
                ('project_overview', models.TextField()),
                ('goals_objectives', models.TextField()),
                ('relationship', models.IntegerField(choices=[(0, 'Project Based'), (1, 'Maintenance'), (2, 'Retainer')], default=0)),
                ('problem', models.TextField()),
                ('site_type', models.IntegerField(choices=[(0, 'Dynamic'), (1, 'Static'), (2, 'N A')], default=0)),
                ('website_url', models.CharField(max_length=250)),
                ('budget', models.CharField(max_length=250)),
                ('timeline', models.IntegerField(choices=[(0, 'One Three'), (1, 'Three Six'), (2, 'Six Plus')], default=0)),
                ('referral', models.TextField()),
                ('comments', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
