from django import forms
from django.core.exceptions import ValidationError

from . import models


class TopicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.topic_id = kwargs.pop("topic_id", None)
        super(TopicForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Topic
        fields = ["title", "public"]
        labels = {"title": "Título do tópico", "public": "Tópico público?"}

    def clean_title(self):
        title = self.cleaned_data.get("title")
        title_used = (
            models.Topic.objects.filter(title__iexact=title, owner=self.user)
            .exclude(id=self.topic_id)
            .exists()
        )

        if title_used:
            raise ValidationError("Você já possui um tópico com esse título!")

        return title


class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ["content"]
        labels = {"content": "O que você aprendeu?"}
