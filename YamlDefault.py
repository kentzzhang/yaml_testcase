#encoding:utf-8

# 默认值
DEFAULT_VALUES = {
    "auth": {},
    "url": "http://api.91wasai.com/v2",
    "method": "POST",
    "action": "/",
    "header": {
        "Content-Type": "application/json"
    }
}

# INT类型的默认值
VARIABLE_INT = [0, 1, 99]

# String类型的默认值
VARIABLE_STRING = ["", "NULL", "none", "TestName"]

# Bool类型的默认值
VARIABLE_BOOL = [False, True]
