#!/usr/bin/python3
"""Fabric script"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")

        time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("tar -cvf versions/web_static_{}.tgz web_static".format(time))

        return "versions/web_static_{}.tgz".format(time)
    except Exception:
        return None
