# Generated by Django 5.0.6 on 2024-07-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_borrow_due_date_borrow_fine_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(default='available', max_length=20),
        ),
    ]
