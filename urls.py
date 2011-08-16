from django.conf.urls.defaults import *
from ajaxfilemanager.settings import *

urlpatterns = patterns('',
    url(r'^$', 'ajaxfilemanager.views.index'),
    url(r'^actions/newfolder/(?P<folder>\w{0,50})/$', 'ajaxfilemanager.views.newfolder'),
    url(r'^actions/rmfile/$', 'ajaxfilemanager.views.rmfile'),
    url(r'^actions/rmfolder/$', 'ajaxfilemanager.views.rmfolder'),
    url(r'^upload', 'ajaxfilemanager.views.upload'),
    url(r'^uploader', 'ajaxfilemanager.views.handlefiles'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/maik/development/django/djangotest/templates/ajaxfilemanager'}),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': file_directory }),

)
