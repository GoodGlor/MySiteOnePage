from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.one_page),
    path('ajax/form_submission/', views.handle_ajax_form, name='ajax_form_submission'),

]
