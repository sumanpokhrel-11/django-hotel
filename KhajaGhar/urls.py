from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("subscribe", views.subscribe, name='subscribe'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name= 'logout' ),
    path('', include('allauth.urls'))

]

