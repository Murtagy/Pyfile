%from lib import ls_dir, gen_button
%DIRS, FILES = ls_dir(path)

% include('header')
%include('tools/dir_tools')
    %for i in DIRS:
        <p><b>{{i}}</b></p>
        {{!gen_button(value=i, name='dir', action='/open')}}    
    %end

    %for i in FILES:
        <p>{{i}}</p>
        {{!gen_button(value=i, name='file', action='/open')}}    
    %end

%include('footer')