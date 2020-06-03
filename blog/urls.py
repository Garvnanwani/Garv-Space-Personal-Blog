from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug>/', views.detail_blog_view, name='detail')
]
