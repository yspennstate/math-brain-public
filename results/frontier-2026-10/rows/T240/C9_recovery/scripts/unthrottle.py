"""Opt a process out of Windows EcoQoS execution-speed throttling (priority unchanged)."""
import ctypes, sys
from ctypes import wintypes
k = ctypes.WinDLL('kernel32', use_last_error=True)
class PPT(ctypes.Structure): _fields_ = [('Version', wintypes.ULONG), ('ControlMask', wintypes.ULONG), ('StateMask', wintypes.ULONG)]
for pid in map(int, sys.argv[1:]):
    h = k.OpenProcess(0x0200 | 0x1000, False, pid)   # PROCESS_SET_INFORMATION | QUERY_LIMITED
    s = PPT(1, 1, 0)                                  # EXECUTION_SPEED controlled, state off
    ok = k.SetProcessInformation(h, 4, ctypes.byref(s), ctypes.sizeof(s))
    print(pid, 'ok' if ok else 'err %d' % ctypes.get_last_error()); k.CloseHandle(h)
