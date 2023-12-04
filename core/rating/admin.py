from django.contrib import admin
from rating.models import Category, SubCategory, Website, Visitor, RatingValue


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Website)
admin.site.register(Visitor)
admin.site.register(RatingValue)


