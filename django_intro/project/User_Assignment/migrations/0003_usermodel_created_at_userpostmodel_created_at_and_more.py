# Generated by Django 4.2.1 on 2023-06-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Assignment', '0002_userpostmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userpostmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userpostmodel',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='user_post_likes', to='User_Assignment.usermodel'),
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
