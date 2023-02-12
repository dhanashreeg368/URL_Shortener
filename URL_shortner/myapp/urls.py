from django.contrib import admin
from django.urls import include, path
from .views import home_page
from myapp import views
from . import views

urlpatterns = [
    path('hello',views.hello_world),
    path('',views.home_page),
    path('task',views.task),
    path('all-analytics', views.all_analytics),
    path('<slug:short_url>', views.redirect_url)  
]
#localhost: 8000/hello