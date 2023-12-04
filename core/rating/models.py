from django.db import models
from utils.models import BaseModel
from rating.serializers import VisitorSerializer, GlobalRatingSerializer
from django.utils.functional import lazy_import

VisitorSerializer = lazy_import('rating.serializers', VisitorSerializer)
GlobalRatingSerializer = lazy_import('rating.serializers', GlobalRatingSerializer)


class Category(BaseModel):
    title = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.title


class Website(BaseModel):
    title         = models.CharField(max_length=255)
    url           = models.URLField()
    register_date = models.DateField()
    name          = models.TextField()
    description   = models.TextField()

    sub_category = models.ManyToManyField(SubCategory, related_name="websites")

    @property
    def visitors_info(self):
        return VisitorSerializer(self.visitor_set.all(), many=True).data
    
    @property
    def global_ratings_info(self):
        return GlobalRatingSerializer(self.globalrating_set.all(), many=True).data
    

    class Meta:
        verbose_name = "Website"
        verbose_name_plural = "Websites"


    def __str__(self):
        return self.title


class Visitor(BaseModel):
    visitors_count = models.PositiveIntegerField(default=0)
    visitors_count_tasix = models.PositiveIntegerField(default=0)

    website = models.ForeignKey(Website, on_delete=models.CASCADE)    

    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitors"

    def __str__(self):
        # Ko'p query ketadi noiloj. Object (1) dan ko'ra yaxshi
        return f"{self.website.title} - {self.created_at}: visitors"


class RatingValue(BaseModel):
    position = models.PositiveIntegerField(default=0) # yesterday's rating
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return self.website.title
    

class GlobalRating(BaseModel):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("website", "position")
        ordering = ["position"]
        verbose_name = "GlobalRating"
        verbose_name_plural = "GlobalRatings"

    def __str__(self):
        return self.website.title
