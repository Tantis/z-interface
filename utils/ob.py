

class model(dict):
    """简洁版MODEL
    >>> conf = model()
    >>> conf = {'dd': {'cc': {'ee': {'xx' : 'test'}}}}, {'a': 'b'}
    >>> print(conf.dd.cc.ee.xx)
    """

    def __init__(self, *args, **kwarg):

        super(model, self).__init__(*args, **kwarg)
        for __attrbute in self.keys():
            setattr(self, __attrbute, self[__attrbute])

    def __dir__(self):

        _dir = list(self.keys())
        return _dir

    def __values_to_model(self, value):
        if isinstance(value, (list, tuple, set)):
            _aval = []
            for _val in value:
                if isinstance(_val, dict):
                    _val = model(_val)
                elif isinstance(_val, (list, tuple, set)):
                    _val = self.__values_to_model(_val)
                _aval.append(_val)
            _aval = value.__class__(_aval)
            return _aval
        elif isinstance(value, dict):
            value = model(value)
        return value

    def __setattr__(self, key, value):
        try:
            if not hasattr(self, key):
                self[key] = value
                value = self.__values_to_model(value)
        except Exception as e:
            print(type(key), value)
            raise(e)

        super(model, self).__setattr__(key, value)

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        elif key in self.keys():
            return self.get(key)
        else:
            return super(model, self).__getitem__(key)


if __name__ == "__main__":
    dicts = {}
    z = model()
    z.code = 123
    z.diction = model({"zxc": 2})
    print("code" in dir(z))
    print(z.code, z.diction, z.diction.zxc)
    print(dir(z.diction))
    import ipdb
    ipdb.set_trace()
