from django.conf.urls.defaults import *
from ajaxfilemanager.settings import *

# Change it to your project settings
from djangotest.settings import *

urlpatterns = patterns('',
    url(r'^$', 'ajaxfilemanager.views.index'),
    url(r'^actions/newfolder/(?P<folder>\w{0,50})/$', 'ajaxfilemanager.views.newfolder'),
    url(r'^actions/rmfile/(?P<filename>\w{0,50})/$', 'ajaxfilemanager.views.rmfile'),
    url(r'^actions/rmfolder/(?P<folder>\w{0,50})/$', 'ajaxfilemanager.views.rmfolder'),
    url(r'^upload', 'ajaxfilemanager.views.upload'),
    url(r'^uploader', 'ajaxfilemanager.views.handlefiles'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': TEMPLATE_DIRS[0]+"/ajaxfilemanager"}),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': file_directory }),

)
