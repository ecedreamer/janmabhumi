# Generated by Django 5.1.2 on 2024-10-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('page_name', models.CharField(max_length=64)),
                ('page_slug', models.SlugField(max_length=128)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pages/')),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]