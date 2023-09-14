from django.contrib import admin
from django.urls import path
from todoapp import views
app_name='todoapp'
urlpatterns = [
       path('', views.add, name='add'),
       path('delete/<int:taskid>/',views.delete_view,name='delete'),
       path('update/<int:id>/', views.update, name='update'),
       path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
       path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name='cbvdeatil'),
       path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name='cbvupdate'),
       path('cbvdelete/<int:pk>/',views.taskdeleteview.as_view(),name='cbvdelete'),

]