from django.urls import path
from .views import CalculateStatistics
urlpatterns=[
    path("", CalculateStatistics.as_view(), name="calculate")
]