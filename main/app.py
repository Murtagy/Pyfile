#!/usr/bin/env python
# -*- coding: utf-8 -*-
import waitress 
import bottle 
from .lib import *
from .auth import *

bottle.DEBUG = True
app = bottle.Bottle()

#DEBUG 
@app.route('/debugGET', method='GET')
def debugGet():
    return 'GET'

@app.route('/debugPOST', method='POST')
def debugPost():
    print(bottle.request.json)
    return bottle.request.body

def main():
    waitress.serve(app, listen='*:44100')

if __name__ == '__main__':
    main()