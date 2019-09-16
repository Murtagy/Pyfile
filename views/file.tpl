% include('header')
%include('tools/file_tools', path=file_name)
%type = file_type
<pre><code class="{{type}}">
%for i in content.splitlines():
{{i}}
%end
</code></pre>
%include('footer') 