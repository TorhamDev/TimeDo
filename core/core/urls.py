from django.contrib import admin
from django.urls import path, include
from api_v1.views.index_views import Index
from api_v1.views.timer_views import GetTimerWthiShortLink

urlpatterns = [
    path('', Index.as_view(), name="site_index"),
    path('admin/', admin.site.urls),
    path('api/v1/', include("api_v1.urls")),

    path('timer/<short_link>/', GetTimerWthiShortLink.as_view())

]
