from django.db import models
from customers.models import Customer

# Create your models here.

class VehiclesType(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name='Nome do veículo',
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição do veículo',
    )

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehiclesType, 
        on_delete=models.PROTECT,
        related_name='vehicles',
        verbose_name='Tipo de veículo',
    )

    license_plate = models.CharField(
        max_length=10, 
        unique=True, 
        verbose_name='Placa',
    )

    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='vehicles',
        verbose_name='Proprietário',
    )

    brand = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Marca do veículo',
    )

    model = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Modelo do veículo',
    )
    
    color = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Cor',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de criação',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de atualização',
    )

    class Meta:
            verbose_name = 'Veículo'
            verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.license_plate