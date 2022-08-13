import json

from django.http import JsonResponse
from django.shortcuts import render

from ads.models import Category, Ads


def index(request):
    if request.method == "GET":
        return JsonResponse({"status": "ok"}, status=200)


def get_cat(request):
    if request.method == "GET":
        cat = Category.objects.all()
        response = []
        for cat_ in cat:
            response.append({
                "id": cat_.id,
                "name": cat_.name
            })
        return JsonResponse(response, safe=False)

    if request.method == "POST":
        cat = json.loads(request.body)
        add = Category.objects.create(**cat)
        response = {
            "name": add.name
        }
        return JsonResponse(response)


def get_ads(request):
    if request.method == "GET":
        ads = Ads.objects.all()
        response = []
        for ads_ in ads:
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


def get_cat_one(request, cat_id):
    if request.method == "GET":
        cat = Category.objects.get(pk=cat_id)
        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        })


def get_ads_one(request, ads_id):
    if request.method == "GET":
        ads = Ads.objects.get(pk=ads_id)
        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })
