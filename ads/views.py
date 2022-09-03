import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ads.models import Category, Ads, User, Location
from ads.serializers import AdsSerializers, UserSerializer, CategorySerializer, LocationSerializer, \
    CategoryOneSerializer
from djangoProject1 import settings


class IndexView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


class GetCat(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCat(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



@method_decorator(csrf_exempt, name='dispatch')
class UpdateCat(UpdateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        cat_data = json.loads(request.body)

        self.object.id = cat_data["id"]
        self.object.name = cat_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class DeleteCat(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class GetAds(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_ads = request.GET.get("ads", None)
        if search_ads:
            self.object_list = self.object_list.filter(ads=search_ads)

        self.object_list = self.object_list.order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_num = request.GET.get("page")
        page_obj = paginator.get_page(page_num)

        response = {
            "items": AdsSerializers(page_obj, many=True).data,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CreateAds(CreateView):
    model = Ads
    fields = ["id", "name", "author", "price", "description", "is_published", "image"]

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)
        ads = Ads.objects.create(
            id=ads_data["id"],
            name=ads_data["name"],
            price=ads_data["price"],
            description=ads_data["description"],
            is_published=ads_data["is_published"],
            image=ads_data["image"]
        )

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "image": ads.image,
        })


@method_decorator(csrf_exempt, name="dispatch")
class UpdateAds(UpdateView):
    model = Ads
    fields = ["id", "name", "price", "description", "is_published", "image"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ads_data = json.loads(request.body)

        self.object.id = ads_data["id"]
        self.object.name = ads_data["name"]
        self.object.price = ads_data["price"]
        self.object.description = ads_data["description"]
        self.object.is_published = ads_data["is_published"]
        self.object.image = ads_data["image"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image
        })


@method_decorator(csrf_exempt, name='dispatch')
class DeleteAds(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class CatOne(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryOneSerializer

class AdsOne(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()
        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author.first_name,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "image": ads.image.url,
        })


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


@method_decorator(csrf_exempt, name='dispatch')
class GetUser(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_user = request.GET.get("user", None)
        if search_user:
            self.object_list = self.object_list.filter(user=search_user)

        self.object_list = self.object_list.order_by("username")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_num = request.GET.get("page")
        page_obj = paginator.get_page(page_num)

        for users in self.object_list:
            count = 0
            ads_user = Ads.objects.all()
            for count_ads in ads_user:
                if users.id == count_ads.author_id:
                    count += 1

        response = {
            "items": UserSerializer(page_obj, many=True).data,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }
        return JsonResponse(response, safe=False)


class UserOne(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({
            "last_name": user.last_name,
            "first_name": user.first_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "location": user.location.name,
            "total_ads": user.author_id.count
        })


@method_decorator(csrf_exempt, name="dispatch")
class CreateUser(CreateView):
    model = User
    fields = ["id", "last_name", "first_name", "username", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user = User.objects.create(
            id=user_data["id"],
            last_name=user_data["last_name"],
            first_name=user_data["first_name"],
            username=user_data["username"],
            role=user_data["role"],
            age=user_data["age"],
            location=user_data["location"]
        )

        #

        return JsonResponse({
            "last_name": user.last_name,
            "first_name": user.first_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "location": user.location.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class UpdateUser(UpdateView):
    model = User
    fields = ["id", "last_name", "first_name", "username", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        self.object.last_name = user_data["last_name"]
        self.object.first_name = user_data["first_name"]
        self.object.username = user_data["username"]
        self.object.role = user_data["role"]
        self.object.age = user_data["age"]
        self.object.location = user_data["location"]

        self.object.save()

        return JsonResponse({
            "last_name": self.object.last_name,
            "first_name": self.object.first_name,
            "username": self.object.username,
            "role": self.object.role,
            "age": self.object.age,
            "location": self.object.location
        })


@method_decorator(csrf_exempt, name='dispatch')
class DeleteUser(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CreateLocation(CreateView):
    model = Location
    fields = ["id", "name", "lat", "lng"]

    def post(self, request, *args, **kwargs):
        location_data = json.loads(request.body)
        location = Location.objects.create(
            id=location_data["id"],
            name=location_data["name"],
            lat=location_data["lat"],
            lng=location_data["lng"],
        )

        location.name = get_object_or_404(Location, pk=location_data["id"])

        return JsonResponse({
            "id": location.id,
            "name": location.name,
            "lat": location.lat,
            "lng": location.lng,
        })


@method_decorator(csrf_exempt, name='dispatch')
class GetLocation(ListView):
    model = Location

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_location = request.GET.get("location", None)
        if search_location:
            self.object_list = self.object_list.filter(cat=search_location)

        self.object_list = self.object_list.order_by("name")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_num = request.GET.get("page")
        page_obj = paginator.get_page(page_num)

        response = {
            "items": LocationSerializer(page_obj, many=True).data,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }
        return JsonResponse(response, safe=False)
