from django.urls import path
from car import views


urlpatterns = [
    path('sahibdetal/<int:id>', views.sahib_detail_view, name='sahibdetal'),
    path('galeridetal/<int:id>', views.galeri_detail_view, name='galeridetal')
]