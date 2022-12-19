from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Task

class login(LoginView):
    template_name = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pendings')

class pendingList(ListView):
    model = Task
    context_object_name = 'tasks'

class DetailTask(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('pendings')

class EditTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('pendings')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('pendings')