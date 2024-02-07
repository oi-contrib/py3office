#!/usr/bin/python3
# coding=utf-8

from ..py3office import handler

"""
【用例】文件夹内容筛选
"""

sourcePath = "./data/source"
targetPath = "./data/result"

filelist = ["身份证", "学位证", "毕业证"]
foldername = "劳动合同"

report = ""


def doit(folderInfo):
    global report
    files = handler.getFiles(folderInfo["path"])
    if len(files) > 0:
        report = report + "\n\n>>> " + folderInfo["path"]

        filemap = {}
        for item in files:
            filemap[item["onlyname"]] = item

        for filename in filelist:
            if filename in filemap:
                handler.copy(
                    filemap[filename]["path"],
                    filemap[filename]["path"].replace(sourcePath, targetPath),
                )
            else:
                report = report + "\n - 缺失《" + filename + "》"

        files2 = handler.getFiles(folderInfo["path"] + "/" + foldername)
        if len(files2) < 1:
            report = report + "\n - 缺失《" + foldername + "》"
        else:

            # 合同需要的是前2页和最后一页
            needPages = [1, 2, len(files2)]
            needPagesResult = [False, False, False]
            for item2 in files2:
                for index in range(len(needPages)):
                    if item2["onlyname"] == str(needPages[index]):
                        handler.copy(
                            item2["path"],
                            item2["path"].replace(sourcePath, targetPath),
                        )
                        needPagesResult[index] = True
            for index in range(len(needPagesResult)):
                if not needPagesResult[index]:
                    report = (
                        report
                        + "\n - 缺失《"
                        + foldername
                        + "》第"
                        + str(index + 1)
                        + "页"
                    )

        return True


def test():
    handler.listFolder(sourcePath, doit)
    handler.write(
        "./data/report.txt", sourcePath + " 转 " + targetPath + " 生成日志\n" + report
    )
