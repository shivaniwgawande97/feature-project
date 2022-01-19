# Generated by Django 2.2.6 on 2022-01-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('weight', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('created_at', models.CharField(blank=True, default='1', max_length=100, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
