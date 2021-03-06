from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api_v1.views.timer_views import (
    CreateTimer,
    TimerInfo,
    EndTimer,
    StopTimer,
    StartTimer,
)


schema_view = get_schema_view(
    openapi.Info(
        title="TimeDo API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

yasg_drf_patterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]


urlpatterns = [

    path('timer/new', CreateTimer.as_view(), name="create_timer"),
    path('timer/<timer_id>/', TimerInfo.as_view(), name="timer_info"),
    path('timer/end/<timer_id>/', EndTimer.as_view(), name="end_timer"),
    path('timer/stop/<timer_id>/', StopTimer.as_view(), name="stop_timer"),
    path('timer/start/<timer_id>/', StartTimer.as_view(), name="start_timer"),

] + yasg_drf_patterns
