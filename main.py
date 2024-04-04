#!/usr/bin/python3
# coding=utf-8

from src.test import handlerTest, pdfTest, demo1Test, ocrTest

if __name__ == "__main__":

    # handler 基本辅助相关
    # handlerTest.getFilesTest()
    # handlerTest.listfileTest()
    # handlerTest.listFolderTest()
    # handlerTest.printListTest()
    # handlerTest.copyTest()

    # demo1Test.test()

    # PDF文件相关操作
    # pdfTest.toImageTest()
    # pdfTest.toImagesTest()
    # pdfTest.toWordTest()
    # pdfTest.logInfoTest()

    # OCR相关操作
    # ocrTest.toTextsTest()
    ocrTest.renameTest()
