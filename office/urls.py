from django.urls import path, re_path
from .views import OfficeListView, OfficeCreateView

name = 'office'
urlpatterns = []

# Address URLs
urlpatterns =[
    path('',
        view=OfficeListView.as_view(),
        name='office_list'
    ),
    path('create',
        view=OfficeCreateView.as_view(),
        name='office_create',
    ),
]

