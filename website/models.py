from django.db import models
from django.contrib import auth


POST_LEVEL = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("10", 10),
)

IMPORTANT_CONTACT_TYPE = (
    ("Ambulance", "Ambulance"),
    ("Hospital", "Hospital"),
    ("Nepal Police", "Nepal Police"),
    ("Electricity Authority", "Electricity Authority"),
    ("Water Supply", "Water Supply"),
    ("LPG Gas", "LPG Gas"),
    ("Others", "Others")
)


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


class SiteInfo(AbstractModel):  # only one can be active, if multiple, the latest will be taken
    version = models.PositiveIntegerField(default=0, unique=True)
    name = models.CharField(max_length=64)
    municipality = models.CharField(max_length=64)
    ward_no = models.CharField(max_length=3)
    district = models.CharField(max_length=64)
    province = models.CharField(max_length=64)
    image = models.ImageField(upload_to="site_info/")
    short_description = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.version)


class ExtraPage(AbstractModel):
    page_name = models.CharField(max_length=64)
    page_slug = models.SlugField(max_length=128)
    image = models.ImageField(upload_to="pages/", null=True, blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.page_name


class PlaceCategory(AbstractModel):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=128)
    icon = models.CharField(max_length=64)
    image = models.ImageField(upload_to="category/", null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Place(AbstractModel):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=128)
    category = models.ForeignKey(PlaceCategory, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="places/logo/", null=True, blank=True)
    image = models.ImageField(upload_to="places/")
    estb_date = models.PositiveIntegerField()
    service = models.TextField(blank=True)
    description = models.TextField(blank=True)
    office_location = models.CharField(max_length=128, blank=True)
    contact_person = models.CharField(max_length=64, blank=True)
    mobile = models.CharField(max_length=16, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    map_latitude_longitude = models.CharField(max_length=64, blank=True)
    view_count = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class ExecutiveMembers(AbstractModel):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    level = models.CharField(max_length=16, choices=POST_LEVEL)
    post = models.CharField(max_length=64)
    full_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="members/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.full_name} ({self.place.name})"


class ImageSlider(AbstractModel):
    slider_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="sliders/")

    def __str__(self) -> str:
        return self.slider_name


class ContactMessage(AbstractModel):
    sender_name = models.CharField(max_length=64)
    mobile = models.CharField(max_length=16, blank=True)
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self) -> str:
        return self.sender_name


class ImportantContact(AbstractModel):
    service_provider = models.CharField(max_length=64)
    service_type = models.CharField(max_length=64, choices=IMPORTANT_CONTACT_TYPE)
    contact_person = models.CharField(max_length=64)
    mobile_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    display_order = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.service_provider } ({self.service_type})"
