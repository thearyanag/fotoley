# Generated by Django 4.1.2 on 2022-10-06 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fotoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, upload_to='media/')),
                ('caption', models.CharField(blank=True, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
