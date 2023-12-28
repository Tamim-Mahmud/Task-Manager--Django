from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name="home"),
    
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.reg_user,name='register'),
    path('tasks/<int:pk>',views.task_view,name="tasks"),
    path('delete_task/<int:pk>',views.delete_task,name="delete_task"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)