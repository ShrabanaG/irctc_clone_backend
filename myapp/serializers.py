from rest_framework import serializers
from .models import User, Train, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['train_name', 'source', 'destination', 'arrival_time_at_source', 'arrival_time_at_destination', 'seat_capacity', 'available_seats']

class TrainAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['id', 'train_name', 'available_seats']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user', 'train', 'no_of_seats', 'seat_numbers']