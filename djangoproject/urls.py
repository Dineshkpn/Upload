from django.conf.urls import patterns, include, url
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        (r'^myapp/', include('myapp.urls')),
        (r'', include('myapp.urls')),
        (r'^admin/', include(admin.site.urls)),

)
