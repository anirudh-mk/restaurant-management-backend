from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=36)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = None
    phone = None
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    @classmethod
    def email_exists(cls, email):
        return cls.objects.filter(email=email).exists()

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), max_length=36)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'country'

    def __str__(self):
        return self.name


class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), max_length=36)
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='state_country')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'state'

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), max_length=36)
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='district_state')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), max_length=36)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    location = models.CharField(max_length=500)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, related_name='resturent_district')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'resturent'

    def __str__(self):
        return self.name


class Catogery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), max_length=36)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'catogery'

    def __str__(self):
        return self.name


class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), max_length=36)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    rating = models.IntegerField()
    resturent = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='food_resturent')
    catogery = models.ForeignKey(Catogery, on_delete=models.DO_NOTHING, related_name='food_catogery')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'food'

    def __str__(self):
        return f"food:{self.name} resturent:{self.resturent.name}"


class Igredients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), max_length=36)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ingredients'

    def __str__(self):
        return self.name


class FoodIngredientsLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), max_length=36)
    ingredient = models.ForeignKey(Igredients, on_delete=models.CASCADE, related_name='food_ingredients_link_ingredient')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_ingredients_link_food')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'food_ingredients_link'

    def __str__(self):
        return f" food:{self.food.name} ingredient:{self.ingredient.name}"
