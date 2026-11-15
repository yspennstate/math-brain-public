"""Small dependency/resource check; creates no files outside the working folder."""
import importlib
import os
import resource
import sys

try:
    os.nice(10)
except PermissionError:
    print('nice(10) denied by sandbox; only small, single-process checks will run')
print('Python', sys.version.split()[0])
for name in ['numpy', 'scipy', 'mpmath']:
    module = importlib.import_module(name)
    print(name, module.__version__)
print('rss_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
