#!/usr/bin/python3

from cnocr import CnOcr

ocr = CnOcr()


# 图片变成列表
def toTexts(file_path):
    texts = ocr.ocr(file_path)
    result = []

    for index in range(len(texts)):
        result.append(texts[index]["text"])

    return result
