#!/usr/bin/python3

from py3office import pdf
from py3office import handler

# print(pdf)

# def getName(name, texts, index, total):
#     print(name, texts, index, total)
#     return name+"_new"
# pdf.toImage("./data/demo.pdf","./data",getName)
# pdf.toImage("./data/参保证明-1.10/江西/饶群-社保证明.pdf", "./data/参保证明-1.10/江西")

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


handler.listFile(sourcePath, doit)
