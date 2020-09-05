# Generated by Django 2.2.12 on 2020-08-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0030_charactermarketorder_corporationmarketorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteraudit',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='characteraudit',
            name='cache_expire_skill_que',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='characteraudit',
            name='cache_expire_wallet',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='characteraudit',
            name='last_update_skill_que',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='characteraudit',
            name='last_update_wallet',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]