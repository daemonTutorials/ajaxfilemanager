# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import ajaxfilemanager
import os
import subprocess
import shutil

def findpath(path):
    above = path[::-1]
    above_int = above.find("/")
    above_pp = above.split(above[above_int])
    above_pp.remove(above_pp[0])
    output = ""
    for tail in above_pp:
        output += tail
    
    output += ""
    above = output[::-1]
    return above

def copytree(src, dst, symlinks=False, ignore=None):
    if os.path.isdir(dst) == False:
        os.mkdir(dst)
        
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def upload(request):
    return render_to_response('ajaxfilemanager/upload.html', { 'ajaxfilemanager': ajaxfilemanager  }, context_instance=RequestContext(request))

def index(request):
    try:
        ajax = request.GET['ajax']
    except (KeyError):
        ajax = ""
             
    try:
        path = request.GET['path']
    except (KeyError):
        return HttpResponseRedirect("/ajaxfilemanager/?path=")
    else:
                    
        if path != "":
            if ajax != "true":
                currentpath = path+"/"
            else:
                currentpath = path
                
            above = findpath(path)
        else:
            currentpath = path
            above = ""
                
        if path != "/":
            if path != "" and ajax != "true":
                path = os.path.join(ajaxfilemanager.settings.file_directory,path)+"/" #[1:len(path)]
            else:
                path = os.path.join(ajaxfilemanager.settings.file_directory,path) #[1:len(path)]
        else:
            return HttpResponseRedirect("/ajaxfilemanager/noroot")
            
        resultdirlist = []        
        filelist = []
        filenames = []
        mimetypes = []  
        filemime = []      
        dirlist = os.listdir(path)
        for item in dirlist:
            if os.path.isfile(os.path.join(path, item)) == False:
                resultdirlist.append(item)
            else:
                filelist.append(item)
                filenames.append(item)
        
        for item in filelist:
            if ".html" in item or ".htm" in item:
                mimetypes.append("text/html")
            elif ".css" in item:
                mimetypes.append("text/css")
            elif ".js" in item:
                mimetypes.append("text/javascript")            
            else:            
                filepath = os.path.join(path, item)
                mime = subprocess.Popen(["/usr/bin/file", "-i", filepath], shell=False, stdout=subprocess.PIPE).communicate()
                mime = mime[0].split(";")
                mime = mime[0].split(":")
                mimetypes.append(mime[1])
        

        for i in range(len(filelist)):
            #filelist[i] += " - ["+mimetypes[i]+"]"   
            filemime.append([filelist[i],mimetypes[i]])
            
        if not ajax:
            return render_to_response('ajaxfilemanager/index.html', { 'ajaxfilemanager': ajaxfilemanager, 'resultdirlist': resultdirlist, 'filelist': filelist, 'currentpath': currentpath, 'path': path, 'above': above, 'filenames': filenames, 'filemime': filemime }, context_instance=RequestContext(request))
        elif ajax == "true":
            return render_to_response('ajaxfilemanager/directory_listing.html', { 'ajaxfilemanager': ajaxfilemanager, 'resultdirlist': resultdirlist, 'filelist': filelist, 'currentpath': currentpath, 'path': path, 'above': above, 'filenames': filenames, 'filemime': filemime }, context_instance=RequestContext(request)) 

def newfolder(request):
    try:
        path = request.GET['path']
        folder = request.GET["folder"]
    except (KeyError):
        return HttpResponse("No path exist")
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory, path)
        if os.access(path, os.W_OK):
            os.chdir(path)
            os.mkdir(folder)
            return HttpResponse("Folder successfully created")


def rmfile(request):
    try:
        path = request.GET['path']
        filename = request.GET["filename"]
    except (KeyError):
        return HttpResponse("No path exist")
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        print(path+" "+currentpath+" "+ajaxfilemanager.settings.file_directory)
        if os.access(path, os.W_OK):
            os.chdir(path)
            os.remove(filename)
            return HttpResponse("File successfully deleted")       

def rmfolder(request):
    try:
        path = request.GET['path']
        folder = request.GET["folder"]
    except (KeyError):
        return HttpResponse("No path exist")
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        if os.access(path, os.W_OK):
            os.chdir(path)
            shutil.rmtree(folder)
            return HttpResponse("Folder successfully deleted")

def mvfile(request):
    class InvalidPath(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)


    try:
        path = request.GET['path']
        filepath = request.GET["filepath"]
        filename = request.GET["filename"]
        
    except KeyError:
        return HttpResponse("No path exist")
        
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        if os.access(path, os.W_OK):
            src = os.path.join(path,filename)
            dst = os.path.join(ajaxfilemanager.settings.file_directory,filepath)
            shutil.move(src, dst)
            return HttpResponse("File successfully moved")
            
def mvfolder(request):
    class InvalidPath(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)


    try:
        path = request.GET['path']
        filepath = request.GET["folderpath"]
        filename = request.GET["foldername"]
        
    except KeyError:
        return HttpResponse("No path exist")
        
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        if os.access(path, os.W_OK):
            src = os.path.join(path,filename)
            dst = os.path.join(ajaxfilemanager.settings.file_directory,filepath)
            shutil.move(src, dst)
            return HttpResponse("Folder successfully moved")
            
def cpfile(request):
    class InvalidPath(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)


    try:
        path = request.GET['path']
        filepath = request.GET["filepath"]
        filename = request.GET["filename"]
        
    except KeyError:
        return HttpResponse("No path exist")
        
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        if os.access(path, os.W_OK):
            src = os.path.join(path,filename)
            dst = os.path.join(ajaxfilemanager.settings.file_directory,filepath)
            shutil.copy(src, dst)
            return HttpResponse("File successfully copied")
            
def cpfolder(request):
    class InvalidPath(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)


    try:
        path = request.GET['path']
        filepath = request.GET["folderpath"]
        filename = request.GET["foldername"]
        
    except KeyError:
        return HttpResponse("No path exist")
        
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        if os.access(path, os.W_OK):
            src = os.path.join(path,filename)
            dst = os.path.join(ajaxfilemanager.settings.file_directory,filepath,filename)
            copytree(src, dst)
            return HttpResponse("Folder successfully copied")
            

@csrf_protect
def handlefiles(request):
	uploadedFile = default_storage.save(ajaxfilemanager.settings.file_directory+request.POST["filename"], ContentFile(request.FILES["Filedata"].read()))
	return HttpResponse("Success!")
    
def noroot(request):
    return HttpResponse("You are not root and can't access to '/'. Please go <a href='../?path='>back</a>.")

    
