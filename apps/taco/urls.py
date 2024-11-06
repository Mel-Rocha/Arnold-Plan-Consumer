from django.urls import path
from apps.taco import views as taco_views

urlpatterns = [
    path('taco/', taco_views.taco_view, name='taco_view'),
]