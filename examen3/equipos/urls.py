from django.urls import path

from equipos import views


app_name = "equipos"


urlpatterns = [
    path('create_equipo/', views.CreateEquipo.as_view(), name="create_equipo"),
    path('', views.index, name="index"),
    path('list_equipo/', views.ListEquipo.as_view(), name="list_equipo"),
    path('detail_equipo/<int:pk>/', views.DetailEquipo.as_view(), name="detail_equipo"),
    path('update_equipo/<int:pk>/', views.UpdateEquipo.as_view(), name="update_equipo"),
    path('delete_equipo/<int:pk>/', views.delete_equipo, name="delete_equipo"),
]

