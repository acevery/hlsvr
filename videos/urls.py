from django.urls import path

from . import views

app_name = 'videos'
urlpatterns = [
    path('<int:video_id>/', views.video_detail, name='detail'),
    path('', views.video_list, name='list'),
]
