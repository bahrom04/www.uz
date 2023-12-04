from django.shortcuts import render
from rating.serializers import (
    CategorySerializer,
    SubCategorySerializer,
    WebsiteSerializer,
    RatingValueSerializer,
    GlobalRatingSerializer,
    VisitorSerializer
    )
from rating.models import (
    Category,
    SubCategory,
    Website,
    RatingValue,
    GlobalRating,
    Visitor,
    )
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import filters


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer


class RatingValueViewSet(viewsets.ModelViewSet):
    queryset = RatingValue.objects.all()
    serializer_class = RatingValueSerializer


class GlobalRatingViewSet(viewsets.ModelViewSet):
    queryset = GlobalRating.objects.all()
    serializer_class = GlobalRatingSerializer


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
