# Generated by Django 4.0.6 on 2022-10-29 01:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_books_id_book_books_id_letra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='id_letra',
        ),
        migrations.AddField(
            model_name='books',
            name='id_book',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]