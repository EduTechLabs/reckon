from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import Invoice.views
urlpatterns = [
url(r'^login/', Invoice.views.login),
url(r'^auth/', Invoice.views.auth),
url(r'^homepage/', Invoice.views.homepage),
]
