#!/usr/bin/python3
# coding=utf-8

from ..py3office import pdf, handler

"""
打印信息
"""


def logInfoTest():
    pdf.logInfo("./data/demo.pdf", False)
    # pdf.logInfo("./data/demo.pdf", True)


"""
PDF转图片
"""


def getName(name, texts, index, total):
    print(name, texts, index, total)
    return name + "_new"


def toImageTest():
    pdf.toImage("./data/demo.pdf", "./data", getName)


sourcePath = "./data/demo"
targetPath = "./data/image"


def doit(fileInfo):
    if fileInfo["path"].endswith(".pdf"):

        def getName1(name, texts, index, total):
            filename = texts[1].replace(
                "姓名：",
                "",
            )
            if total > 1:
                return filename + "_" + index
            else:
                return filename

        def getName2(name, texts, index, total):
            if total > 1:
                return name + "_" + str(index)
            else:
                return name

        pdf.toImage(
            fileInfo["path"],
            fileInfo["folder"].replace(sourcePath, targetPath),
            getName2,
        )


def toImagesTest():
    handler.listFile(sourcePath, doit)


"""
PDF转Word
"""


def getName3(name, pages):
    print(name, pages)
    return name


def toWordTest():
    pdf.toWord("./data/demo.pdf", "./data", getName3)
