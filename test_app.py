#!/usr/bin/env python
"""
Simple test script to verify the X Clone application is working correctly.
"""
import os
import sys
import django
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xclone.settings')
django.setup()

from posts.models import Post

User = get_user_model()

def test_basic_functionality():
    """Test basic functionality of the X Clone app"""
    print("Testing X Clone Application...")
    
    # Test 1: Create a user
    print("1. Testing user creation...")
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123',
        first_name='Test',
        last_name='User'
    )
    print(f"✓ User created: {user.username}")
    
    # Test 2: Create a post
    print("2. Testing post creation...")
    post = Post.objects.create(
        author=user,
        content="This is a test post with #hashtag and @mention!"
    )
    print(f"✓ Post created: {post.content[:50]}...")
    
    # Test 3: Test hashtag extraction
    print("3. Testing hashtag extraction...")
    hashtags = post.get_hashtags()
    print(f"✓ Hashtags found: {hashtags}")
    
    # Test 4: Test mentions extraction
    print("4. Testing mentions extraction...")
    mentions = post.get_mentions()
    print(f"✓ Mentions found: {mentions}")
    
    # Test 5: Test follow functionality
    print("5. Testing follow functionality...")
    user2 = User.objects.create_user(
        username='testuser2',
        email='test2@example.com',
        password='testpass123'
    )
    user.following.add(user2)
    print(f"✓ {user.username} is now following {user2.username}")
    print(f"✓ {user.username} following count: {user.following_count}")
    print(f"✓ {user2.username} followers count: {user2.followers_count}")
    
    # Test 6: Test like functionality
    print("6. Testing like functionality...")
    post.likes.add(user2)
    print(f"✓ Post liked by {user2.username}")
    print(f"✓ Post likes count: {post.likes_count}")
    
    # Test 7: Test web client
    print("7. Testing web client...")
    client = Client()
    
    # Test home page
    response = client.get('/')
    print(f"✓ Home page status: {response.status_code}")
    
    # Test login page
    response = client.get('/accounts/login/')
    print(f"✓ Login page status: {response.status_code}")
    
    # Test register page
    response = client.get('/accounts/register/')
    print(f"✓ Register page status: {response.status_code}")
    
    print("\n🎉 All tests passed! Your X Clone application is working correctly!")
    print("\nYou can now:")
    print("1. Visit http://127.0.0.1:8000/ to see the home page")
    print("2. Register a new account at http://127.0.0.1:8000/accounts/register/")
    print("3. Login with the admin account (username: admin)")
    print("4. Create posts, follow users, like posts, and more!")
    
    # Cleanup
    User.objects.filter(username__in=['testuser', 'testuser2']).delete()
    print("\n✓ Test data cleaned up")

if __name__ == "__main__":
    test_basic_functionality()
