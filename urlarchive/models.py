from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    icon = models.CharField(max_length=50, default="fas fa-link")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class URL(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=500, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"
        ordering = ['title']

    def __str__(self):
        return self.title + " " + self.website
