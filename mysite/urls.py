from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/login/', admin.site.urls),
    path('', include('ratingapp.urls')),

]
