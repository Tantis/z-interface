from define.document.bases import DocumentFormat
from utils.fn import trace_calls


if __name__ == '__main__':

    new = DocumentFormat(_type=int, _value=1, _description="这是一个测试数据")

    _renew = DocumentFormat(
        _type=list, _value=[new, new], _description="这是一个测试数据")
    par = _renew.json()
    print(par)
    import ipdb
    ipdb.set_trace()

    print(new)
    print(isinstance(new, DocumentFormat))
