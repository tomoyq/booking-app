from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Room, RoomImage, OccupiedDate, User

class RoomImageSerializer(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(view_name='room-detail',
                                               queryset=Room.objects.all()),
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption', 'room']

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['url', 'id', 'name', 'type', 'pricePerNight', 'currency', 'maxOccupancy', 'description', 'images']

class OccupiedDateSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name = 'room-detail',
        queryset = Room.objects.all()
    )
    class Meta:
        model = OccupiedDate
        fields = ['url', 'id', 'room', 'date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'email', 'full_name']

    def validate_password(self, value):
        return make_password(value)