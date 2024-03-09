from django.urls import path
from .views import index_view,contact_view

urlpatterns = [
    path('', index_view, name='index_url'),
    path('create-contact', contact_view, name='contact_url')

]