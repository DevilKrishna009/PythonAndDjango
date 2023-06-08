# Generated by Django 4.2.1 on 2023-06-08 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User_Assignment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('user_des', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_post_model', to='User_Assignment.usermodel')),
            ],
        ),
    ]
