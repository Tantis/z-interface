from flask_restplus import fields


defaultJson = {
    "name": (fields.Integer, 1, "这是一个名字程序"),
    "list": [(fields.String, "nihao", "这是一个名字程序")],
    "json": {
        "your": (fields.Integer, 1, "这是一个名字程序")
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

defaultResponse = {
    "status": (fields.Integer, 200, "这是一个名字程序"),
    "description": [(fields.String, "nihao", "这是一个名字程序")],
    "data": {
        "your": (fields.Integer, 1, "这是一个名字程序")
    }
}
