<form id="upload" style="display: none;" action="/upload" method="post" enctype="multipart/form-data">
  Select a file: <input type="file" name="file" />
  <input type="hidden" name="path" value="{{file_name}}" />
  <input type="submit" value="Start upload" />
</form>