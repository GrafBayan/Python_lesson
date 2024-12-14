import inspect

def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [att for att in dir(obj) if not callable(getattr(obj, att)) and not att.startswith('__')]
    info['methods'] = [meth for meth in dir(obj) if callable(getattr(obj, meth)) and not meth.startswith('__')]
    info['module'] = getattr(obj, '__module__', None)
    if isinstance(obj, (list, dict, set, str)):
        info['length'] = len(obj)
    return info


class Test:
    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b
    def sum(self):
        c = self.a + self.b
        return c


t1 = Test(1, 2)

print(introspection_info(42))
print(introspection_info(t1))