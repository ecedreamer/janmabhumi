# Generated by Django 5.1.2 on 2024-12-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_alter_culturalevent_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='culturalevent',
            name='event_slug',
            field=models.SlugField(default='doasdf', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='culturalevent',
            name='occurrence',
            field=models.CharField(blank=True, default='asdfasdf', max_length=64),
            preserve_default=False,
        ),
    ]