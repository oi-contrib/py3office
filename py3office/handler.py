#!/usr/bin/python3

import os


def listFile(folder, callback):
    list = os.listdir(folder)
    for name in list:
        fullpath = os.path.join(folder, name)
        if os.path.isdir(fullpath):
            listFile(fullpath, callback)
        else:
            callback({"path": fullpath, "folder": folder})


def printList(input):
    for index in range(len(input)):
        print(f"[{index}] {input[index]}")
