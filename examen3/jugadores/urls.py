from django.urls import path

from jugadores import views


app_name = "jugadores"


urlpatterns = [
    path('create_jugador/', views.Createjugador.as_view(), name="create_jugador"),
    path('list_jugador/', views.Listjugador.as_view(), name="list_jugador"),
    path('detail_jugador/<int:pk>/', views.Detailjugador.as_view(), name="detail_jugador"),
    path('update_jugador/<int:pk>/', views.Updatejugador.as_view(), name="update_jugador"),
    path('delete_jugador/<int:pk>/', views.delete_jugador, name="delete_jugador"),
]

