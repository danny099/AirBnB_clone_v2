#!/usr/bin/python3
# task 2
from fabric.api import run, env, put
from os import path


env.hosts = ["34.74.99.82", "3.90.104.161"]


def do_deploy(archive_path):
    """deploy"""
    if not path.isfile(archive_path):
        return False

    file_ = archive_path.split("/")[-1]
    name = file_.split(".")[0]
    tmp = "/tmp/{}".format(file_)
    data = "/data/web_static/releases/{}/".format(name)
    current = "/data/web_static/current"

    if put(archive_path, tmp).failed:
        return False
    if run("rm -rf {}".format(data)).failed:
        return False
    if run("mkdir -p {}".format(data)).failed:
        return False
    if run("tar -xzf {} -C {}".format(tmp, data)).failed:
        return False
    if run("rm {}".format(tmp)).failed:
        return False
    if run("mv {}web_static/* {}".format(data, data)).failed:
        return False
    if run("rm -rf {}web_static".format(data)).failed:
        return False
    if run("rm -rf {}".format(current)).failed:
        return False
    if run("ln -s {} {}".format(data, current)).failed:
        return False
    print("New version deployed!")

    return True
