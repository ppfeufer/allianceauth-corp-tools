# Generated by Django 4.2.16 on 2025-03-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0117_starbase_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
