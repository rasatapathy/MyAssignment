from django.urls import path
from . import views
urlpatterns = [
    path("getUser/", views.getUserData),
    path("addUser/", views.addUserData),
    path("getProject/", views.getProjectData),
    path("addProject/", views.addProjectData),
    path("getIssue/", views.getIssueData),
    path("addIssue", views.addIssueData),

]