from django.shortcuts import render
from rest_framework import status
from .decorators import validate_apikey, jwt_authentication_required
from .models import User, Train, Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, TrainSerializer, TrainAvailabilitySerializer
import random
import jwt

@api_view(['POST'])
@validate_apikey
def signup(request):
    user_data = request.data.copy()
    user_data['role'] = 'USER'
    serializer = UserSerializer(data=user_data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({'status_code': 200, 'user_id': user.id, 'status': 'Account succesfully created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@validate_apikey
def signup_admin(request):
    user_data = request.data.copy()
    user_data['role'] = 'ADMIN'
    serializer = UserSerializer(data=user_data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({'status_code': 200, 'user_id': user.id, 'status': 'Account succesfully created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try: 
        user = User.objects.get(username=username, password=password)
    except User.DoesNotExist:
        return Response({
            'status': 'Incorrect username/password provided. Please retry',
            'status_code': 401
        }, status=status.HTTP_401_UNAUTHORIZED)

    serializer = UserSerializer(user)
    access = jwt.encode(serializer.data, '12')
    return Response({
        'status': 'Login successful',
        'status_code': 200,
        'user_id': user.id,
        'access_token': access,
        'username': user.username,
        'email': user.email
    })

@api_view(['POST'])
@validate_apikey
def create_train(request):
    seat_capacity = request.data.get('seat_capacity')
    train_data = request.data.copy()
    train_data['available_seats'] = seat_capacity
    print('train', train_data)
    serializer = TrainSerializer(data=train_data)
    if serializer.is_valid():
        train = serializer.save()
        return Response({
            'message': 'Train added successfully',
            'train_id': train.id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@jwt_authentication_required
def train_availability(request):
    source = request.query_params.get('source')
    destination = request.query_params.get('destination')

    if not source or not destination:
        return Response({
            'status': 'Bad Request',
            'detail': 'Both source and destination must be provided.'
        }, status=status.HTTP_400_BAD_REQUEST)

    trains = Train.objects.filter(source=source, destination=destination)
    serializer = TrainAvailabilitySerializer(trains, many=True)

    return Response(serializer.data)
