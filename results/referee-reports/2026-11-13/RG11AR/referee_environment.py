"""Read-only dependency/resource probe; no subprocesses or external writes."""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
import importlib.util
import platform
import resource
import signal
signal.alarm(60)
print("Python", platform.python_version())
for name in ("numpy", "scipy", "sympy", "cvxpy", "clarabel", "scs"):
    spec = importlib.util.find_spec(name)
    print(name, "available" if spec else "absent")
if importlib.util.find_spec("cvxpy"):
    import cvxpy
    print("cvxpy solvers:", cvxpy.installed_solvers())
print("peak RSS (bytes on macOS):", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
