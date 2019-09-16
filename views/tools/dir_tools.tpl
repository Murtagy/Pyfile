
%include('tools/back')
*
<img src="static/images/newfile.jpg" 
    onclick="show('file')" alt="File" width=30 height=30 style="margin-right: 5px;" title="Создать новый файл"> 
<img src="static/images/newfolder.png" 
    onclick="show('dir')" alt="Folder" width=30 height=30 title="Создать новую папку">
* 
<hr>
%include('forms/make_dir')
%include('forms/make_file')