from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='mysite-home'),
    path('about/', views.about, name='mysite-about'),
    path('blog/', views.blog, name='mysite-blog'),
    path('resources/', views.resources, name='mysite-resources'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]