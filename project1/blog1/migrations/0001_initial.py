# Generated by Django 2.0.3 on 2019-03-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('pic', models.ImageField(blank=True, upload_to='mypicture')),
            ],
        ),
    ]