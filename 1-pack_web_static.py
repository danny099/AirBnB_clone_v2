#!/usr/bin/python3
# task 1
from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
    """do pack"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    f = 'versions/web_static_' + date + '.tgz'
    if not path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local('tar -cvzf {} web_static'.format(f)).failed:
        return None
    return f
