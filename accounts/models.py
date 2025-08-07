from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True)
    cover_photo = models.ImageField(upload_to='covers/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize avatar if it exists
        if self.avatar and hasattr(self.avatar, 'path'):
            try:
                img = Image.open(self.avatar.path)
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.avatar.path)
            except:
                pass

    @property
    def followers_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.following.count()

    def is_following(self, user):
        return self.following.filter(id=user.id).exists()

    def get_avatar_url(self):
        """Return user avatar URL or default avatar URL if file doesn't exist"""
        if self.avatar and hasattr(self.avatar, 'url'):
            try:
                # Try to access the URL - if file exists, this will work
                return self.avatar.url
            except:
                pass

        # Return a default avatar URL using a placeholder service
        name = self.get_full_name() or self.username
        return f"https://ui-avatars.com/api/?name={name}&background=1da1f2&color=fff&size=300"

    def get_cover_url(self):
        """Return user cover photo URL or None if file doesn't exist"""
        if self.cover_photo and hasattr(self.cover_photo, 'url'):
            try:
                return self.cover_photo.url
            except:
                pass
        return None
