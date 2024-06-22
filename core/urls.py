from django.urls import path
from .views import update_task_status

urlpatterns = [
  path('task/satus/<int:task_id>', update_task_status, name="update_task_status" )
]