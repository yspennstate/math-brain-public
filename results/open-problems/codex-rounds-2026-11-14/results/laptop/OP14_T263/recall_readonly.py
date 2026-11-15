"""Run the prescribed math recall without outside writes or large allocations.

Windows only. Stdlib, no encoder, one CPU, 768 MiB commit cap, BelowNormal.
If a shared cache needs mutation, the read fails safely instead of building it.
"""
import os
import sys
import ctypes
from ctypes import wintypes
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parent
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"
os.environ["MATH_STRENGTH_NOLOG"] = "1"
os.environ["MATH_STRENGTH_OFF"] = "1"
os.environ["MATH_BRAIN_SEMANTIC"] = "0"
os.environ["MATH_RECALL_FAST_ENCODER"] = "0"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

if os.name != "nt":
    raise RuntimeError("This memory guard is Windows-specific")
k = ctypes.WinDLL("kernel32", use_last_error=True)
k.GetCurrentProcess.restype = wintypes.HANDLE
k.CreateJobObjectW.restype = wintypes.HANDLE
k.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
k.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int,
                                     ctypes.c_void_p, wintypes.DWORD]
k.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
k.SetPriorityClass.argtypes = [wintypes.HANDLE, wintypes.DWORD]
k.GetProcessAffinityMask.argtypes = [wintypes.HANDLE, ctypes.POINTER(ctypes.c_size_t),
                                   ctypes.POINTER(ctypes.c_size_t)]
k.SetProcessAffinityMask.argtypes = [wintypes.HANDLE, ctypes.c_size_t]


class Basic(ctypes.Structure):
    _fields_ = [("PerProcessUserTimeLimit", ctypes.c_longlong),
                ("PerJobUserTimeLimit", ctypes.c_longlong),
                ("LimitFlags", wintypes.DWORD),
                ("MinimumWorkingSetSize", ctypes.c_size_t),
                ("MaximumWorkingSetSize", ctypes.c_size_t),
                ("ActiveProcessLimit", wintypes.DWORD),
                ("Affinity", ctypes.c_size_t),
                ("PriorityClass", wintypes.DWORD),
                ("SchedulingClass", wintypes.DWORD)]


class Counters(ctypes.Structure):
    _fields_ = [(name, ctypes.c_ulonglong) for name in
                ("ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
                 "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]


class Extended(ctypes.Structure):
    _fields_ = [("BasicLimitInformation", Basic), ("IoInfo", Counters),
                ("ProcessMemoryLimit", ctypes.c_size_t),
                ("JobMemoryLimit", ctypes.c_size_t),
                ("PeakProcessMemoryUsed", ctypes.c_size_t),
                ("PeakJobMemoryUsed", ctypes.c_size_t)]


proc = k.GetCurrentProcess()
job = k.CreateJobObjectW(None, None)
limits = Extended()
limits.BasicLimitInformation.LimitFlags = 0x100  # process commit limit
limits.ProcessMemoryLimit = 768 * 1024 * 1024
for ok in (job, k.SetInformationJobObject(job, 9, ctypes.byref(limits),
                                        ctypes.sizeof(limits)),
           k.AssignProcessToJobObject(job, proc), k.SetPriorityClass(proc, 0x4000)):
    if not ok:
        raise ctypes.WinError(ctypes.get_last_error())
pm, sm = ctypes.c_size_t(), ctypes.c_size_t()
if not k.GetProcessAffinityMask(proc, ctypes.byref(pm), ctypes.byref(sm)):
    raise ctypes.WinError(ctypes.get_last_error())
if not k.SetProcessAffinityMask(proc, pm.value & -pm.value):
    raise ctypes.WinError(ctypes.get_last_error())


def inside(path):
    if isinstance(path, int):
        return True
    try:
        return Path(os.fsdecode(path)).resolve().is_relative_to(ROOT)
    except (ValueError, TypeError):
        return False


def audit(event, args):
    if event == "open":
        path, mode, flags = args
        writing = (mode is not None and any(c in mode for c in "wax+"))
        writing |= bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
        if writing and not inside(path):
            raise PermissionError("Recall attempted an outside write: " + str(path))
    elif event in ("os.mkdir", "os.remove", "os.rmdir", "os.chmod", "os.utime"):
        if not inside(args[0]):
            raise PermissionError("Recall attempted an outside mutation: " + str(args[0]))
    elif event in ("os.rename", "os.replace"):
        if not all(inside(p) for p in args[:2]):
            raise PermissionError("Recall attempted an outside move")
    elif event in ("subprocess.Popen", "os.system"):
        raise PermissionError("Subprocesses disabled during read-only recall")


sys.addaudithook(audit)
sys.path.insert(0, r"~\.claude\dreaming")
target = r"~\.claude\dreaming\math_recall.py"
sys.argv = [target, "T263 generalization overparameterized networks",
            "--or", "Gaussian mixture benign overfitting leaky ReLU",
            "--or", "Gaussian tail margin constant factor", "--limit", "3"]
runpy.run_path(target, run_name="__main__")
