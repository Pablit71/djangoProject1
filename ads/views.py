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

        response = []
        for cat_ in self.object_list:
            response.append({
                "id": cat_.id,
                "name": cat_.name
            })
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CreateCat(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)
        category = Category.objects.create(
            id=cat_data["id"],
            name=cat_data["name"]
        )
        category.name = cat_data["name"]
        category.id = cat_data["id"]

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


class GetAds(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_ads = request.GET.get("cat", None)
        if search_ads:
            self.object_list = self.object_list.filter(cat=search_ads)
        response = []
        for ads_ in self.object_list:
            response.append({
                "id": ads_.id,
                "name": ads_.name,
                "author": ads_.author,
                "price": ads_.price,
                "description": ads_.description,
                "address": ads_.address,
                "is_published": ads_.is_published
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)
        ads = Ads()
        ads.id = ads_data["id"]
        ads.name = ads_data["name"]
        ads.author = ads_data["author"]
        ads.price = ads_data["price"]
        ads.description = ads_data["description"]
        ads.address = ads_data["address"]
        ads.is_published = ads_data["is_published"]

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })


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
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })
