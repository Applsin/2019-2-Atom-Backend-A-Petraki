# Generated by Django 2.2.5 on 2019-10-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('attach_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=256)),
                ('message_id', models.ManyToManyField(to='chats.Message')),
                ('user_id', models.ManyToManyField(to='user_profile.User')),
            ],
        ),
    ]
