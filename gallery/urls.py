from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="login.html"), name='logout'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('', views.gallery, name='gallery'),
    url(r'^filter/(?P<image_type>[\w-]+)/$', views.filtergalleryData, name='filtergalleryData'),
    ]
