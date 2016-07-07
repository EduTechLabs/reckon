from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import Invoice.views
urlpatterns = [
 url(r'^auth/',Invoice.views.auth),
 url(r'^login/',Invoice.views.login),
 url(r'^homepage/',Invoice.views.homepage),
 url(r'^invoice/',Invoice.views.invoice),
 url(r'^invoicepage/',Invoice.views.invoicePage),
 url(r'^client/(?P<id>\d+)/$',Invoice.views.clientlist,name='client'),
]
