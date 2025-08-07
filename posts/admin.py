from django.contrib import admin
from .models import Post, Hashtag, Notification

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_preview', 'created_at', 'likes_count', 'retweets_count')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')
    ordering = ('-created_at',)

    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'posts_count', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('recipient__username', 'sender__username')
    ordering = ('-created_at',)
