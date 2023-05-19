from django.urls import path

from . import views

# app_name='web_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.reg, name='reg'),
    path('log', views.log, name='login'),
    path('logout/', views.logoutfrom, name='logout'),

]
