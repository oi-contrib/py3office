#!/usr/bin/python3

from setuptools import setup

readmeFile = open("README.md", "r", encoding="utf-8")
long_description = readmeFile.read().replace(
    "./docs/", "https://github.com/fragement-contrib/py3office/blob/master/docs/"
)
readmeFile.close()

# https://setuptools.pypa.io/en/latest/setuptools.html

setup(
    name="py3office",
    version="0.2.0",
    description="提供python3版本的自动化办公常用处理方法",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zxl20070701",
    author_email="1904314465@qq.com",
    maintainer="zxl20070701",
    maintainer_email="1904314465@qq.com",
    package_dir={"": "src"},
    packages=["py3office"],
    url="https://github.com/fragement-contrib/py3office",
    license="MIT",
    keywords=["pdf", "office", "python3"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["PyMuPDF>=1.23.16", "pdf2docx>=0.5.8"],
)
