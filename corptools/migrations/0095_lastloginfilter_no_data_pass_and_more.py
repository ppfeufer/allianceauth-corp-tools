# Generated by Django 4.2.5 on 2023-10-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0094_lastloginfilter_characteraudit_last_known_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastloginfilter',
            name='no_data_pass',
            field=models.BooleanField(
                blank=True, default=False, help_text='If there is no data (No Valid Corp Token) for a characters account then should this filter automatically pass.'),
        ),
        migrations.AlterField(
            model_name='lastloginfilter',
            name='days_since_login',
            field=models.IntegerField(
                default=30, help_text="Days since last login of any Character in the accounts Main's Corporation to pass filter."),
        ),
    ]
