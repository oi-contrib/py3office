# OCR相关操作

> v0.3.0 开始提供

提供和ocr相关的一些处理方法。

```python
from py3office import ocr
```

## toTexts

获取图片的文本内容：

```python
texts = ocr.toTexts(imgUrl)
```

返回的内容是一个列表。
