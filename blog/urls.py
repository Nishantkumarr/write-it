
from django.urls import path , include
from . import views
from .views import PostListView , PostDeleteView,PostCreateView,PostDetailView,PostUpdateView,UserPostListView,TechPostListView

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('blog/',PostListView.as_view(),name='blog-name'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user-post'),
    path('blog/new/',PostCreateView.as_view(),name='blog-new'),
    path('blog/<int:pk>/',PostDetailView.as_view(),name='blog-detail'),
    path('blog/<str:tech>/',TechPostListView.as_view(),name='tech-post'),
    path('blog/<int:pk>/update/',PostUpdateView.as_view(),name='blog-update'),
    path('blog/<int:pk>/delete/',PostDeleteView.as_view(),name='blog-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='contact')

    
]
