from django.contrib import admin

# Register your models here.
from newsBigdata.models import User, News, Interest, Scrap

admin.site.register(User)
admin.site.register(News)
admin.site.register(Interest)
admin.site.register(Scrap)