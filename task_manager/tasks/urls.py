from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.reg_user,name='register'),
    path('tasks/<int:pk>',views.task_view,name="tasks"),
    path('delete_task/<int:pk>',views.delete_task,name="delete_task"),
    path('update_task/<int:pk>',views.update_task,name="update_task"),
    path('add_task',views.add_task,name="add_task"),
    path('mark_complete<int:pk>',views.mark_complete,name="mark_complete"),
    path('search_by_name', views.search_by_name, name='search_by_name'),
    path('sort_by_due_date', views.sort_by_due_date, name='sort_by_due_date'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)