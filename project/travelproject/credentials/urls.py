from django.urls import path

from . import views

urlpatterns = [
    path('register/',views.register_person,name="reg"),
    path('login/', views.login, name="log"),
    path('logout/', views.logout, name="logout"),

]
