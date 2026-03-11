from django.contrib import admin
from django.urls import path
from tasks.views import TasksListView,TasksCreateView,TasksUpdateView,TasksDeleteView,TasksCompleteView
from django.contrib.auth import views as auth_views
from accounts.views import SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TasksListView.as_view(), name="tasks_list"),
    path("create",TasksCreateView.as_view(), name="tasks_create"),
    path("update/<int:pk>", TasksUpdateView.as_view(), name="tasks_update"),
    path("delete/<int:pk>", TasksDeleteView.as_view(), name="tasks_delete"),
    path("complete/<int:pk>", TasksCompleteView.as_view(), name="tasks_complete"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
