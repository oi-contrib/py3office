#!/usr/bin/python3

from py3office import handler


def doit(fileInfo):
    print("")
    print(fileInfo["path"])
    print(fileInfo["folder"])


handler.listFile("./", doit)
