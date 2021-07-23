from django.db import models


# Unit Tables
class Hotel(models.Model):
    """ Hotel model for storage data of hotel """

    name = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'hotel'

    def __str__(self):
        return self.name


class RoomType(models.Model):
    """ model for many type's room """

    type_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'room_types'

    def __str__(self):
        return self.type_name


class ReservationStatusCalalog(models.Model):
    """ this model storage all type of reservation """

    name = models.CharField(max_length=150)

    class Meta:
        db_table = "reservation_status_calalogs"

    def __str__(self):
        return self.name


class Guest(models.Model):
    """ Guest model for peoples data """

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "guests"
        verbose_name = "guest"
        verbose_name_plural = "guests"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

# Tables with relations

class Room(models.Model):
    """ Room model for guest"""

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.RESTRICT)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "rooms"
        verbose_name = "room"
        verbose_name_plural = "rooms"

    def __str__(self):
        return '%s %s' % (self.room_name, self.room_type)

class Reservation(models.Model):
    """ Reservation model for save data reservation """

    guest = models.ForeignKey(Guest, on_delete=models.RESTRICT)
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoices = models.ManyToManyField(Guest, through='InvoiceGuest', related_name="invoice_guest")
    rooms = models.ManyToManyField(Room, through='RoomReserved')
    status = models.ManyToManyField(ReservationStatusCalalog, through='ReservationStatusEvent')

    class Meta:
        db_table = "reservations"
        verbose_name = "reservation"
        verbose_name_plural = "reservations"

    # def __str__(self):
    #     return self.name


class InvoiceGuest(models.Model):
    """ this model is for save invoce for each reservations"""

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    Invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateTimeField(auto_now_add=True)
    date_paid = models.DateField(auto_now=False, auto_now_add=False)
    date_canceled = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'invoice_guest'
        verbose_name = "invoice_guest"
        unique_together = [['guest', 'reservation']]

    # def __str__(self):
    #     return self.name


class RoomReserved(models.Model):
    """ this model is for storage the rooms reservated with specific price """

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'room_reserved'
        unique_together = [['reservation', 'room']]

    def __str__(self):
        return self.room.name


class ReservationStatusEvent(models.Model):
    """ this model storage a collection  when change an status in the reservation """

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    status_catalog = models.ForeignKey(ReservationStatusCalalog, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reservation_status_event'
        unique_together = [['reservation', 'status_catalog']]

    def __str__(self):
        return self.status_catalog.name
