#!/usr/bin/python3
# Create a tar archive from web_static folder

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Create a tar archive from web_static folder """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(path), capture=True)
    if result.failed:
        return None
    return path
