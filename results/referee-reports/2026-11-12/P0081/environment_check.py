"""Record availability of the numerical libraries used for this audit."""
import importlib.util
print({m: bool(importlib.util.find_spec(m)) for m in ['numpy', 'scipy', 'sympy', 'mpmath']})
