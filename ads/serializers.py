from rest_framework import serializers

from ads.models import Ads, User, Location, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["name"]


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True)

    class Meta:
        model = User
        fields = ["last_name", "first_name", "location"]


class AdsSerializers(serializers.ModelSerializer):
    author = UserSerializer(many=True)

    class Meta:
        model = Ads
        fields = ["id", "name", "author", "price", "description", "is_published", "image"]
