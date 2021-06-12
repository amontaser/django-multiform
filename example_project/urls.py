from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.urls import reverse, reverse_lazy
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^chaining/', include('smart_selects.urls')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy("office:Office_list")), name='home'),
    re_path(r'^office/', include(('office.urls', 'office'), namespace = 'office')),
]
