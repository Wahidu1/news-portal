from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator, RegexValidator
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from content.models import BaseModel
class Author(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    bio = models.TextField(blank=True, null=True)  # Optional bio
    profile_image = models.ImageField(upload_to='author_images/', blank=True, null=True)  # Optional profile image
    password = models.CharField(max_length=255)  # Store the hashed password
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, blank=True, null=True)  # Optional address
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)  # Optional phone number
    category = models.ManyToManyField('article.Category', related_name='authors')  # Related to categories
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_author = models.BooleanField(default=True)
    is_reader = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        indexes = [models.Index(fields=['email'])]  # Index for faster lookups

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):  # Avoid re-hashing an already hashed password
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
