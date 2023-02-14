from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    path("", views.index, name="index"),
    path("meus_topicos/", views.topics, name="topics"),
    path("meus_topicos/<int:topic_id>/", views.topic, name="topic"),
    path("novo_topico/", views.create_topic, name="create_topic"),
    path("atualizar_topico/<int:topic_id>/", views.update_topic, name="update_topic"),
    path("excluir_topico/<int:topic_id>/", views.delete_topic, name="delete_topic"),
]
