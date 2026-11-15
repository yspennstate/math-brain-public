"""Run a small task with Windows resource limits and writes confined to this folder."""
import ctypes
from ctypes import wintypes
import os
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[name] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
os.environ["MATH_STRENGTH_NOLOG"] = "1"
os.environ["MATHBRAIN_RECALL_PROFILE"] = "0"
os.environ["MATH_RECALL_FAST"] = "0"
sys.dont_write_bytecode = True
# A recall must not load torch or start an encoder.
sys.modules["torch"] = None

class Basic(ctypes.Structure):
    _fields_ = [("process_time", ctypes.c_int64), ("job_time", ctypes.c_int64),
                ("flags", wintypes.DWORD), ("min_working", ctypes.c_size_t),
                ("max_working", ctypes.c_size_t), ("active", wintypes.DWORD),
                ("affinity", ctypes.c_size_t), ("priority", wintypes.DWORD),
                ("scheduling", wintypes.DWORD)]

class IO(ctypes.Structure):
    _fields_ = [(x, ctypes.c_uint64) for x in
                ("read_ops", "write_ops", "other_ops", "read_bytes", "write_bytes", "other_bytes")]

class Extended(ctypes.Structure):
    _fields_ = [("basic", Basic), ("io", IO), ("process_memory", ctypes.c_size_t),
                ("job_memory", ctypes.c_size_t), ("peak_process", ctypes.c_size_t),
                ("peak_job", ctypes.c_size_t)]

if os.name != "nt":
    raise RuntimeError("This launcher implements Windows limits only")
k = ctypes.WinDLL("kernel32", use_last_error=True)
k.GetCurrentProcess.restype = wintypes.HANDLE
k.CreateJobObjectW.restype = wintypes.HANDLE
k.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
k.SetPriorityClass.argtypes = [wintypes.HANDLE, wintypes.DWORD]
k.GetProcessAffinityMask.argtypes = [wintypes.HANDLE, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_size_t)]
k.SetProcessAffinityMask.argtypes = [wintypes.HANDLE, ctypes.c_size_t]
k.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
k.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
proc = k.GetCurrentProcess()
assert k.SetPriorityClass(proc, 0x4000), ctypes.get_last_error()  # BELOW_NORMAL
allowed, system = ctypes.c_size_t(), ctypes.c_size_t()
assert k.GetProcessAffinityMask(proc, ctypes.byref(allowed), ctypes.byref(system))
assert k.SetProcessAffinityMask(proc, allowed.value & -allowed.value)
job = k.CreateJobObjectW(None, None)
assert job, ctypes.get_last_error()
limits = Extended()
limits.basic.flags = 0x100 | 0x2  # PROCESS_MEMORY | PROCESS_TIME
limits.basic.process_time = 1200 * 10_000_000
limits.process_memory = 768 * 1024 * 1024
assert k.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)), ctypes.get_last_error()
assert k.AssignProcessToJobObject(job, proc), ctypes.get_last_error()

def inside(path):
    if isinstance(path, int):
        return True
    try:
        Path(os.fsdecode(path)).resolve().relative_to(ROOT)
        return True
    except (ValueError, TypeError):
        return False

def guard(event, args):
    if event == "open":
        path, mode, flags = args
        writing = ((isinstance(mode, str) and any(c in mode for c in "wax+")) or
                   flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writing and not inside(path):
            raise PermissionError("External write blocked: " + str(path))
    if event in ("os.mkdir", "os.remove", "os.rmdir", "os.chmod", "os.utime"):
        if not inside(args[0]):
            raise PermissionError("External mutation blocked: " + str(args[0]))
    if event in ("os.rename", "os.replace") and not all(inside(p) for p in args[:2]):
        raise PermissionError("External rename blocked")
    if event == "subprocess.Popen":
        raise PermissionError("Child processes disabled")

sys.addaudithook(guard)
if len(sys.argv) < 2:
    raise SystemExit("usage: python -B run_limited.py SCRIPT [ARG ...]")
sys.argv = sys.argv[1:]
runpy.run_path(sys.argv[0], run_name="__main__")
