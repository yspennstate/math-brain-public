import importlib, json, platform
from datetime import datetime
print(datetime.now().astimezone().isoformat())
print(platform.python_version())
for name in ['mpmath','numpy','scipy','sympy']:
    try:
        mod=importlib.import_module(name)
        print(name,mod.__version__)
    except ImportError:
        print(name,'unavailable')
