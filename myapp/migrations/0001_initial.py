# Generated by Django 4.2.6 on 2023-11-22 14:04

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FoundItemDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('item_name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('location_found', models.CharField(blank=True, max_length=100)),
                ('datetime', models.DateTimeField(blank=True)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to=myapp.models.filepath)),
            ],
            options={
                'db_table': 'found_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LostItemDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('item_name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('location_lost', models.CharField(blank=True, max_length=100)),
                ('datetime', models.DateTimeField(blank=True)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to=myapp.models.filepath)),
            ],
            options={
                'db_table': 'lost_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=30, null=True)),
                ('subject', models.CharField(max_length=100)),
                ('issue', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'ticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
