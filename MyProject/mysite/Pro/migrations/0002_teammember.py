# Generated by Django 5.1 on 2024-08-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='team_images/')),
            ],
        ),
    ]