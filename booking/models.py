from django.db import models

class House(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва будинуку:")
    info = models.TextField(max_length=1024, verbose_name="Інформація за будинок:")
    country = models.TextField(max_length=15, verbose_name="Країна:")
    adress = models.CharField(max_length=100, verbose_name="Адреса будинку:")
    room_count = models.PositiveIntegerField(default=0, verbose_name="Кількість кімнат:")
    people_count = models.PositiveIntegerField(default=0, verbose_name="Кількість людей:")
    square = models.PositiveIntegerField(default=0, verbose_name="Площа будинку:")
    price_by_day = models.PositiveSmallIntegerField(verbose_name="Ціна за добу:")
    rating = models.PositiveIntegerField(default=0, verbose_name="Рейтинг:")
    is_booked = models.BooleanField(default=False, verbose_name="Заброньовано:")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.country} - {self.price_by_day}$ - {self.rating}"
    class Meta:
        verbose_name = "Будинок"
        verbose_name_plural = "Будинки"
        ordering = ["-created_at"]

class Client(models.Model):
    first_name = models.CharField(max_length=15, verbose_name="Ім'я:")
    last_name = models.CharField(max_length=15, verbose_name="Прізвище:")
    phone_number = models.CharField(max_length=20, unique=True, verbose_name="Номер телефону")
    email = models.EmailField(verbose_name="Елеткронна пошта:")
    age = models.PositiveBigIntegerField(verbose_name="Вік:")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнтти"
        ordering = ["-created_at"]


class Booking(models.Model):
    STATUS_CHOICES = [
        ("in_progress", "В обробці"),
        ("comfirmed", "Підтверджено"),
        ("canceled", "Скасовано"),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клієнт", related_name="bookings")
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name="Будинок", related_name="booking_all")
    arrival_date = models.DateField("Дата заїзду")
    departure_day = models.DateField(verbose_name="Дата віїзду")
    status = models.CharField(max_length=20,  choices=STATUS_CHOICES, default="in_progress", verbose_name="Статус:")
    comment = models.CharField(max_length=100, verbose_name="Коментарі")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} з {self.arrival_date} по {self.departure_day}"

    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"
        ordering = ["-created_at"]

