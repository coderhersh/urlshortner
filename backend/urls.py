from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.submit, name='submit'),
    path('<requested_short_url>', views.short_url_to_long_url),
]
