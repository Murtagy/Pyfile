import json
import os
import datetime
from bottle import template

def ls_dir(dir):
    dirs = []
    files = []
    for file_object in os.listdir(dir):
        file_object = os.path.join(dir, file_object)
        if os.path.isdir(file_object):
            dirs.append(file_object)
        if os.path.isfile(file_object):
            files.append(file_object)
    dirs.sort()
    files.sort()
    return dirs, files 


def cat_file(file):
    with open(file, 'r') as f:
        return f.read()

   
def gen_button(text='INSPECT', value='', name='', action='', onclick=''):
    if len(name)>0:
        name = f'name="{name}"'
    if len(value)>0:
        value = f'value="{value}"'
    if len(action)>0:
        action = f'action="{action}"'
    if len(onclick)>0:
        onclick = f'onclick="{onclick}"'

    btn = f"""
    <form {action}><button {name} {value} {onclick}> {text} </button></form>
    """
    return btn


if __name__ == '__main__':
    pass


