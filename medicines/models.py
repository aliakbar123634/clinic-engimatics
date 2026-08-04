
from django.db import models


class Medicine(models.Model):


    name = models.CharField(
        max_length=200,
        unique=True
    )

    generic_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    company = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
#    python manage.py makemigrations medicines
#    python manage.py migrate medicines
#    python manage.py runserver