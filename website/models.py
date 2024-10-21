from django.db import models
from django.contrib import auth


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# User Authentication and Authorization
class Operator(AbstractModel):
    user = models.OneToOneField(auth.get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.full_name


class Page(AbstractModel):
    page_name = models.CharField(max_length=64)
    page_slug = models.SlugField(max_length=128)
    image = models.ImageField(upload_to="pages/", null=True, blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.page_name
