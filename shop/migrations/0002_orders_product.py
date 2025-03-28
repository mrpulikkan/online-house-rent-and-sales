# Generated by Django 4.0.2 on 2022-06-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('booked', 'booked'), ('sold', 'sold')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(choices=[('rent', 'rent'), ('sale', 'sale')], max_length=50, null=True)),
                ('place', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(null=True)),
                ('owner', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
