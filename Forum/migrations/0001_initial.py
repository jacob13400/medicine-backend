# Generated by Django 2.2.4 on 2019-08-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=10)),
                ('user_id', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('post_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(default='Doctor', max_length=10)),
                ('user_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=127)),
                ('description', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=127)),
            ],
        ),
    ]
