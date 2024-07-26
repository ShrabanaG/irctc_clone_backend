from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'

class Train(models.Model):
    train_name = models.CharField(max_length=150)
    source = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    seat_capacity = models.IntegerField()
    arrival_time_at_source = models.CharField(max_length=150)
    arrival_time_at_destination = models.CharField(max_length=150)
    available_seats = models.IntegerField(default=0)

    def __str__(self):
        return self.train_name

    class Meta:
        db_table = 'trains'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    no_of_seats = models.IntegerField()
    seat_numbers = models.JSONField()  # Store seat numbers in JSON format

    def __str__(self):
        return f"Booking by {self.user.username} on {self.train.train_name}"
    
    class Meta:
        db_table = 'bookings'