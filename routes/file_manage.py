from main.app import app
from .security import check_login
import bottle
import main.lib  as lib 
import os 


#  BASIC FILE MANAGEMENT
@app.route('/open', method='get')
@check_login
def _open(path=None):
    path_d = None
    path_f = None
    path = path or bottle.request.query.get('path')
    if path:
        if os.path.isdir(path):
            path_d = path
        if os.path.isfile(path):
            path_f = path
    file = path_f or bottle.request.query.get('file')
    _dir = path_d or bottle.request.query.get('dir')
    if file:
        file_name = file
        file_type = 'lang-' + file_name.split('.')[-1]
        file = lib.cat_file(file)
        return render_file(file, file_name, file_type)
    if _dir:
        return bottle.template('main', path=_dir)
    return 'UNKNOWN'

@app.route('/download', method='get')
@check_login
def download():
    file = bottle.request.query.get('file')
    folder,file = os.path.split(file)
    return bottle.static_file(file, root=folder, download=file)

@app.route('/upload', method='POST')
@check_login
def do_upload():
    path = bottle.request.forms.get('path')

    file_upload = bottle.request.files.get('file')
    file_create = bottle.request.forms.get('file')
    dir_create = bottle.request.forms.get('dir')
    if file_upload:
        file_upload.save(path, overwrite=True) # appends upload.filename automatically
    if file_create:
        file_create = os.path.join(path, file_create)
        open(file_create,'a').close()
    if dir_create:
        dir_create= os.path.join(path,dir_create)
        os.mkdir(dir_create)
    return _open(path)

@app.route('/static/<path:path>')
@check_login
def static(path):
    return bottle.static_file(path, root='./static/')

def render_file(file_content, file_name, file_type, path='.'):
    return bottle.template('file',
                           content=file_content,
                           file_name=file_name,
                           file_type=file_type
                           )