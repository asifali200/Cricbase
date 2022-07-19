# Generated by Django 4.0.3 on 2022-06-01 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_remove_league_teams_remove_team_players_player_teams_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueTeams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaguename1', models.CharField(max_length=300)),
                ('leagueteams', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]
