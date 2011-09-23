from django.conf.urls.defaults import *
from ajaxfilemanager.settings import *

# Change it to your project settings
from djangotest.settings import *

urlpatterns = patterns('',
    url(r'^$', 'ajaxfilemanager.views.index'),
    url(r'^actions/newfolder/$', 'ajaxfilemanager.views.newfolder'),
    url(r'^actions/rmfile/$', 'ajaxfilemanager.views.rmfile'),
    url(r'^actions/rmfolder/$', 'ajaxfilemanager.views.rmfolder'),
    url(r'^actions/mvfile/$', 'ajaxfilemanager.views.mvfile'),
    url(r'^upload', 'ajaxfilemanager.views.upload'),
    url(r'^uploader', 'ajaxfilemanager.views.handlefiles'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': TEMPLATE_DIRS[0]+"/ajaxfilemanager"}),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': file_directory }),

)
