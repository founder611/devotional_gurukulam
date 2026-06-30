from django.urls import path

from Myapp import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('emailenquiry/',views.emailenquiry,name='emailenquiry'),
]
