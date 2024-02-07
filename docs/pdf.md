# PDF文件相关操作

提供和pdf相关的一些处理方法。

```python
from py3office import pdf
```

## logInfo

> v0.2.0 开始提供

打印pdf内容：

```python
pdf.toImage(pdfUrl, isSingle=True)
```

其中isSingle表示是否一页页`texts`内容打印，默认True，如果设置为False则按照一个文件`pages`打印。

## toImage

把pdf转成图片：

```python
pdf.toImage(pdfUrl, targetFolder)
```

你还可以传递一个函数来自定义图片名称：

```python
# 文件名、当前页内容、页序号、页数
def getName(name, texts, index, total):
    return <新的名称>

pdf.toImage(pdfUrl, targetFolder, getName)
```

## toWord

> v0.2.0 开始提供

把pdf转成word：

```python
pdf.toWord(pdfUrl, targetFolder)
```

你还可以传递一个函数来自定义word名称：

```python
# 文件名、当前文件内容
def getName(name, pages):
    return <新的名称>

pdf.toWord(pdfUrl, targetFolder, getName)
```
