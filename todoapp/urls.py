from django.urls import path, re_path
from . import views

urlpatterns = [
   
    path('create/',views.create,name='create'),
    path('create_project/',views.create_project,name='create_project'),
    re_path(r'^home/(?P<pk>[0-9a-f-]+)/$', views.home, name='home'),
    path('addTask/<str:project_id>/', views.addTask, name='addTask'),
    path('mark_as_done/<str:desc_id>/',views.mark_as_done,name='mark_as_done'),
    path('mark_as_undone/<str:desc_id>/',views.mark_as_undone,name='mark_as_undone'),
    path('delete_task/<str:desc_id>/',views.delete_task,name='delete_task'),
    path('edit_task/<str:desc_id>/',views.edit_task,name='edit_task'),
    path('project_detail/<str:prj_id>/',views.project_detail,name='project_detail'),
    path('edit_project/<str:prj_id>/',views.edit_project,name='edit_project'),
    
]
    


