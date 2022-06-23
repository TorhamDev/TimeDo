from api_v1.models import Timer, ToDo
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'id'
        )


class TimerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timer
        fields = (
            'owner',
            'title',
            'description',
            'short_link',
        )


class ToDoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"


class TimerInfoSerializer(serializers.ModelSerializer):
    todo = ToDoInfoSerializer(read_only=True, many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Timer
        fields = (
            'id',
            'owner',
            'title',
            'description',
            'start_time',
            'last_stop',
            'end_time',
            'is_archive',
            'short_link',
            'created',
            'updated',
            'todo',
        )
