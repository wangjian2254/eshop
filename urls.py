from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
from shop.views import Index, Goods, Search

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', Index.as_view()),
    (r'^goods', Goods.as_view()),
    (r'^search', Search.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)
