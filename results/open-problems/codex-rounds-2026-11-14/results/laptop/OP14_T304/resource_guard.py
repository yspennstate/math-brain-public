"""Local, single-core, below-normal, 768 MiB process guard; no external writes."""
import ctypes
from ctypes import wintypes as w
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
_JOB = None


def enable():
    global _JOB
    sys.dont_write_bytecode = True
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                 "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
        os.environ[name] = "1"
    if os.name != "nt":
        raise RuntimeError("This resource guard is written for the specified Windows host")
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.GetCurrentProcess.restype = w.HANDLE
    proc = kernel.GetCurrentProcess()
    kernel.SetPriorityClass.argtypes = (w.HANDLE, w.DWORD)
    if not kernel.SetPriorityClass(proc, 0x4000):
        raise ctypes.WinError(ctypes.get_last_error())
    kernel.GetProcessAffinityMask.argtypes = (
        w.HANDLE, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_size_t))
    allowed, system = ctypes.c_size_t(), ctypes.c_size_t()
    if not kernel.GetProcessAffinityMask(proc, ctypes.byref(allowed), ctypes.byref(system)):
        raise ctypes.WinError(ctypes.get_last_error())
    kernel.SetProcessAffinityMask.argtypes = (w.HANDLE, ctypes.c_size_t)
    core = allowed.value & -allowed.value
    if not kernel.SetProcessAffinityMask(proc, core):
        raise ctypes.WinError(ctypes.get_last_error())

    class Basic(ctypes.Structure):
        _fields_ = [("process_time", ctypes.c_longlong), ("job_time", ctypes.c_longlong),
                    ("flags", w.DWORD), ("min_ws", ctypes.c_size_t),
                    ("max_ws", ctypes.c_size_t), ("active", w.DWORD),
                    ("affinity", ctypes.c_size_t), ("priority", w.DWORD),
                    ("scheduling", w.DWORD)]

    class IO(ctypes.Structure):
        _fields_ = [(name, ctypes.c_ulonglong) for name in
                    ("read_ops", "write_ops", "other_ops", "read_bytes", "write_bytes", "other_bytes")]

    class Extended(ctypes.Structure):
        _fields_ = [("basic", Basic), ("io", IO), ("process_memory", ctypes.c_size_t),
                    ("job_memory", ctypes.c_size_t), ("peak_process", ctypes.c_size_t),
                    ("peak_job", ctypes.c_size_t)]

    kernel.CreateJobObjectW.argtypes = (ctypes.c_void_p, w.LPCWSTR)
    kernel.CreateJobObjectW.restype = w.HANDLE
    kernel.SetInformationJobObject.argtypes = (w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD)
    kernel.AssignProcessToJobObject.argtypes = (w.HANDLE, w.HANDLE)
    _JOB = kernel.CreateJobObjectW(None, None)
    info = Extended()
    info.basic.flags = 0x100  # JOB_OBJECT_LIMIT_PROCESS_MEMORY
    info.process_memory = 768 * 1024 * 1024
    if not _JOB or not kernel.SetInformationJobObject(_JOB, 9, ctypes.byref(info), ctypes.sizeof(info)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not kernel.AssignProcessToJobObject(_JOB, proc):
        raise ctypes.WinError(ctypes.get_last_error())

    def check_write(path):
        if isinstance(path, int):
            return
        target = Path(os.fsdecode(path)).resolve()
        if not target.is_relative_to(ROOT):
            raise PermissionError("Outside-folder write blocked: " + str(target))

    def audit(event, args):
        if event == "open":
            path, mode, flags = args
            if (isinstance(mode, str) and any(x in mode for x in "wax+")) or (
                    isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC)):
                check_write(path)
        elif event in ("os.mkdir", "os.remove", "os.rmdir", "os.chmod", "os.utime"):
            check_write(args[0])
        elif event in ("os.rename", "os.replace"):
            check_write(args[0])
            check_write(args[1])
        elif event in ("subprocess.Popen", "os.system", "os.startfile"):
            raise PermissionError("Child processes are disabled")

    sys.addaudithook(audit)
    return {"priority": "BelowNormal", "affinity_mask": core,
            "process_memory_limit_MiB": 768, "thread_environment": 1}


if __name__ == "__main__":
    metadata = enable()
    import json
    import runpy
    print(json.dumps(metadata), flush=True)
    if len(sys.argv) < 2:
        raise SystemExit("usage: python -B resource_guard.py SCRIPT [ARGS]")
    script = Path(sys.argv[1]).resolve()
    sys.argv = [str(script)] + sys.argv[2:]
    sys.path.insert(0, str(script.parent))
    runpy.run_path(str(script), run_name="__main__")
