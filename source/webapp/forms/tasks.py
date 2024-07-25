from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from source.webapp.models.task import Task


def title_validate(title):
    if len(title) < 5:
        raise ValidationError("error")


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, label="Название", validators=[title_validate])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            if not isinstance(v.field.widget, widgets.CheckboxSelectMultiple):
                v.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Task
        fields = ("title", "content", "author", "tags")
        widgets = {"tags": widgets.CheckboxSelectMultiple()}