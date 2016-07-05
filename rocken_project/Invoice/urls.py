from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import Invoice.views
urlpatterns = [
url(r'^login/', Invoice.views.login),
url(r'^auth/', Invoice.views.auth),
url(r'^homepage/', Invoice.views.homepage),
# # url(r'^client/', Invoice.views.clients),
# url(r'^client/(?P<id>[\w\-]+)/', Invoice.views.client),
url(r'^client/(?P<id>\d+)/$', Invoice.views.client, name='client_list')
]
