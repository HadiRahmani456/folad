from django.contrib import admin
from .models import Post, Slid, Messenger_chat, Video


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish', 'status')
    list_filter = ('status', 'publish', 'created')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)


@admin.register(Slid)
class SlidAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')


@admin.register(Messenger_chat)
class MessengerChatAdmin(admin.ModelAdmin):
    list_display = ('url', 'type')


@admin.register(Video)
class VideoAdmin(PostAdmin):
    pass