# Generated by Django 4.0.3 on 2022-06-05 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0030_delete_city_remove_events_manager_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(default='', max_length=300, null=True, verbose_name='teams1')),
                ('teaminfo', models.TextField(default='', null=True, verbose_name='teaminfo1')),
                ('name', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Name1')),
                ('country', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Country1')),
                ('city', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='City1')),
                ('teams', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Team1')),
                ('para', models.TextField(blank=True, default='', null=True, verbose_name='Para1')),
                ('dob', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Dob1')),
                ('mat', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Mat1')),
                ('runs', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='runs1')),
                ('hs', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Hs1')),
                ('hcen', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Hcen1')),
                ('cen', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Cen1')),
                ('wick', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Wick1')),
                ('cts', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Cts1')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300, null=True, verbose_name='Name2')),
                ('teaminfo', models.TextField(blank=True, default='', null=True, verbose_name='teaminfo2')),
                ('country', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Country2')),
                ('city', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='City2')),
                ('teams', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Team2')),
                ('para', models.TextField(blank=True, default='', null=True, verbose_name='Para2')),
                ('dob', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Dob2')),
                ('mat', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Mat2')),
                ('runs', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='runs2')),
                ('hs', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Hs2')),
                ('hcen', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Hcen2')),
                ('cen', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Cen2')),
                ('wick', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Wick2')),
                ('cts', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Cts2')),
                ('teamname', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.teams')),
            ],
        ),
        migrations.CreateModel(
            name='Playerinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teaminfo', models.TextField(blank=True, default='', null=True, verbose_name='teaminfo3')),
                ('country', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Country3')),
                ('city', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='City3')),
                ('teams', models.CharField(blank=True, max_length=300, null=True, verbose_name='Team3')),
                ('para', models.TextField(blank=True, default='', null=True, verbose_name='Para3')),
                ('dob', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Dob3')),
                ('mat', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Mat3')),
                ('runs', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='runs3')),
                ('hs', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Hs3')),
                ('hcen', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Hcen3')),
                ('cen', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Cen3')),
                ('wick', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Wick3')),
                ('cts', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Cts3')),
                ('name', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.players')),
                ('teamname', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.teams')),
            ],
        ),
    ]
