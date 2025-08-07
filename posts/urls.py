from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('retweet/<int:pk>/', views.retweet_post, name='retweet_post'),
    path('search/', views.search_view, name='search'),
    path('hashtag/<str:hashtag_name>/', views.hashtag_view, name='hashtag'),
]
