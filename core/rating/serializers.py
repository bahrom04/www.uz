from rating.models import Category, SubCategory, Website, Visitor, RatingValue, GlobalRating
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'title', 
            'category'
            ]


class GlobalRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlobalRating
        fields = [
            'id',
            'website',
            'position', 
            ]

class VisitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visitor
        fields = [
            'id',
            'visitors_count', 
            'visitors_count_tasix', 
            'website',
            ]
        

class WebsiteSerializer(serializers.ModelSerializer):
    global_rating = GlobalRatingSerializer()
    sub_category = SubCategorySerializer(many=True)
    visitor = VisitorSerializer()

    class Meta:
        model = Website
        fields = [
            'id',
            'title', 
            'url', 
            'register_date', 
            'name', 
            'description', 
            'sub_category',
            'global_rating',
            'visitor',
            ]
        
    def get_visitors_info(self, obj):
        return obj.visitors_info
    
    def get_global_ratings_info(self, obj):
        return obj.global_ratings_info
        

class RatingValueSerializer(serializers.ModelSerializer):
    # website = WebsiteSerializer()
    sub_category = SubCategorySerializer()
    class Meta:
        model = RatingValue
        fields = [
            'id',
            'sub_category'
            'website',
            'position', 
            ]
        
