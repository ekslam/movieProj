from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'prefMovie'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movies_id>/', views.movies_detail, name='detail'),
    path('add/',views.add_movie, name = 'add'),
    path('<int:movies_id>/update', views.update_movie, name='update'),
    path('register/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
] 