from django.contrib import admin

from .models import Cards


class CardsAdmin(admin.ModelAdmin):
    list_display = ('id','card', 'card_meaning')
    list_filter = ("card",)
    search_fields = ['card_meaning']
    #prepopulated_fields = {'slug': ('card',)}

admin.site.register(Cards, CardsAdmin)