##### Flask Restful Application


>>> mkdir .env
>>> cd .env
>>> python -m venv web 
>>> ./env/web/Script/activete 
>>> pip3 install -r requirements.txt
---

>>> python migrate db init 
>>> python migrate db migrate 
>>> python migrate db update


--- 

>>> python main.py

--- 
```
├─core                      // 核心代码区域
├─define                    // 配置与文档
│  ├─config                 // 配置
│  ├─document               // 文档
├─interface                 // 接口与逻辑
│  ├─params                 // 参数
│  ├─resource               // 接口
├─log                       // 日志
├─migrations                
│  ├─versions
├─orm                       // ORM
│  ├─model                  // 模板
├─tasks                     // 任务工作区
└─utils                     // 实用工具

// 暂定这些目录，后面还会陆续追加

```
##### API Document
```python

defaultJson = {
    # Json 方式请求。
    # TODO:数组渲染有一些问题。
    # type, default, description
    "name": (fields.Integer, 1, "这是一个INT"),
    "list": [(fields.String, "nihao", "这是一个字符串")],
    "json": {
        "your": (fields.String, "nihao", "这是一个字符串")
    }
}
defaultParams = {
    # 请求参数
    # (_type, default, helper, required, location)
    # location 包括: header, args, form, cookies, values
    # location 可以设置为数组 ["headers", "args"]
    "name":         (int, 1, "这是一个整型", True, "values"),
    "uri":          (str, "nihao",  "这是一个字符串", True, "args"),
    "uri_prefix":   (str, "nihao",  "这是一个不必要的参数", False, "values"),
}

```


