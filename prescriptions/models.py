

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from patients.models import Patient
from medicines.models import Medicine


# VISIT MODEL
class Visit(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='visits'
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    complaints = models.TextField(
        blank=True,
        null=True
    )

    diagnosis = models.TextField(
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    visit_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.patient.name} - {self.visit_date}"


# PRESCRIPTION MODEL
class Prescription(models.Model):

    visit = models.OneToOneField(
        Visit,
        on_delete=models.CASCADE,
        related_name='prescription'
    )

    instructions = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Prescription #{self.id}"


# PRESCRIPTION ITEM MODEL
class PrescriptionItem(models.Model):

    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name='items'
    )

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE
    )

    dosage = models.CharField(
        max_length=100
    )

    frequency = models.CharField(
        max_length=100
    )

    duration = models.CharField(
        max_length=100
    )

    notes = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):

        return self.medicine.name