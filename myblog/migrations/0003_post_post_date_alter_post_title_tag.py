# Generated by Django 4.1.1 on 2022-09-14 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]
