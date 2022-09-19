from django.urls import path

from estadios import views


app_name = "estadios"


urlpatterns = [
    path('create_estadio/', views.CreateEstadio.as_view(), name="create_estadio"),
    path('list_estadio/', views.ListEstadio.as_view(), name="list_estadio"),
    path('detail_estadio/<int:pk>/', views.DetailEstadio.as_view(), name="detail_estadio"),
    path('update_estadio/<int:pk>/', views.UpdateEstadio.as_view(), name="update_estadio"),
    path('delete_estadio/<int:pk>/', views.delete_estadio, name="delete_estadio"),
]

