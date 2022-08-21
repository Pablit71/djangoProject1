from django.contrib import admin

# Register your models h
from ads.models import Ads, Location, Category, User

admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(User)
