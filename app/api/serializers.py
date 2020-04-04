from rest_framework import serializers
from app.models import *


class userAdminSerializers(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'username', 'timezone', 'password', ]
        depth = 1

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validate_data):

        user = CustomUser.objects.create_user(
            username=validate_data['username'], password=validate_data['password'], timezone=validate_data['timezone'], id=validate_data['id'])

        return user


class normalUserSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        read_only_fields = ('url', 'id', 'username', 'timezone')
        fields = ['url', 'id', 'username', 'timezone']
        depth = 1


class normalActivitySerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = activity
        fields = ['url', 'start_time', 'end_time']
        depth = 1

    def create(self, validate_data):
        active = activity.objects.create(
            start_time=validate_data['start_time'], end_time=validate_data['end_time'], user_id=self.context['request'].user.id)

        return active


class AdminActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = activity
        read_only_fields = ('url', 'start_time', 'end_time', 'user')
        fields = ['url', 'start_time', 'end_time', 'user']
        depth = 1
