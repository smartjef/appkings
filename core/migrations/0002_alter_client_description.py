# Generated by Django 5.0 on 2024-01-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.TextField(blank=True, help_text='include the features here', max_length=400, null=True),
        ),
    ]
