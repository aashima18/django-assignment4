from django.urls import path
from django.conf.urls import url
from .import views
from .views import *

urlpatterns=[
    path('indexx',views.indexx,name='indexx'),
    path('', views.signup, name='signup'),
    path('update_profile/<int:id>/', views.update_profile, name='update_profile'),
    path('clientlist/', views.clientlist, name='clientlist'),
    path('get_user_profile/<int:id>/', views.get_user_profile, name='get_user_profile'),
    path('search2/', views.get_queryset, name='search2_results'),

]