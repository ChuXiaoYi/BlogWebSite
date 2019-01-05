# Generated by Django 2.1.1 on 2019-01-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190105_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='to_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.IntegerField(default=0, verbose_name='回复的哪条评论'),
        ),
        migrations.AddField(
            model_name='comment',
            name='root_to',
            field=models.IntegerField(default=0, verbose_name='评论的哪个文章'),
        ),
    ]
