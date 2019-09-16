from main.app import app
from .security import check_login
import bottle

#  BASIC FILE MANAGEMENT
@app.route('/')
@check_login
def index():
    return bottle.template('main', path='.')