import random
import string

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save


class Article(models.Model):
    title = models.CharField(max_length=220, db_index=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='articles', null=True, blank=True, help_text="2MB dan o'shmasin")
    content = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.id})"

#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         if self.slug is None:
#             self.slug = slugify(self.title)
#         super().save()
#
#         if self.slug is None:
#             try:
#                 self.slug = slugify(self.title)
#             except Exception as e:
#                 self.slug = slugify(self.title)
#         super().save()
#
#
#     def article_pre_save(sender, instance, *args, **kwargs):
#         if instance.slug is None:
#             instance.slug = slugify(instance.title)
#
# # def article_post_save(sender, instance, created, *args, **kwargs):
# #     if created:
#
#
# pre_save.connect(article_pre_save, sender=Article)
# # post_save.connect(article_post_save, sender=Article)
