#!/usr/bin/python3

import os
import fitz
import re


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
        save = os.path.join(png_path, "%s.jpg" % filename)
        while os.path.exists(save):
            save = os.path.join(png_path, f"{filename}({str(index)}).jpg")
            index += 1
        print(save)

        # 保存
        pm.save(save)

    # 关闭pdf
    doc.close()
