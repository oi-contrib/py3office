#!/usr/bin/python3
# coding=utf-8

from ..py3office import handler, ocr


def toTextsTest():
    handler.printList(ocr.toTexts("./data/demo.png"))


sourcePath = "./data/source"
targetPath = "./data/target"


def doit(fileInfo):
    idcardInfo = ocr.toTexts(fileInfo["path"])
    # handler.printList(idcardInfo)
    handler.copy(
        fileInfo["path"],
        fileInfo["folder"].replace(sourcePath, targetPath)
        + "/"
        + idcardInfo[1]
        + ".jpg",
    )


def renameTest():
    handler.listFile(sourcePath, doit)
