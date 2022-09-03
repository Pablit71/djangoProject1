from django.urls import path

from ads import views

urlpatterns = [
    path("", views.GetLocation.as_view()),
    path("<int:pk>", views.OneLocation.as_view()),
    path("create", views.CreateLocation.as_view()),
    path("<int:pk>/delete", views.DeleteLocation.as_view()),
    path("<int:pk>/update", views.UpdateLocation.as_view()),
    ]