from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TaskList.as_view(), name="task_list"),
    path('<int:pk>/', TaskDetail.as_view(), name="task_detail"),
    path('category/', CategoryList.as_view(), name="category_list"),
    path('category_detail/<int:pk>/', CategoryDetail.as_view(), name="category_detail"),
    path('addTask/', add_task, name="add_task"),
    path('', home, name="home"),
    path('addCategory/', add_category, name="add_category"),
    
]