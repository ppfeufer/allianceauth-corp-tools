# Generated by Django 3.2.8 on 2022-01-09 01:42

from django.db import migrations


def migrate_notifications(apps, schema_editor):
    Notification = apps.get_model('corptools', 'Notification')
    NotificationText = apps.get_model('corptools', 'NotificationText')
    print("Starting Migration!")
    print("this will look like it has hung but it is doing bulk migration of data in the background")

    def get_missing_qs():
        existing_notes = NotificationText.objects.all().values('notification_id')
        return Notification.objects.all().values(
            'notification_id').exclude(
                notification_id__in=existing_notes).distinct()

    step = 50000
    note_cnt = get_missing_qs().count()

    while note_cnt > 0:
        n = get_missing_qs().values('notification_id',
                                    'notification_text')[:step]
        obs = []
        for i in n:
            obs.append(NotificationText(notification_id=i['notification_id'],
                                        notification_text=i['notification_text']))
        c = NotificationText.objects.bulk_create(
            obs, batch_size=20000, ignore_conflicts=True)

        print(f"Migrated {len(c)} of {note_cnt}")

        note_cnt = get_missing_qs().count()

    newids = NotificationText.objects.all().values('notification_id')
    cnt = Notification.objects.all().exclude(notification_id__in=newids).count()

    if cnt > 0:
        print(
            f"Notifications have not been migrated fully, {cnt} missing notifications, please run `manage.py migrate --fake corptools 0061_notificationtext` then retry migrations. If Problem persists please contact the developers")


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('corptools', '0061_notificationtext'),
    ]

    operations = [
        migrations.RunPython(migrate_notifications)
    ]
