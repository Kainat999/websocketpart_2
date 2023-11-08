from django.contrib import admin
from .models import Chat, Group

@admin.register(Chat)

class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'timmestamp', 'group']


@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

