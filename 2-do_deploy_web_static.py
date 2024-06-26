#!/usr/bin/python3
"""web_static files."""

from fabric.api import local
from fabric.api import run
from fabric.api import put
from fabric.api import env
from datetime import datetime
import os

env.hosts = [
    '52.73.249.3',
    '54.146.71.171'
]
env.user = "ubuntu"


def do_deploy(archive_path):
    """the."""
    if not os.path.isfile(archive_path):
        return False

    if put(archive_path, "/tmp/").failed is True:
        return False
    archive = archive_path.split("/")[-1]
    arch_name = archive.split(".")[0]
    re_path = "/data/web_static/releases/{}/".format(arch_name)
    if run("mkdir -p {}".format(re_path)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C {}".format(archive, re_path)).failed is True:
        return False

    if run("rm /tmp/{}".format(archive)).failed is True:
        return False
    pth = "/data/web_static/releases"
    if run("mv -f {}/{}/web_static/* {}/{}".
           format(pth, arch_name, pth, arch_name)).failed is True:
        return False

    if run("rm -rf {}/{}/web_static".format(pth, arch_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s {} /data/web_static/current".format(re_path)).failed is True:
        return False
    print("New version deployed!")
    return True
