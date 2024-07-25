from django.urls import path
from django.views.generic import RedirectView

from source.webapp.views.comments import CreateCommentView, UpdateCommentView, DeleteCommentView
from source.webapp.views.tasks import TaskListView, CreateTaskView, TaskDetailView, UpdateTaskView, DeleteTaskView

app_name = 'webapp'

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('', RedirectView.as_view(pattern_name='webapp:tasks')),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_article'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_article'),
    path('task/<int:pk>/comment/create/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/update/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]