from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/register/', views.HandleRegister),
    path('api/login/', views.HandleLogin),
    path('api/logout/', views.HandleLogout),
    path('api/list/', views.HandleList),
    path('api/view/', views.HandleView),
    path('api/average/', views.HandleAverage),
    path('api/rate/', views.HandleRate),
]
