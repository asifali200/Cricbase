from email.policy import default
import django
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class User(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    email = models.EmailField('Email Address')

class News(models.Model):
    newsheading = models.CharField('newsheading',max_length=300,default='',null=True)
    created = models.DateTimeField('created',default=timezone.now)
    news = RichTextField('news',default='',null=True)
    tour = models.CharField('tour',max_length=300,default='',null=True)
    summary = models.CharField('summary',max_length=300,default='',null=True)
    News_pic = models.ImageField('News_pic',upload_to='chicks/',default='',null=True)
    #news = models.TextField('news',default='',null=True)
    
    class Meta:
      verbose_name_plural = "News"
    
    def __str__(self):
        return str(self.newsheading)

class Player(models.Model):
    Name = models.CharField('Name',max_length=300,default='',null=True)
    Country = models.CharField('Country',max_length=300,default='',null=True)
    Birthday = models.CharField('Birthday',max_length=300,default='',null=True)
    City = models.CharField('City',max_length=300,default='',null=True)
    Role = models.CharField('Role',max_length=300,default='',null=True)
    Batting_style = models.CharField('Batting_style',max_length=300,default='',null=True)
    Bowling_style = models.CharField('Bowling_style',max_length=300,default='',null=True)
    Teams = models.CharField('Team',max_length=300,default='',null=True)
    Test_Matches = models.CharField('Test_Matches',max_length=300,default='',null=True)
    Odi_Matches = models.CharField('Odi_Matches',max_length=300,default='',null=True)
    T20_Matches = models.CharField('T20_Matches',max_length=300,default='',null=True)
    Ipl_Matches = models.CharField('Ipl_Matches',max_length=300,default='',null=True)
    Test_Runs = models.CharField('Test_Runs',max_length=300,default='',null=True)
    Odi_Runs = models.CharField('Odi_Runs',max_length=300,default='',null=True)
    T20_Runs = models.CharField('T20_Runs',max_length=300,default='',null=True)
    Ipl_Runs = models.CharField('Ipl_Runs',max_length=300,default='',null=True)
    Test_50 = models.CharField('Test_50',max_length=300,default='',null=True)
    Odi_50 = models.CharField('Odi_50',max_length=300,default='',null=True)
    T20_50 = models.CharField('T20_50',max_length=300,default='',null=True)
    Ipl_50 = models.CharField('Ipl_50',max_length=300,default='',null=True)
    Test_100 = models.CharField('Test_100',max_length=300,default='',null=True)
    Odi_100 = models.CharField('Odi_100',max_length=300,default='',null=True)
    T20_100 = models.CharField('T20_100',max_length=300,default='',null=True)
    Ipl_100 = models.CharField('Ipl_100',max_length=300,default='',null=True)
    Test_Wickets = models.CharField('Test_Wickets',max_length=300,default='',null=True)
    Odi_Wickets = models.CharField('Odi_Wickets',max_length=300,default='',null=True)
    T20_Wickets = models.CharField('T20_Wickets',max_length=300,default='',null=True)
    Ipl_Wickets = models.CharField('Ipl_Wickets',max_length=300,default='',null=True)
    Test_5W = models.CharField('Test_5W',max_length=300,default='',null=True)
    Odi_5W = models.CharField('Odi_5W',max_length=300,default='',null=True)
    T20_5W = models.CharField('T20_5W',max_length=300,default='',null=True)
    Ipl_5W = models.CharField('Ipl_5W',max_length=300,default='',null=True)
    Test_10W = models.CharField('Test_10W',max_length=300,default='',null=True)
    Odi_10W = models.CharField('Odi_10W',max_length=300,default='',null=True)
    T20_10W = models.CharField('T20_10W',max_length=300,default='',null=True)
    Ipl_10W = models.CharField('Ipl_10W',max_length=300,default='',null=True)
    Para = RichTextField('Para',default='',null=True)
    Model_pic = models.ImageField('Model_pic',upload_to='chicks/',default='',null=True)

    class Meta:
      verbose_name_plural = "Players"
    
    def __str__(self):
        return str(self.Name)

class Comment(models.Model):
    post = models.ForeignKey(News,related_name='comments',on_delete=models.CASCADE)
    cname = models.CharField('CName',max_length=300,default='',null=True)
    box = models.TextField('Box',default='',null=True)
    cmted = models.DateTimeField(default=timezone.now)

    class Meta:
      verbose_name_plural = "Comments"

    def __str__(self):
        return '%s - %s' % (self.post.newsheading, self.cname)
    