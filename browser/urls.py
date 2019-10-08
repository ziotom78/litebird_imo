from django.urls import path

from . import views

urlpatterns = [
    path("", views.EntityTypeListView.as_view(), name="index"),
    path("entity_types/<int:pk>/", views.EntityTypeView.as_view(), name="entity_type_detail"),
    path("entity/<str:pk>/", views.EntityView.as_view(), name="entity_detail"),
    path("data_file/<str:pk>/", views.DataFileView.as_view(), name="data_file_detail"),
]
