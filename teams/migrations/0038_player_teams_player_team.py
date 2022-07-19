# Generated by Django 4.0.4 on 2022-06-06 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0037_remove_players_teamname_remove_teams_playername_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300, null=True, verbose_name='Name')),
                ('country', models.CharField(default='', max_length=300, null=True, verbose_name='Name')),
                ('city', models.CharField(default='', max_length=300, null=True, verbose_name='City')),
                ('para', models.TextField(default='', null=True, verbose_name='Para')),
                ('dob', models.CharField(default='', max_length=300, null=True, verbose_name='Dob')),
                ('mat', models.CharField(default='', max_length=300, null=True, verbose_name='Mat')),
                ('runs', models.CharField(default='', max_length=300, null=True, verbose_name='runs')),
                ('hs', models.CharField(default='', max_length=300, null=True, verbose_name='Hs')),
                ('hcen', models.CharField(default='', max_length=300, null=True, verbose_name='Hcen')),
                ('cen', models.CharField(default='', max_length=300, null=True, verbose_name='Cen')),
                ('wick', models.CharField(default='', max_length=300, null=True, verbose_name='Wick')),
                ('cts', models.CharField(default='', max_length=300, null=True, verbose_name='Cts')),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams', models.CharField(default='', max_length=300, null=True, verbose_name='Name')),
                ('players', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playername', to='teams.player')),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.teams'),
        ),
    ]
