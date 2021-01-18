from django.urls import path
from .views import hello_world, get_link

app_name = 'new_app'

urlpatterns = [
    path('', hello_world),
    path('link/<str:link_code>/',get_link, name='get_link')
]