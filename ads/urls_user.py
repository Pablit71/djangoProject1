from django.urls import path

from ads import views

urlpatterns = [
    path("", views.GetUser.as_view()),
    path("<int:pk>", views.UserOne.as_view()),
    path("create", views.CreateUser.as_view()),
    path("<int:pk>/delete", views.DeleteUser.as_view()),
    path("<int:pk>/update", views.UpdateUser.as_view()),
]
