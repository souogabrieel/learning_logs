from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    path("", views.index, name="index"),
    path("topicos_publicos/", views.public_topics, name="public_topics"),
    path("topicos_publicos/<int:topic_id>/", views.public_topic, name="public_topic"),
    path("meus_topicos/", views.topics, name="topics"),
    path("meus_topicos/<int:topic_id>/", views.topic, name="topic"),
    path("novo_topico/", views.create_topic, name="create_topic"),
    path("atualizar_topico/<int:topic_id>/", views.update_topic, name="update_topic"),
    path("excluir_topico/<int:topic_id>/", views.delete_topic, name="delete_topic"),
    path("novo_topico/", views.create_topic, name="create_topic"),
    path("atualizar_topico/<int:topic_id>/", views.update_topic, name="update_topic"),
    path("excluir_topico/<int:topic_id>/", views.delete_topic, name="delete_topic"),
    path("copiar_topico/<int:topic_id>/", views.copy_topic, name="copy_topic"),
    path("novo_registro/<int:topic_id>/", views.create_entry, name="create_entry"),
    path("atualizar_registro/<int:entry_id>/", views.update_entry, name="update_entry"),
    path("excluir_registro/<int:entry_id>/", views.delete_entry, name="delete_entry"),
]
