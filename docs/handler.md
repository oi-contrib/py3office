# handler 基本辅助相关

提供一些辅助方法的模块，比如文件遍历等。

```python
from py3office import handler
```

## printList

打印列表：

```python
handler.printList(list)
```

## listFile

遍历文件夹folder下的所有文件：

```python
handler.listFile(folder, callback)
```

callback有一个字典类型的参数fileInfo，格式如下：

```python
{
    "name": <文件名称> , # v0.2.0 开始提供
    "onlyname": <仅文件名> , # v0.2.0 开始提供
    "path": <文件路径> ,
    "folder": <当前文件所在文件夹>
}
```

## getFiles

> v0.2.0 开始提供

获取指定文件夹下的所有子文件：

```python
files = handler.getFiles(folder)
```

返回的files是一个列表类型，格式如下：

```python
[{
    "name": <文件名称> ,
    "onlyname": <仅文件名> ,
    "path": <文件路径> ,
    "folder": <当前文件所在文件夹>
},...]
```

## listFolder

> v0.2.0 开始提供

遍历文件夹folder下的所有文件夹：

```python
handler.listFolder(folder, callback)
```

callback有一个字典类型的参数folderInfo，格式如下：

```python
{
    "name": <文件夹名称> ,
    "path": <文件夹路径> ,
    "folder": <当前文件夹所在文件夹>
}
```

此外，callback还可以有一个布尔类型的返回值，默认返回False，如果返回True，表示不再进一步遍历此文件夹的子文件夹。

## copy

> v0.2.0 开始提供

复制文件或文件夹：

```python
error = handler.listFolder(source, target)
```

如果返回成功，error就是False，否则就是一个字符串，描述错误原因。

## write

> v0.2.0 开始提供

文本写入文件：

```python
handler.write(target, txt)
```
