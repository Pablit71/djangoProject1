import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Category, Ads


class IndexView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class GetCat(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_cat = request.GET.get("cat", None)
        if search_cat:
            self.object_list = self.object_list.filter(cat=search_cat)

        self.object_list = self.object_list.order_by("name")

        response = []
        for cat_ in self.object_list:
            response.append({
                "id": cat_.id,
                "name": cat_.name
            })
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CreateCat(CreateView):
    model = Category
    fields = ["id", "name"]

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)
        category = Category.objects.create(
            id=cat_data["id"],
            name=cat_data["name"]
        )

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


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

        self.object_list = self.object_list.order_by("name")
        response = []
        for ads_ in self.object_list:
            response.append({
                "id": ads_.id,
                "name": ads_.name,
                "price": ads_.price,
                "description": ads_.description,
                "is_published": ads_.is_published,
                "image": ads_.image.url
            })
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CreateAds(CreateView):
    model = Ads
    fields = ["id", "name", "author_id", "price", "description", "is_published", "image"]

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)
        ads = Ads.objects.create(
            id=ads_data["id"],
            name=ads_data["name"],
            author_id=ads_data["author_id"],
            price=ads_data["price"],
            description=ads_data["description"],
            is_published=ads_data["is_published"],
            image=ads_data["image"]
        )

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author_id": ads.author_id,
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


class CatOne(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        })


class AdsOne(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()
        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "image": ads.image,
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
