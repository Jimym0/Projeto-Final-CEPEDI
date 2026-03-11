from .models import Tasks
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class TasksListView(LoginRequiredMixin, ListView):
    model = Tasks

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)

class TasksCreateView(LoginRequiredMixin,CreateView):
    model = Tasks
    fields = ["title","deadline"]
    success_url = reverse_lazy("tasks_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TasksUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ["title","deadline"]
    success_url = reverse_lazy("tasks_list")

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)        

class TasksDeleteView(LoginRequiredMixin, DeleteView):
    model = Tasks
    success_url = reverse_lazy("tasks_list")    

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user) 

class TasksCompleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        task.mark_as_complete()
        return redirect("tasks_list")

