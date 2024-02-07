#!/usr/bin/python3

import os
import fitz
import re
from pdf2docx import Converter
from . import handler


# 打印pdf内容
def logInfo(file_path, isSingle=True):
    print(f"\n文件：{file_path}")

    # 打开pdf
    doc = fitz.open(file_path)

    # pdf文件名
    name = re.sub(r"\.pdf$", "", os.path.basename(file_path))
    print(f"\n> [name]文件名 = '{name}'")

    # 总页数
    total = doc.page_count
    print(f"\n> [total]总页数 = {total}")

    if isSingle:
        for index in range(total):
            print(f"\n> [index]当前页序号 = {index}")
            print(f"\n> [texts]当前页面内容如下：")

            # 读取内容
            page = doc.load_page(index)
            texts = page.get_text("text").split("\n")

            handler.printList(texts)

    else:
        pages = []
        for index in range(total):
            # 读取内容
            page = doc.load_page(index)
            texts = page.get_text("text").split("\n")
            pages.append(texts)
        print(f"\n> [pages]当前文件内容如下：")
        handler.printList(pages)

    # 关闭pdf
    doc.close()


# 转图片
def toImage(file_path, png_path, getName=False):
    print(f"\n文件：{file_path}")

    # 打开pdf
    doc = fitz.open(file_path)

    # pdf文件名
    name = re.sub(r"\.pdf$", "", os.path.basename(file_path))

    # 总页数
    total = doc.page_count

    for index in range(total):
        # 读取内容
        page = doc.load_page(index)
        texts = page.get_text("text").split("\n")

        zoom = 3.0  # 值越大，分辨率越高，文件越清晰
        trans = fitz.Matrix(zoom, zoom).prerotate(0)

        pm = page.get_pixmap(matrix=trans, alpha=False)

        # 建立目标文件夹
        if not os.path.exists(png_path):
            os.makedirs(png_path)

        # 图片名称
        filename = name
        if getName:
            filename = getName(name, texts, index, total)
        elif total > 1:
            filename = name + "_" + str(index)

        # 图片路径
        index = 1
        save_path = os.path.join(png_path, "%s.jpg" % filename)
        while os.path.exists(save_path):
            save_path = os.path.join(png_path, f"{filename}({str(index)}).jpg")
            index += 1
        print(save_path)

        # 保存
        pm.save(save_path)

    # 关闭pdf
    doc.close()


# 转word
def toWord(file_path, word_path, getName=False):
    print(f"\n文件：{file_path}")

    # 打开pdf
    doc = fitz.open(file_path)

    # pdf文件名
    name = re.sub(r"\.pdf$", "", os.path.basename(file_path))

    # 总页数
    total = doc.page_count

    # pdf内容
    pages = []
    for index in range(total):
        # 读取内容
        page = doc.load_page(index)
        texts = page.get_text("text").split("\n")
        pages.append(texts)

    # 关闭pdf
    doc.close()

    # word名称
    filename = name
    if getName:
        filename = getName(name, pages)

    # word路径
    index = 1
    save_path = os.path.join(word_path, "%s.docx" % filename)
    while os.path.exists(save_path):
        save_path = os.path.join(word_path, f"{filename}({str(index)}).docx")
        index += 1

    cv = Converter(file_path)
    cv.convert(save_path)
    cv.close()
