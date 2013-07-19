from django.conf.urls import patterns, url
from django.conf.urls.static import static
from ajaxfilemanager.settings import *

urlpatterns = patterns('',
    url(r'^$', 'ajaxfilemanager.views.index', name='index'),
    url(r'^index/$', 'ajaxfilemanager.views.index', name='index'), 
    url(r'^editor/$', 'ajaxfilemanager.views.editor', name='editor'),
    url(r'^actions/newfolder/$', 'ajaxfilemanager.views.newfolder', name='newfolder'),
    url(r'^actions/rmfile/$', 'ajaxfilemanager.views.rmfile', name='rmfile'),
    url(r'^actions/rmfolder/$', 'ajaxfilemanager.views.rmfolder', name='rmfolder'),
    url(r'^actions/mvfile/$', 'ajaxfilemanager.views.mvfile', name='mvfile'), 
    url(r'^actions/mvfolder/$', 'ajaxfilemanager.views.mvfolder', name='mvfolder'), 
    url(r'^actions/cpfile/$', 'ajaxfilemanager.views.cpfile', name='cpfile'),
    url(r'^actions/cpfolder/$', 'ajaxfilemanager.views.cpfolder', name='cpfolder'),
    url(r'^actions/renamefile/$', 'ajaxfilemanager.views.renamefile', name='renamefile'),
    url(r'^actions/renamefolder/$', 'ajaxfilemanager.views.renamefolder', name='renamefolder'),
    url(r'^actions/editfile/$', 'ajaxfilemanager.views.editfile', name='editfile'),
    url(r'^upload/$', 'ajaxfilemanager.views.upload', name='upload'),
    url(r'^upload/uploader/$', 'ajaxfilemanager.views.handlefiles'),
    url(r'^noroot/$', 'ajaxfilemanager.views.noroot', name='noroot'),
    url(r'^ajaxfmmedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': file_directory}),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': TEMPLATE_DIRS[0]+"/ajaxfilemanager"}),
    #url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': file_directory }),

)
