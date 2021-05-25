from django.urls import path
from .views import IndexView, TesteView
urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('test', TesteView.as_view(), )
]