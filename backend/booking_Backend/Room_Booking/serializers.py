from rest_framework import serializers

from .models import Room, RoomImage

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