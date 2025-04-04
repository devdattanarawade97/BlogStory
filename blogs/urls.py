from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('', views.blog_list, name='blog_list'),
    path('blogs', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('category/<int:category_id>/', views.filter_by_category, name='filter_by_category'),
    path('like/<int:pk>/', views.like_blog, name='like_blog'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)