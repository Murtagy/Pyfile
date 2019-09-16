%from lib import gen_button

%include('tools/back')
<a href="/download?file={{path}}"><img src="static/images/download.png" 
    alt="Folder" width=30 height=30 ></a>
<img src="static/images/upload.png" 
    onclick="show('upload')" alt="Folder" width=30 height=30 >
%include('forms/upload')
<hr>


