from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RatingValue

@receiver(post_save, sender=RatingValue)
def update_rating_count(sender, instance, created, **kwargs):
    if created:
        instance.website.visitors_count += 1
        instance.website.visitors_count_tasix += 1
        instance.website.save()