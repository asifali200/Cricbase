# Generated by Django 4.0.3 on 2022-06-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0048_rename_city_player_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Role',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='Role'),
        ),
    ]
