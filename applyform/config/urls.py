"""applyform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

import forms_builder.forms.urls

from main.views import IndexView, SuccessView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^forms/', include(forms_builder.forms.urls)),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^success/$', SuccessView.as_view(), name='success'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
