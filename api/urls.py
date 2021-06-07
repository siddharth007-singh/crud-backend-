from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.show, name="events"),
    path('create/', views.create, name="create"),
    path('filter/<str:pk>', views.showfilter, name="details"),
    path('delete/<str:pk>', views.delete, name="delete"),
    path('update/<str:pk>', views.update ,name="update"),
]
