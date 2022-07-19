import requests
from bs4 import BeautifulSoup
from asyncio import events
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
#from models import Post


from .models import News
from .models import Player



# Create your views here.
def home(request):    
    return render(request,'home.html',{})

def quiz(request):
    return render(request,'quiz.html', {})

def gallery(request):
    return render(request,'gallery.html', {})

def about(request):
    return render(request,'about.html', {})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'profile.html')

def newsheading(request):
    newsheading = News.objects.all()
    return render(request,'newsheading.html',{'newsheading': newsheading})

def news(request, news_id):
    news = News.objects.get(pk=news_id)
    return render(request,'news.html',{'news': news})

def test(request):
    try:
        html_text = requests.get('https://sports.ndtv.com/cricket/live-scores').text
        soup = BeautifulSoup(html_text, "html.parser")
        sect = soup.find_all('div', class_='sp-scr_wrp vevent')
        section = sect[0]
        description1 = section.find('span', class_='description').text #
        description = (description1[11:])
        location = section.find('span', class_='location').text #
        current = section.find('div', class_='scr_dt-red').text #
        status = section.find_all('div', class_="scr_dt-red")[1].text
        block = section.find_all('div', class_='scr_tm-wrp')
        team1_block = block[0]
        team1_name = team1_block.find('div', class_='scr_tm-nm').text
        team1_score = team1_block.find('div', class_='scr_tm-scr').text
        team2_block = block[1]
        team2_name = team2_block.find('div', class_='scr_tm-nm').text
        team2_score = team2_block.find('div', class_='scr_tm-scr').text
        return render(request, "test.html", {'description': description,'location':location ,'current':current,'status':status,'team1_name':team1_name,'team1_score':team1_score,'team2_name':team2_name,'team2_score':team2_score})

    except:
        return render(request,'test.html', {})

def upcoming(request):
    try:
        html_text = requests.get('https://sports.ndtv.com/cricket/schedules-fixtures').text
        soup = BeautifulSoup(html_text, "html.parser")
        sect = soup.find_all('div', class_='sp-scr_wrp vevent')
        for section in sect:
            description1 = section.find_all('span', class_='description').text
            description = (description1[7:])
            location = section.find_all('span', class_='location').text
            current = section.find_all('div', class_='scr_dt-red').text
        return render(request, "upcoming.html", {'description': description,'location':location ,'current':current})
    except:
        return render(request,'upcoming.html', {})


def team(request): #list_venues class name
    team = Player.objects.all() #Venue object name
    return render(request,'team.html',{'team': team}) #{'variable': value}

def player(request, player_id):
    player = Player.objects.get(pk=player_id)
    return render(request,'player.html',{'player': player})

def search(request):
    if request.method == "POST":
        searched = request.POST('searched',False)
        return render(request,'search.html',{'searched':searched})
    else:
        return render(request,'search.html',{})