from django.db import models
from vehicles.models import Vehicle

# Create your models here.
class ParkingSpot(models.Model):
    spot_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Número da vaga',
    )

    is_occupied = models.BooleanField(
        default=False,
        verbose_name='Vaga ocupada',
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
        verbose_name = 'Vaga de estacionamento'
        verbose_name_plural = 'Vagas de estacionamento'

    def __str__(self):
        return self.spot_number

class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Veículo',
    )

    parking_spot = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Vaga de estacionamento',
    )

    entry_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Horário de entrada',
    )

    exit_time = models.DateTimeField(
        blank=True, 
        null=True,
        verbose_name='Horário de saída',
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
        verbose_name = 'Registro de estacionamento'
        verbose_name_plural = 'Registros de estacionamento'

    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot} - {self.entry_time}'