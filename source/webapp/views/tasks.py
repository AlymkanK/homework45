from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from source.webapp.forms.search_form import SearchForm
from source.webapp.forms.tasks import TaskForm
from source.webapp.models.task import Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"
    ordering = ['-created_at']
    context_object_name = "tasks"
    paginate_by = 5

    # paginate_orphans = 2

    def dispatch(self, request, *args, **kwargs):
        print(request.user.is_authenticated, "is_authenticated")
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__contains=self.search_value) | Q(author__contains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = "tasks/create_task.html"
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailView(DetailView):
    template_name = "tasks/task_detail.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.order_by("-created_at")
        return context


class UpdateTaskView(UpdateView):
    template_name = "tasks/update_task.html"
    form_class = TaskForm
    model = Task
    permission_required = 'webapp/change_task'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

class DeleteTaskView(DeleteView):
    template_name = "tasks/delete_task.html"
    model = Task
    success_url = reverse_lazy("webapp:tasks")
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author
