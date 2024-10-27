from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator, EmailValidator
from django.db import models
from django.utils import timezone

class AuthorManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular author."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email) 
        author = self.model(email=email, **extra_fields)
        author.set_password(password)
        author.save(using=self._db)
        return author

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)

class Author(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='author_images/', blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    
    category = models.ManyToManyField('article.Category', related_name='authors')
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_author = models.BooleanField(default=True)
    is_reader = models.BooleanField(default=False)

    # Custom related names to avoid conflicts with the default auth.User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='author_set',  # Custom related name
        blank=True,
        help_text='The groups this author belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='author_permission_set',  # Custom related name
        blank=True,
        help_text='Specific permissions for this author.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AuthorManager()

    def __str__(self):
        return self.email

    @property
    def is_authenticated(self):
        return True
    

