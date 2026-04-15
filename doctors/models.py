from django.db import models # type: ignore

class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.full_name