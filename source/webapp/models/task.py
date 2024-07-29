from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from base_model import BaseModel

statuses = [("new", "Новая"), ("moderated", "Модерированная"), ("deleted", "Удаленная")]


class Task(BaseModel):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    content = models.TextField(null=False, blank=False, verbose_name="Контент")
    status = models.CharField(max_length=20, choices=statuses, verbose_name="Статус", default=statuses[0][0])

    author = models.ForeignField(
        get_user_model(),
        related_name="tasks",
        on_delete=models.SET_DEFAULT,
        default = 1
    )

    tags = models.ManyToManyField(
        "webapp.Tag",
        related_name="tasks",
        verbose_name="Теги",
        blank=True,
        through='webapp.TaskTag',
        through_fields=("task", "tag"),
    )

    def get_absolute_url(self):
        return reverse("webapp:task_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.pk}. {self.title}: {self.author}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        permissions = [('change_task', 'менять статус задаче')]