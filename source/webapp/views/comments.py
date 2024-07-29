from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from source.webapp.forms.comments import CommentForm
from source.webapp.models import task
from source.webapp.models.comment import Comment
from source.webapp.models.task import Task


class CreateCommentView(CreateView):
    template_name = "comments/create_comment.html"
    form_class = CommentForm

    def form_valid(self, form):
        article = get_object_or_404(Task, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.task = task
        comment.save()
        return redirect(article.get_absolute_url())


class UpdateCommentView(UpdateView):
    template_name = "comments/update_comment.html"
    form_class = CommentForm
    model = Comment

    def get_success_url(self):
        return reverse("webapp:task_detail", kwargs={"pk": self.object.task.pk})


class DeleteCommentView(DeleteView):
    queryset = Comment.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("webapp:task_detail", pk=self.object.article.pk)