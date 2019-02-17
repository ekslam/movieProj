from django.urls import path

from . import views

app_name = 'prefMovie'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movies_id>/', views.movies_detail, name='detail'),
    path('add/',views.add_movie, name = 'add'),
    path('<int:movies_id>/update', views.update_movie, name='update'),
]