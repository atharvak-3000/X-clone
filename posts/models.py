from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import re

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=280)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    retweets = models.ManyToManyField(User, related_name='retweeted_posts', blank=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}..."

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def retweets_count(self):
        return self.retweets.count()

    @property
    def replies_count(self):
        return self.replies.count()

    def get_hashtags(self):
        """Extract hashtags from post content"""
        hashtag_pattern = r'#\w+'
        return re.findall(hashtag_pattern, self.content)

    def get_mentions(self):
        """Extract mentions from post content"""
        mention_pattern = r'@\w+'
        return re.findall(mention_pattern, self.content)


class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    posts = models.ManyToManyField(Post, related_name='hashtags', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.name}"

    @property
    def posts_count(self):
        return self.posts.count()


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('like', 'Like'),
        ('retweet', 'Retweet'),
        ('follow', 'Follow'),
        ('mention', 'Mention'),
        ('reply', 'Reply'),
    )

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sender.username} {self.notification_type} - {self.recipient.username}"
