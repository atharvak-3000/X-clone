from django import template
from django.conf import settings
import os

register = template.Library()

@register.filter
def avatar_url(user):
    """Return user avatar URL or default avatar URL if file doesn't exist"""
    if user.avatar and hasattr(user.avatar, 'url'):
        # Check if file exists
        avatar_path = os.path.join(settings.MEDIA_ROOT, str(user.avatar))
        if os.path.exists(avatar_path):
            return user.avatar.url
    
    # Return a default avatar URL (using a placeholder service)
    return f"https://ui-avatars.com/api/?name={user.get_full_name() or user.username}&background=1da1f2&color=fff&size=300"

@register.filter
def cover_url(user):
    """Return user cover photo URL or default if file doesn't exist"""
    if user.cover_photo and hasattr(user.cover_photo, 'url'):
        # Check if file exists
        cover_path = os.path.join(settings.MEDIA_ROOT, str(user.cover_photo))
        if os.path.exists(cover_path):
            return user.cover_photo.url
    
    # Return None for no cover photo
    return None
