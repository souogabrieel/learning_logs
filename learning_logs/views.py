from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from . import models, forms


def index(request):
    return render(request, "learning_logs/index.html")


def public_topics(request):
    topics = models.Topic.objects.filter(public=True)
    context = {"topics": topics, "public": True}
    return render(request, "learning_logs/topics.html", context)


def public_topic(request, topic_id):
    topic = get_object_or_404(models.Topic, id=topic_id, public=True)
    entries = topic.entries.all()
    context = {"topic": topic, "entries": entries, "public": True}
    return render(request, "learning_logs/topic.html", context)


@login_required
def topics(request):
    topics = models.Topic.objects.filter(owner=request.user)
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    topic = get_object_or_404(models.Topic, id=topic_id, owner=request.user)
    entries = topic.entries.all()
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def create_topic(request):
    if request.method != "POST":
        form = forms.TopicForm()
    else:
        form = forms.TopicForm(data=request.POST, user=request.user)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            messages.success(request, "Tópico criado com sucesso!")
            return redirect("learning_logs:topic", new_topic.id)

    context = {"form": form}
    return render(request, "learning_logs/create_topic.html", context)


@login_required
def update_topic(request, topic_id):
    topic = get_object_or_404(models.Topic, id=topic_id, owner=request.user)

    if request.method != "POST":
        form = forms.TopicForm(instance=topic)
    else:
        form = forms.TopicForm(
            instance=topic, data=request.POST, user=request.user, topic_id=topic_id
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Tópico atualizado com sucesso!")
            return redirect("learning_logs:topic", topic_id)

    context = {"form": form}
    return render(request, "learning_logs/update_topic.html", context)


@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(models.Topic, id=topic_id, owner=request.user)

    if request.method != "POST":
        raise Http404
    else:
        topic.delete()
        messages.success(request, "Tópico excluído com sucesso!")
        return redirect("learning_logs:topics")


@login_required
def create_entry(request, topic_id):
    topic = get_object_or_404(models.Topic, id=topic_id, owner=request.user)

    if request.method != "POST":
        form = forms.EntryForm()
    else:
        form = forms.EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            messages.success(request, "Registro criado com sucesso!")
            return redirect("learning_logs:topic", topic_id)

    context = {"form": form}
    return render(request, "learning_logs/create_entry.html", context)


@login_required
def update_entry(request, entry_id):
    entry = get_object_or_404(models.Entry, id=entry_id, topic__owner=request.user)

    if request.method != "POST":
        form = forms.EntryForm(instance=entry)
    else:
        form = forms.EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro atualizado com sucesso!")
            return redirect("learning_logs:topic", entry.topic.id)

    context = {"form": form}
    return render(request, "learning_logs/update_entry.html", context)


@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(models.Entry, id=entry_id, topic__owner=request.user)
    topic = entry.topic

    if request.method != "POST":
        raise Http404
    else:
        entry.delete()
        messages.success(request, "Registro excluído com sucesso!")
        return redirect("learning_logs:topic", topic.id)
