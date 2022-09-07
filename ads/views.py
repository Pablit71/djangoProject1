import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ads, User, Location
from ads.serializers import AdsSerializer, UserSerializer, CategorySerializer, LocationSerializer, \
    CategoryOneSerializer, CategoryDeleteSerializer, AdsDeleteSerializer, AdsOneSerializer, UserOneSerializer, \
    UserDeleteSerializer, LocationDeleteSerializer, LocationOneSerializer
from djangoProject1 import settings


class IndexView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


# Category VIEW
class GetCat(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CatOne(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryOneSerializer


class DeleteCat(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer


class UpdateCat(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCat(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ads VIEW
class GetAds(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    def get(self, request, *args, **kwargs):
        ads_category_id = request.GET.get('cat', None)
        if ads_category_id:
            self.queryset = self.queryset.filter(
                category__id__exact=ads_category_id
            )

        ads_text = request.GET.get('text', None)
        if ads_text:
            self.queryset = self.queryset.filter(
                text__icontains=ads_text
            )

        ads_location = request.GET.get('location', None)
        if ads_location:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=ads_location
            )

        ads_price_from = request.GET.get('price_from', None)
        if ads_price_from:
            self.queryset = self.queryset.filter(
                price__gte=ads_price_from
            )

        ads_price_to = request.GET.get('price_to', None)
        if ads_price_to:
            self.queryset = self.queryset.filter(
                price__lte=ads_price_to
            )

        return super().get(request, *args, **kwargs)


class AdsOne(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = AdsOneSerializer


class DeleteAds(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = AdsDeleteSerializer


class UpdateAds(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = AdsSerializer


class CreateAds(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = AdsSerializer


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
class UserSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Location VIEW
class LocationSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
