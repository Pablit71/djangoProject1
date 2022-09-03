import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Category, Ads, User, Location
from ads.serializers import AdsSerializer, UserSerializer, CategorySerializer, LocationSerializer, \
    CategoryOneSerializer, CategoryDeleteSerializer, AdsDeleteSerializer, AdsOneSerializer, UserOneSerializer, \
    UserDeleteSerializer, LocationDeleteSerializer, LocationOneSerializer
from djangoProject1 import settings


class IndexView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


# category VIEW
class GetCat(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CatOne(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryOneSerializer


class CreateCat(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCat(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCat(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer


# ads VIEW
class GetAds(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class CreateAds(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class UpdateAds(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class DeleteAds(DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsDeleteSerializer


class AdsOne(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsOneSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdsImageView(UpdateView):
    model = Ads
    fields = ["id", "name", "author_id", "price", "description", "is_published", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None
        })


# User VIEW

class GetUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserOne(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserOneSerializer


class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUser(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUser(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer


# Location VIEW
class CreateLocation(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class GetLocation(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class OneLocation(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationOneSerializer


class DeleteLocation(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDeleteSerializer


class UpdateLocation(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
