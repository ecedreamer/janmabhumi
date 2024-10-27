# Generated by Django 5.1.2 on 2024-10-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('service', models.CharField(max_length=64)),
                ('contact_person', models.CharField(max_length=64)),
                ('mobile_number', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('website', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
