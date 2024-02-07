#!/usr/bin/python3
# coding=utf-8

from ..py3office import handler, pdf


def doit(fileInfo):
    print("")
    print("名称：" + fileInfo["name"])
    print("名称(only)：" + fileInfo["onlyname"])
    print("路径：" + fileInfo["path"])
    print("所在文件夹：" + fileInfo["folder"])


def listfileTest():
    handler.listFile("./", doit)


def getFilesTest():
    files = handler.getFiles("./data/1月/张三/劳动合同文件夹")
    print(files)


def doit2(folderInfo):
    files = handler.getFiles(folderInfo["path"])
    if len(files) > 0:
        print("文件夹路径：" + folderInfo["path"])
        return True


def listFolderTest():
    handler.listFolder("./data/source", doit2)


def printListTest():
    def getName(name, pages):
        handler.printList(pages)
        return name

    pdf.toWord("./data/demo.pdf", "./data", getName)


def copyTest():
    error = handler.copy("./data/1月/李四/身份证.jpg", "./data/example/value/demo3.jpg")
    if error:
        print("copy 失败")
        print(error)
