from django.contrib import admin
from django.urls import path
from announcements import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('announcements/', views.announcement_list, name="announcement_list"),
    path('announcements/<int:id>/', views.announcement_detail, name="announcement_detail"),
]
