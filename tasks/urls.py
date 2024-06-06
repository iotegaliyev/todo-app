from django.urls import path
from .views import TaskList, UserTaskList, TaskDetail, TaskComplete, TaskFilterByStatus

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('users/<int:userId>/tasks/', UserTaskList.as_view(), name='user-task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', TaskComplete.as_view(), name='task-complete'),
    path('tasks/status/', TaskFilterByStatus.as_view(), name='task-filter-status'),
]
