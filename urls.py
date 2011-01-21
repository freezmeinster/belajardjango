from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^pools/$', 'belajardjango.pools.views.index'),
    (r'^pools/(?P<pool_id>\d+)/$', 'belajardjango.pools.views.detail'),
    (r'^pools/(?P<pool_id>\d+)/results/$', 'belajardjango.pools.views.results'),
    (r'^pools/(?P<pool_id>\d+)/vote$', 'belajardjango.pools.views.vote'),
)
