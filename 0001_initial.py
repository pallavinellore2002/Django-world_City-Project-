# Generated by Django 5.0.6 on 2024-07-13 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('countrycode', models.CharField(max_length=3)),
                ('district', models.CharField(max_length=255)),
                ('population', models.IntegerField()),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
    ]
