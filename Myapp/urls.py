from django.urls import path

from Myapp import views

urlpatterns = [
    path('homepage/',views.homepage),
    path('emailenquiry/',views.emailenquiry),
]
