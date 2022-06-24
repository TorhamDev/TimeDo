from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from api_v1.models import Timer
from api_v1.serializers import TimerCreateSerializer, TimerInfoSerializer
from core.utils.exceptions import YouAreNotOwnerOfThisTimer
from core.utils.url_tools import create_short_link_for_timer
from datetime import datetime


class CreateTimer(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TimerCreateSerializer

    def post(self, request):
        
        data = request.data
        _mutable = data._mutable
        data._mutable = True 
        data["owner"] = request.user.id
        data["short_link"] = create_short_link_for_timer(5, request.build_absolute_uri('/')) 
        data._mutable = _mutable

        serializer = TimerCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)


class TimerInfo(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = TimerInfoSerializer

    def get(self, request, timer_id):

        timer = get_object_or_404(Timer, pk=timer_id)
        serializer = TimerInfoSerializer(instance=timer)

        return Response(serializer.data, 200)


class EndTimer(GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = TimerInfoSerializer

    def put(self, request, timer_id):

        timer = get_object_or_404(Timer, pk=timer_id)

        if request.user == timer.owner:
            timer.end_time = datetime.now()
            timer.is_end = True
            timer.save()

            serializer = TimerInfoSerializer(instance=timer)

            return Response(serializer.data)

        else:
            raise YouAreNotOwnerOfThisTimer


class StopTimer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TimerInfoSerializer
    
    def put(self, request, timer_id):
        timer = get_object_or_404(Timer, pk=timer_id)
        

        if request.user == timer.owner:
            timer.last_stop = datetime.now()
            timer.is_stop = True
            timer.save()

            serializer = self.serializer_class(instance=timer)

            return Response(serializer.data)


class StartTimer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TimerInfoSerializer

    def put(self, request, timer_id):
        timer = get_object_or_404(Timer, pk=timer_id)

        if request.user == timer.owner:
            timer.is_stop = False
            timer.save()

            serializer = self.serializer_class(instance=timer)

            return Response(serializer.data)


class GetTimerWthiShortLink(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = TimerInfoSerializer

    def get(self, request, short_link):

        timer = get_object_or_404(Timer, short_link__contains=short_link)
        serializer = TimerInfoSerializer(instance=timer)

        return Response(serializer.data)
 