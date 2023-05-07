#!/usr/bin/python3
# clean up fabfile

from os import listdir
from fabric.api import *

env.host = ["18.209.225.63", "100.25.17.109"]
env.user = "ubuntu"


def do_clean(number=0):
    """
        Clean outdated archives
    """

    number = 1 if int(number) == 0 else int(number)
    # get all archives list sorted in asc order
    archives = sorted(listdir("versions"))
    # remove archives not to delete from the list of archives
    [archives.pop() for i in range(number)]
    # Change local current directory with lcd
    with lcd("versions"):
        # remove all outdated archives locally
        [local("rm ./{}".format(archive)) for archive in archives]
    # change remote current directory
    with cd("/data/web_static/release"):
        archives = run("ls -tlr").split()
        # ensure to get only web_static archives
        archives = \
            [archive for archive in archives if "web_static_" in archive]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(archive)) for archive in archives]
