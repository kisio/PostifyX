from django.urls import path
from. views import (PostListView, 
PostDetailView,
PostCreateView,
PostUpdate,
PostDeleteview,
UserPostListView

)
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update',PostUpdate.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteview.as_view(), name='post-delete'),
    path('about/',views.about,name='blog-about'),
]
