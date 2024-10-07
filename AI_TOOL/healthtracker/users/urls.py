from django.urls import path
from .views import AppleHealthStatList, SleepConditionAPIView, Walked_10000_StepsAPIView, LowActivityAPIView

urlpatterns = [
    path('api/stats/', AppleHealthStatList.as_view(), name='health-stats'),
    path('api/sleep-condition/', SleepConditionAPIView.as_view(), name='sleep-condition'),
    path('api/walked-10000-steps/', Walked_10000_StepsAPIView.as_view(), name='walked-10000-steps'),
    path('api/walked-50-percent-less/', LowActivityAPIView.as_view(), name='walked-50-percent-less'),
]
