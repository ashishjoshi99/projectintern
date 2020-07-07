# Generated by Django 2.2 on 2020-07-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opp', '0002_userprofile_is_organisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=256, unique=True)),
                ('description', models.CharField(max_length=2500)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=32)),
            ],
        ),
    ]
