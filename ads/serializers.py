from rest_framework import serializers

from ads.models import Ads, User, Location, Category, Compilation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class LocationOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "lat", "lng"]


class LocationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "lat", "lng"]


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = User
        fields = ["last_name", "first_name", "location"]


class UserOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "username", "password", "role", "age"]


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "username", "password", "role", "age"]


class AdsSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Ads
        fields = ["id", "name", "author", "price", "description", "is_published", "image"]


class AdsOneSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Ads
        fields = ["id", "name", "author", "price", "description", "is_published", "image"]


class AdsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ["id", "name", "author", "price", "description", "is_published", "image"]


class CompilationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compilation
        fields = '__all__'


class CompilationCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Compilation
        fields = '__all__'


class CompilationUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Compilation
        fields = '__all__'
