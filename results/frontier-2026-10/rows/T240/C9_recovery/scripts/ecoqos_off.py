# Opt given PIDs out of Windows EcoQoS power throttling; priority class is left as it is.
import ctypes, sys
from ctypes import wintypes
k = ctypes.WinDLL("kernel32", use_last_error=True)
class PPT(ctypes.Structure):
    _fields_ = [("Version", wintypes.ULONG), ("ControlMask", wintypes.ULONG), ("StateMask", wintypes.ULONG)]
k.OpenProcess.restype = wintypes.HANDLE
for pid in map(int, sys.argv[1:]):
    h = k.OpenProcess(0x0200 | 0x1000, False, pid)   # PROCESS_SET_INFORMATION | QUERY_LIMITED
    s = PPT(1, 1, 0)                                  # EXECUTION_SPEED controlled, state off
    ok = k.SetProcessInformation(wintypes.HANDLE(h), 4, ctypes.byref(s), ctypes.sizeof(s)) if h else 0
    print(pid, "ok" if ok else "fail %d" % ctypes.get_last_error())
    if h: k.CloseHandle(wintypes.HANDLE(h))
