from django.contrib import admin
from django.urls import path
from resources import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.resource_home, name='home'),
    
    path('create-secret-admin/', views.generate_live_admin),
]