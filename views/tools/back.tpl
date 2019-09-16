%import os
%import bottle 

%path_back, _ = os.path.split(path)

%if path=='tech':
%path_back = bottle.request.query.get('path')
%end

<a href="/open?dir={{path_back}}"> <img src="static/images/back.png" 
     alt="Back" width=30 height=30 style="margin-right: 5px" ></a>