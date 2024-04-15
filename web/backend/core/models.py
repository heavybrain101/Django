from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         return self.create_user(email, password, **extra_fields)
# 
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


class Employe(models.Model):
    name = models.CharField(max_length=200)


class Profile(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    phone = models.CharField(max_length=200)
    office = models.CharField(max_length=200)


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
# 
#     objects = CustomUserManager()
# 
#     USERNAME_FIELD = "email"


class News(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="news_images/")


class Wallet(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, unique=True)
    wallet = models.IntegerField(default=4000)


class ShopCategory(models.Model):
    name = models.CharField(max_length=200)


class ShopItems(models.Model):
    shop = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200)
    coast = models.IntegerField()


class Cart(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    items = models.ManyToManyField(ShopItems)


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        username = username
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Имя пользователя",
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=255,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=255,
        null=True,
        blank=True
    )
    date_joined = models.DateField(
        auto_now_add=True,
        verbose_name="Дата регистрации",
    )
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)

    email = models.EmailField(
        "Email",
        null=False,
        unique=True,
        db_index=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)
