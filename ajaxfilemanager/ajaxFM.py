import os
import shutil
from django.http import HttpResponse

import ajaxfilemanager
    
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
        
def rm(request,datatype):
    try:
        path = request.GET['path']
        if datatype == "file":
            filename = request.GET["filename"]
        elif datatype == "folder":
            folder = request.GET["folder"]
        
    except (KeyError):
        return HttpResponse("No path exist")
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        print(path+" "+currentpath+" "+ajaxfilemanager.settings.file_directory)
        if os.access(path, os.W_OK):
            os.chdir(path)
            if datatype == "file":
                os.remove(filename)
            elif datatype == "folder":
                os.rmtree(folder)
            
            return HttpResponse(datatype+" successfully deleted")
            
def mv(request, datatype):
    class InvalidPath(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)


    try:
        path = request.GET['path']
        if datatype == "file":
            filepath = request.GET["filepath"]
            filename = request.GET["filename"]
        elif datatype == "folder":
            folderpath = request.GET["folderpath"]
            foldername = request.GET["foldername"]
    
    except KeyError:
        return HttpResponse("No path exist")
    
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        if os.access(path, os.W_OK):
            if datatype == "file":
                src = os.path.join(path,filename)
                dst = os.path.join(ajaxfilemanager.settings.file_directory,filepath)
            elif datatype == "folder":
                src = os.path.join(path,foldername)
                dst = os.path.join(ajaxfilemanager.settings.file_directory,folderpath,foldername)
            
            shutil.move(src, dst)
            return HttpResponse(datatype+" successfully moved")
        
def cp(request, datatype):
    class InvalidPath(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)


    try:
        path = request.GET['path']
        if datatype == "file":
            filepath = request.GET["filepath"]
            filename = request.GET["filename"]
        elif datatype == "folder":
            folderpath = request.GET["folderpath"]
            foldername = request.GET["foldername"]
    
    except KeyError:
        return HttpResponse("No path exist")
    
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        if os.access(path, os.W_OK):
            if datatype == "file":
                src = os.path.join(path,filename)
                dst = os.path.join(ajaxfilemanager.settings.file_directory,filepath)
                shutil.copy(src,dst)
            
            elif datatype == "folder":
                src = os.path.join(path,foldername)
                dst = os.path.join(ajaxfilemanager.settings.file_directory,folderpath,foldername)
                copytree(src,dst)

            return HttpResponse(datatype+" successfully copied")
            
def rename(request,datatype):
    try:
        path = request.GET['path']
        if datatype == "file":
            filenewname = request.GET["filenewname"]
            filename = request.GET["filename"]
        elif datatype == "folder":
            foldernewname = request.GET["foldernewname"]
            foldername = request.GET["foldername"]
    
    except KeyError:
        return HttpResponse("No path exist")
    
    else:
        currentpath = path
        path = os.path.join(ajaxfilemanager.settings.file_directory,path)
        if os.access(path, os.W_OK):
            if datatype == "file":
                src = os.path.join(path,filename)
                dst = os.path.join(ajaxfilemanager.settings.file_directory,filenewname)
                os.rename(src,dst)
            
            elif datatype == "folder":
                src = os.path.join(path,foldername)
                dst = os.path.join(ajaxfilemanager.settings.file_directory,foldernewname)
                os.rename(src,dst)

            return HttpResponse(datatype+" successfully renamed")
            
            
def editfile(request):
    try: 
        path = request.POST['path']
        content = request.POST['content']
    except (KeyError):
        return HttpResponse("No path exist")
    else:
        with open(path,'w') as f:
            f.write(content)
            
        return HttpResponse("Successfull edited!")
