#!/usr/bin/python3

import os
import shutil
import re


# 遍历文件夹folder下的所有文件
def listFile(folder, callback):
    list = os.listdir(folder)
    for name in list:
        fullpath = os.path.join(folder, name)
        if os.path.isdir(fullpath):
            listFile(fullpath, callback)
        else:
            callback(
                {
                    "name": name,
                    "path": fullpath,
                    "folder": folder,
                    "onlyname": re.sub(r"\.\w{1,}$", "", name),
                }
            )


# 获取指定文件夹下的所有子文件
def getFiles(folder):
    try:
        files = []
        list = os.listdir(folder)
        for name in list:
            fullpath = os.path.join(folder, name)
            if not os.path.isdir(fullpath):
                files.append(
                    {
                        "name": name,
                        "path": fullpath,
                        "folder": folder,
                        "onlyname": re.sub(r"\.\w{1,}$", "", name),
                    }
                )
        return files
    except Exception as error:
        # print(error)
        return []


# 遍历文件夹folder下的所有文件夹
def listFolder(folder, callback):
    list = os.listdir(folder)
    for name in list:
        fullpath = os.path.join(folder, name)
        if os.path.isdir(fullpath):
            if not callback({"name": name, "path": fullpath, "folder": folder}):
                listFolder(fullpath, callback)


# 打印列表
def printList(input, preStr=""):
    for index in range(len(input)):
        if type(input[index]) == list:
            printList(input[index], f"[{index}]")
        else:
            print(f"{preStr}[{index}] {input[index]}")


# 复制文件或文件夹
def copy(source, target):
    try:

        # 获取目标父文件或文件夹所在文件夹
        targetFolder = os.path.dirname(target)

        # 如果不存在，创建（不然会报错）
        if not os.path.exists(targetFolder):
            os.makedirs(targetFolder)

        # 复制文件夹
        if os.path.isdir(source):
            shutil.copytree(source, target)
        # 复制文件
        else:
            shutil.copy(source, target)
        return False
    except FileNotFoundError:
        return "未找到指定的文件或目录。"
    except PermissionError:
        return "没有足够的权限来访问该文件或目录。"
    except Exception as error:
        return "发生了其他错误：" + str(error)


# 文本写入文件
def write(filepath, txt):
    # 获取目标父文件或文件夹所在文件夹
    targetFolder = os.path.dirname(filepath)

    # 如果不存在，创建（不然会报错）
    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)

    with open(filepath, "w") as file:
        file.write(txt)
