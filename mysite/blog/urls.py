from django.contrib import admin
from django.urls import path
from mysite.blog.views.post_view import PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', PostView.as_view(), name='home'),
]