from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Hashtag, Notification
from .forms import PostForm
import re

User = get_user_model()

def home_view(request):
    if request.user.is_authenticated:
        # Show posts from followed users and own posts
        following_users = request.user.following.all()
        posts = Post.objects.filter(
            Q(author__in=following_users) | Q(author=request.user)
        ).select_related('author').prefetch_related('likes', 'retweets')
    else:
        # Show all posts for anonymous users
        posts = Post.objects.all().select_related('author').prefetch_related('likes', 'retweets')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = PostForm() if request.user.is_authenticated else None

    context = {
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'posts/home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            # Process hashtags
            hashtags = post.get_hashtags()
            for hashtag_text in hashtags:
                hashtag_name = hashtag_text[1:]  # Remove the # symbol
                hashtag, created = Hashtag.objects.get_or_create(name=hashtag_name)
                hashtag.posts.add(post)

            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    replies = post.replies.all().select_related('author')

    context = {
        'post': post,
        'replies': replies,
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
@require_POST
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

        # Create notification if not own post
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                sender=request.user,
                notification_type='like',
                post=post
            )

    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes_count
    })

@login_required
@require_POST
def retweet_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.retweets.all():
        post.retweets.remove(request.user)
        retweeted = False
    else:
        post.retweets.add(request.user)
        retweeted = True

        # Create notification if not own post
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                sender=request.user,
                notification_type='retweet',
                post=post
            )

    return JsonResponse({
        'retweeted': retweeted,
        'retweets_count': post.retweets_count
    })

def search_view(request):
    query = request.GET.get('q', '')
    posts = []
    users = []
    hashtags = []

    if query:
        # Search posts
        posts = Post.objects.filter(content__icontains=query).select_related('author')[:20]

        # Search users
        users = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )[:10]

        # Search hashtags
        if query.startswith('#'):
            hashtag_name = query[1:]
            hashtags = Hashtag.objects.filter(name__icontains=hashtag_name)[:10]

    context = {
        'query': query,
        'posts': posts,
        'users': users,
        'hashtags': hashtags,
    }
    return render(request, 'posts/search.html', context)

def hashtag_view(request, hashtag_name):
    hashtag = get_object_or_404(Hashtag, name=hashtag_name)
    posts = hashtag.posts.all().select_related('author')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'hashtag': hashtag,
        'page_obj': page_obj,
    }
    return render(request, 'posts/hashtag.html', context)
