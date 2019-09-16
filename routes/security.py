#SECURITY
import functools


from main.app import app
from main.auth import USER 
from main.auth import PASS 
from main.auth import AUTH 
import bottle
import os

@app.route('/login', method=['get','post'])
def login():
    key = bottle.request.get_cookie('AUTH','0')
    if key == AUTH:
        return bottle.redirect('/')
    if bottle.request.forms.get('USER') == USER and \
       bottle.request.forms.get('PASS') == PASS:
        bottle.response.set_cookie('AUTH',AUTH)
        return bottle.redirect('/')
    return bottle.template('login')  

def check_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args,**kwargs)
        _auth = bottle.request.get_cookie('AUTH')
        if _auth != AUTH:
            return bottle.redirect('/login')
        return ret
    return wrapper
