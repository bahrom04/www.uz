from django.urls import path
from rating.views import (
    CategoryViewSet,
    SubCategoryViewSet,
    WebsiteViewSet,
    RatingValueViewSet,
    GlobalRatingViewSet,
    VisitorViewSet
    )


urlpatterns = [
    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    path('subcategory/', SubCategoryViewSet.as_view({'get': 'list'})),
    path('website/', WebsiteViewSet.as_view({'get': 'list'})),
    path('ratingvalue/', RatingValueViewSet.as_view({'get': 'list'})),
    path('globalrating/', GlobalRatingViewSet.as_view({'get': 'list'})),
    path('visitor/', VisitorViewSet.as_view({'get': 'list'})),
]