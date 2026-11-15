"""Read-only dependency and resource information for this referee run."""
import importlib
import os
import time

print('Local time:', time.strftime('%Y-%m-%d %H:%M:%S %Z'))
print('Working directory:', os.getcwd())
for name in ['mpmath', 'numpy', 'scipy', 'sympy']:
    try:
        mod = importlib.import_module(name)
        print(name, mod.__version__)
    except ImportError:
        print(name, 'unavailable')
