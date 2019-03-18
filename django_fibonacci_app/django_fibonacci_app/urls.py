#fibonacci_app URL Configuration

from django.conf.urls import url
from django.contrib import admin

from app.views import FibonacciAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', FibonacciAPIView.as_view()),

]
