# Generated by Django 4.1.10 on 2023-09-26 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_comments_userimage_comments_username_posts_userimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='likeUsername',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
