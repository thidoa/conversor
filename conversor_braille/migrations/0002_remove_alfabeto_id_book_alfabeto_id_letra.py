# Generated by Django 4.0.6 on 2022-10-29 01:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conversor_braille', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alfabeto',
            name='id_book',
        ),
        migrations.AddField(
            model_name='alfabeto',
            name='id_letra',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
    ]