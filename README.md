# Ajaxfilemanager

<table>
<tbody>
<tr>
<td>Version</td><td>0.2</td>
</tr>
<tr>
<td>Built with</td><td>Django 1.5 - Python 2.7.3</td>
</tr>
</table>
This ajaxfilemanager based on *python-django*!

Released with **Django 1.5**

## Install

It's easy:

1. Copy the complete App<sup><a href="#1">[1]</a></sup> folder into your project folder
2. Add the App to the INSTALLED_APPS
3. Insert the path to the "template" directory in the "ajaxfilemanager" folder into your TEMPLATE_DIRS
4. Add a URL-Rule to your urls.py in the django-site-root (Example: url(r^'ajaxfilemanager/', include('ajaxfilemanager.urls')), )
5. Ensure that you activate 'staticfiles'
6. Edit the 'settings.py' in the ajaxfilemanager directory and import YOUR global project settings. 
 
Finish!

## Usage

Serve to 'http://your.server.com/ajaxfilemanager'. You will be 
redirect to 'http://your.server.com/ajaxfilemanager/?path='.
The Path Syntax in the URL is simple. Nothing is the ajaxfm_media_root. 
The rest is the original path. But if you enter *?path=/* you will be 
redirect to *ajaxfilemanager/noroot* and get a message like **You are 
not root, please go back.** because "/" is basically the root directory
of your server. This has a technical reason of *os.path.join*

Currently you can access the uploader 
with "http://your.server.com/ajaxfilemanager/upload" this is still a
security leak, because anyone can upload without have access to the
filemanager. 

## TODO


* "Access denied" for direct usage of /upload.
* Watch the media directory for changes and add them immediately to page.
* Authentication for access to ajaxfm   
   
**<a name="1">[1]</a>** Exactly called *ajaxfilemanager* and in this directory you find *views.py*, *models.py*, and *urls.py*
