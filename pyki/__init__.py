# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Flask
import os

app = Flask(__name__)
#here = os.path.abspath(os.path.dirname(__file__))
here = os.getcwd()

def linkify(parent, name):
    relpath = os.path.join(parent, name)
    return '<a href="{relpath}">{name}</a>'.format(relpath=relpath, name=name)

@app.route('/', defaults={'relpath': ''})
@app.route('/<path:relpath>')
def parse_path(relpath):
    fullpath = os.path.join(here, relpath)
    msg = fullpath + "<p>"
    if os.path.isdir(fullpath):
        msg +='<br>'.join([linkify(relpath, f) for f in os.listdir(fullpath)])
    elif os.path.isfile(fullpath):
        with open(fullpath, 'r') as f:
            text = f.read()
            for org, rep in {'"': '&quot;', '<': '&lt;', '>': '&gt;', '&': '&amp;'}.items():
                text = text.replace(org, rep)
            msg += '<textarea cols=80 rows=50>' + text + '</textarea>'
    else:
        msg += fullpath + " not found!"
    return msg

if __name__ == '__main__':
    app.run()
