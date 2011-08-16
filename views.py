# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import ajaxfilemanager
import os
import subprocess

def findpath(path):
    above = path[::-1]
    above_int = above.find("/")
    above_pp = above.split(above[above_int])
    above_pp.remove(above_pp[0])
    output = ""
    for tail in above_pp:
        output += "/"+tail

    above = output[::-1]
    return above



def upload(request):
    return render_to_response('ajaxfilemanager/upload.html', { 'ajaxfilemanager': ajaxfilemanager  })

def index(request):
    try:
        path = request.REQUEST['path']
        currentpath = path
    except (KeyError):
        return HttpResponseRedirect("/ajaxfilemanager/?path=base::")
    else:        
        above = findpath(path)
        path = path.replace("base::", ajaxfilemanager.settings.file_directory)
        resultdirlist = []        
        filelist = []
        filenames = []
        mimetypes = []        
        dirlist = os.listdir(path)
        for item in dirlist:
            if item.find(".") == -1:
                resultdirlist.append(item)
            else:
                filelist.append(item)
                filenames.append(item)
        
        for item in filelist:
            if item.find(".html") != -1 or item.find(".htm") != -1:
                mimetypes.append("text/html")
            elif item.find(".css") != -1:
                mimetypes.append("text/css")
            elif item.find(".js") != -1:
                mimetypes.append("text/javascript")            
            else:            
                mime = subprocess.Popen("cd "+path+";/usr/bin/file -i '"+item+"'", shell=True, stdout=subprocess.PIPE).communicate()
                mime = mime[0].split(";")
                mime = mime[0].split(":")
                mimetypes.append(mime[1])
        

        for i in range(len(filelist)):
            filelist[i] += " - ["+mimetypes[i]+"]"    
            

        return render_to_response('ajaxfilemanager/index.html', { 'ajaxfilemanager': ajaxfilemanager, 'resultdirlist': resultdirlist, 'filelist': filelist, 'currentpath': currentpath, 'path': path, 'above': above, 'filenames': filenames })


def handlefiles(request):
    if request.method == 'POST':
        output = "Artist: " + request.POST["artist"] + "<br />Album: " + request.POST["album"] + "<br />Year: " + request.POST["year"]
        if 'file' in request.FILES:
            file = request.FILES["file"]
            filename = file["filename"]

            fd = open('%s/%s' % (ajaxfilemanager.settings.file_directory, filename), 'wb')
            fd.write(file['content'])
            fd.close()
            output += "<br />Format: " + file['content-type']
     
            return HttpResponse(output)

def newfolder(request, folder):
    try:
        path = request.GET['path']
    except (KeyError):
        return HttpResponse("No path exist")
    else:
        currentpath = path
        path = path.replace("base:", ajaxfilemanager.settings.file_directory)    
        if os.access(path, os.W_OK):
            os.chdir(path)
            os.mkdir(folder)
            return HttpResponse("Folder successfully created")


def rmfile(request):
    try:
        path = request.GET['path']
    except (KeyError):
        return HttpResponse("No path exist")
    else:
        currentpath = path
        path = path.replace("base::", ajaxfilemanager.settings.file_directory) 
        if os.access(path, os.W_OK):
            os.chdir(path)
            os.remove(request.REQUEST['file'])
            return HttpResponse("File successfully deleted");        

def rmfolder(request):
    try:
        path = request.GET['path']
    except (KeyError):
        return HttpResponse("No path exist")
    else:
        currentpath = path
        path = path.replace("base::", ajaxfilemanager.settings.file_directory) 
        if os.access(path, os.W_OK):
            os.chdir(path)
            os.rmdir(request.REQUEST['folder'])
            return HttpResponse("Folder successfully deleted"); 
        

    
            

    
