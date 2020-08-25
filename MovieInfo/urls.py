from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addmovie', views.AddMovie, name='addmovie'),
    path('form_submission', views.form_submission, name='form_submission'),
]
