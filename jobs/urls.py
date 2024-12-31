from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"), #Dashboard Route Path
    path("job_list/", views.job_list, name="job_list"), #Job_list Route Path
    path("job/create/", views.job_create, name="job_create"), #Job_Create Route Path
    path("job/edit/<int:job_post_id>", views.job_edit, name="job_edit"), #Job_Edit Route Path
    path("job/delete/<int:job_post_id>", views.job_delete, name="job_delete"), #Job_Edit Route Path
]