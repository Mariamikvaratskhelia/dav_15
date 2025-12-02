from django.urls import path
from .views import lookups_view

urlpatterns = [
    
    path('lookups/', lookups_view, name='lookups'),
]
