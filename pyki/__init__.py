# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Flask
import os

app = Flask(__name__)
#here = os.path.abspath(os.path.dirname(__file__))
here = os.getcwd()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def parse_path(path):
    fullpath = os.path.join(here, path)
    if os.path.isdir(fullpath):
        return '<br>'.join(os.listdir(fullpath))
    elif os.path.isfile(fullpath):
        return fullpath + " is a file!"
    else:
        return fullpath + " not found!"

if __name__ == '__main__':
    app.run()
