# Generated by Django 5.1.2 on 2024-10-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_siteinfo_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slider_name', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='sliders/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
