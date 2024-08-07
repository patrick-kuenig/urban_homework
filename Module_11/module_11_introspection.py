import inspect
from pprint import pprint


def introspection_info(obj):
    result = dict()
    result['Type'] = type(obj).__name__
    result['Methods'] = [method for method in dir(obj) if callable((getattr(obj, method)))]
    result['Attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    result['From module'] = inspect.getmodule(obj)
    return result


number_info = introspection_info(42)
pprint(number_info)
