from django.urls import path
from posts.views import HomeBlog, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

app_name = 'posts'
urlpatterns = [
    path('', HomeBlog.as_view(), name='home'),
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='detail'),
    path('edite/<str:slug>/', BlogPostUpdate.as_view(), name='edite'),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name='delete'),
]