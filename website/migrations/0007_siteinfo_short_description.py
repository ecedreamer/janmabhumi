# Generated by Django 5.1.2 on 2024-10-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_siteinfo_ward_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='short_description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
