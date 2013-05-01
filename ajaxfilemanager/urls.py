from django.conf.urls import patterns, url
from ajaxfilemanager.settings import *

urlpatterns = patterns('',
    url(r'^$', 'ajaxfilemanager.views.index', name='index'),
    url(r'^index/$', 'ajaxfilemanager.views.index', name='index'), 
    url(r'^actions/newfolder/$', 'ajaxfilemanager.views.newfolder', name='newfolder'),
    url(r'^actions/rmfile/$', 'ajaxfilemanager.views.rmfile', name='rmfile'),
    url(r'^actions/rmfolder/$', 'ajaxfilemanager.views.rmfolder', name='rmfolder'),
    url(r'^actions/mvfile/$', 'ajaxfilemanager.views.mvfile', name='mvfile'),
    url(r'^upload/$', 'ajaxfilemanager.views.upload', name='upload'),
    url(r'^upload/uploader/$', 'ajaxfilemanager.views.handlefiles'),
    url(r'^noroot/$', 'ajaxfilemanager.views.noroot', name='noroot'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': TEMPLATE_DIRS[0]+"/ajaxfilemanager"}),
    #url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': file_directory }),

)
