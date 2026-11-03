"""Worker policy: windowless at BelowNormal with execution-speed throttling disabled on Windows; nice 10 elsewhere."""
import ctypes
import os
import subprocess

FLAGS = 0x08000000 | 0x00004000

def unthrottle(handle):
    if os.name != 'nt':
        return
    class State(ctypes.Structure):
        _fields_ = [('Version', ctypes.c_ulong), ('ControlMask', ctypes.c_ulong),
                    ('StateMask', ctypes.c_ulong)]
    state = State(1, 1, 0)
    fn = ctypes.windll.kernel32.SetProcessInformation
    fn.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_ulong]
    fn.restype = ctypes.c_int
    if not fn(ctypes.c_void_p(int(handle)), 4, ctypes.byref(state), ctypes.sizeof(state)):
        raise ctypes.WinError()

def policy():
    if os.name == 'nt':
        handle = ctypes.windll.kernel32.GetCurrentProcess()
        ctypes.windll.kernel32.SetPriorityClass(handle, 0x00004000)
        unthrottle(handle)
    else:
        try:
            if os.getpriority(os.PRIO_PROCESS, 0) < 10:
                os.setpriority(os.PRIO_PROCESS, 0, 10)
        except (AttributeError, OSError):
            pass

def spawn(argv, **kwargs):
    if os.name != 'nt':
        # its own session, so the child outlives the shell that started it
        return subprocess.Popen(argv, start_new_session=True, **kwargs)
    p = subprocess.Popen(argv, creationflags=FLAGS, **kwargs)
    try:
        unthrottle(p._handle)
    except Exception:
        p.terminate()
        p.wait()
        raise
    return p
