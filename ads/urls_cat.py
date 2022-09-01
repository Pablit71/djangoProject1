from django.urls import path

from ads import views

urlpatterns = [
    path("", views.GetCat.as_view()),
    path("<int:pk>", views.CatOne.as_view()),
    path("create", views.CreateCat.as_view()),
    path("<int:pk>/delete", views.DeleteCat.as_view()),
    path("<int:pk>/update", views.UpdateCat.as_view()),
]
