from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api_v1.models import Timer
from api_v1.serializers import TimerCreateSerializer, TimerInfoSerializer

from datetime import datetime


class Index(View):

    def get(self, request):

        return HttpResponse("<h1>TimeDo : timer with todo</h1>")


class CreateTimer(CreateAPIView):
    queryset = Timer.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TimerCreateSerializer


class TimerInfo(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = TimerInfoSerializer

    def get(self, request, timer_id):

        timer = get_object_or_404(Timer, pk=timer_id)
        request.build_absolute_uri()
        serializer = TimerInfoSerializer(instance=timer)

        return Response(serializer.data)


class StopTimer(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = TimerInfoSerializer

    def post(self, request, timer_id):

        timer = get_object_or_404(Timer, pk=timer_id)
        timer.end_time = datetime.now()
        timer.save()

        serializer = TimerInfoSerializer(instance=timer)

        return Response(serializer.data)

class GetTimerWthiShortLink(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = TimerInfoSerializer

    def get(self, request, short_link):

        timer = get_object_or_404(Timer, short_link=short_link)
        serializer = TimerInfoSerializer(instance=timer)

        return Response(serializer.data)
 