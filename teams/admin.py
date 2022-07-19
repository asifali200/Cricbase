from django.contrib import admin
from pandas import Series

from .models import User,News,Player,Comment

admin.site.register(User)
admin.site.register(News)
admin.site.register(Player)
admin.site.register(Comment)