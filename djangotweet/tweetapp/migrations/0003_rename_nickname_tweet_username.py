# Generated by Django 4.1.3 on 2024-08-09 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0002_alter_tweet_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='nickname',
            new_name='username',
        ),
    ]