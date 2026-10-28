"""Windows subprocess tree owned by a native Job Object before its first instruction.

The child starts suspended. A failed job assignment never launches it. Cleanup
uses native handles and cannot select an unrelated process by a reused PID.
"""
import ctypes as c
from ctypes import wintypes as w
import os
import subprocess
import time


class BasicLimit(c.Structure):
    _fields_ = [("process_time", c.c_longlong), ("job_time", c.c_longlong),
                ("flags", w.DWORD), ("min_working_set", c.c_size_t),
                ("max_working_set", c.c_size_t), ("active_limit", w.DWORD),
                ("affinity", c.c_size_t), ("priority", w.DWORD), ("scheduling", w.DWORD)]


class IoCounters(c.Structure):
    _fields_ = [(name, c.c_ulonglong) for name in
                ("read_ops", "write_ops", "other_ops", "read_bytes", "write_bytes", "other_bytes")]


class ExtendedLimit(c.Structure):
    _fields_ = [("basic", BasicLimit), ("io", IoCounters),
                ("process_memory", c.c_size_t), ("job_memory", c.c_size_t),
                ("peak_process_memory", c.c_size_t), ("peak_job_memory", c.c_size_t)]


def run(argv, *, input=None, cwd=None, timeout=600, progress=None, env=None):
    if os.name != "nt":
        raise RuntimeError("This process owner is implemented and tested for Windows only")
    import psutil
    k = c.WinDLL("kernel32", use_last_error=True)
    k.CreateJobObjectW.argtypes = [c.c_void_p, w.LPCWSTR]
    k.CreateJobObjectW.restype = w.HANDLE
    k.SetInformationJobObject.argtypes = [w.HANDLE, c.c_int, c.c_void_p, w.DWORD]
    k.SetInformationJobObject.restype = w.BOOL
    k.AssignProcessToJobObject.argtypes = [w.HANDLE, w.HANDLE]
    k.AssignProcessToJobObject.restype = w.BOOL
    k.TerminateJobObject.argtypes = [w.HANDLE, w.UINT]
    k.TerminateJobObject.restype = w.BOOL
    k.CloseHandle.argtypes = [w.HANDLE]
    k.CloseHandle.restype = w.BOOL
    k.OpenThread.argtypes = [w.DWORD, w.BOOL, w.DWORD]
    k.OpenThread.restype = w.HANDLE
    k.GetProcessIdOfThread.argtypes = [w.HANDLE]
    k.GetProcessIdOfThread.restype = w.DWORD
    k.ResumeThread.argtypes = [w.HANDLE]
    k.ResumeThread.restype = w.DWORD

    def checked(value):
        if not value:
            raise c.WinError(c.get_last_error())
        return value

    job = checked(k.CreateJobObjectW(None, None))
    proc = None
    assigned = False
    try:
        limits = ExtendedLimit()
        limits.basic.flags = 0x2000  # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
        checked(k.SetInformationJobObject(job, 9, c.byref(limits), c.sizeof(limits)))
        flags = subprocess.CREATE_NO_WINDOW | subprocess.BELOW_NORMAL_PRIORITY_CLASS | 0x4
        proc = subprocess.Popen(argv, cwd=cwd, env=env, stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, encoding="utf-8", errors="replace",
                                creationflags=flags)
        if progress:
            progress({"phase": "created_suspended", "pid": proc.pid})
        # Popen retains this native handle until process cleanup. The child is suspended.
        checked(k.AssignProcessToJobObject(job, w.HANDLE(int(proc._handle))))
        assigned = True
        threads = psutil.Process(proc.pid).threads()
        if len(threads) != 1:
            raise RuntimeError("Expected one suspended initial thread; refusing ambiguous launch")
        thread = checked(k.OpenThread(0x0802, False, threads[0].id))
        try:
            if k.GetProcessIdOfThread(thread) != proc.pid:
                raise RuntimeError("Initial thread ownership changed")
            suspend_count = k.ResumeThread(thread)
            if progress:
                progress({"phase": "resumed", "previous_suspend_count": suspend_count})
            if suspend_count == 0xFFFFFFFF:
                raise c.WinError(c.get_last_error())
            if suspend_count != 1:
                raise RuntimeError("Unexpected suspend count; refusing to override another process controller")
        finally:
            k.CloseHandle(thread)
        start = time.monotonic()
        pending_input = input
        while True:
            try:
                out, err = proc.communicate(pending_input, timeout=min(15, max(0.01, timeout - (time.monotonic() - start))))
                break
            except subprocess.TimeoutExpired as exc:
                pending_input = None
                elapsed = time.monotonic() - start
                if progress:
                    progress({"phase": "waiting", "seconds": round(elapsed, 3), "root_exit_code": proc.poll()})
                if elapsed >= timeout:
                    checked(k.TerminateJobObject(job, 124))
                    out, err = proc.communicate(timeout=15)
                    raise subprocess.TimeoutExpired(argv, timeout, output=out, stderr=err) from exc
        return subprocess.CompletedProcess(argv, proc.returncode, out, err)
    finally:
        if proc is not None and proc.poll() is None:
            if assigned:
                k.TerminateJobObject(job, 125)
            else:
                proc.kill()  # native handle; never resumed, so no descendants exist
        k.CloseHandle(job)  # also closes any remaining descendants owned by this call
        if proc is not None:
            try:
                proc.wait(timeout=15)
            finally:
                for pipe in (proc.stdin, proc.stdout, proc.stderr):
                    if pipe is not None:
                        pipe.close()
