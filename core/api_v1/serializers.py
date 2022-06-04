from api_v1.models import Timer, ToDo
from rest_framework import serializers


class TimerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timer
        fields = (
            'title',
            'description',
        )


class ToDoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"


class TimerInfoSerializer(serializers.ModelSerializer):
    todo = ToDoInfoSerializer(read_only=True, many=True)

    class Meta:
        model = Timer
        fields = (
            'id',
            'title',
            'description',
            'start_time',
            'end_time',
            'is_archive',
            'short_link',
            'created',
            'updated',
            'todo'
        )

    def to_representation(self, instance):
        """Convert shortlink to clickeble link"""
        data_response = super().to_representation(instance)
        data_response["short_link"] = "http" + "://" + \
            "127.0.0.1:8000" + "/timer/" + data_response["short_link"]

        return data_response