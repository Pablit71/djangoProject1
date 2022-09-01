from django.urls import path

from ads import views

urlpatterns = [
    path("", views.GetAds.as_view()),
    path("<int:pk>", views.AdsOne.as_view()),
    path("create", views.CreateAds.as_view()),
    path("<int:pk>/delete", views.DeleteAds.as_view()),
    path("<int:pk>/update", views.UpdateAds.as_view()),
    path("<int:pk>/image", views.AdsImageView.as_view()),
]
