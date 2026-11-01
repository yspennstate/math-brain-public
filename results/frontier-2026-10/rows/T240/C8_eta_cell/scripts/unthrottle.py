"""Opt processes out of Windows EcoQoS execution-speed throttling (priority unchanged).
Usage: python unthrottle.py PID [PID ...]   (or import and call unthrottle_self())"""
import ctypes, sys
from ctypes import wintypes

class PPT(ctypes.Structure):
    _fields_ = [('Version', wintypes.ULONG), ('ControlMask', wintypes.ULONG), ('StateMask', wintypes.ULONG)]

k = ctypes.WinDLL('kernel32', use_last_error=True)
k.OpenProcess.restype = wintypes.HANDLE
k.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
k.SetProcessInformation.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
k.GetCurrentProcess.restype = wintypes.HANDLE

def _apply(h):
    s = PPT(1, 1, 0)  # control EXECUTION_SPEED, state off
    return bool(k.SetProcessInformation(h, 4, ctypes.byref(s), ctypes.sizeof(s)))

def unthrottle_self():
    return _apply(k.GetCurrentProcess())

if __name__ == '__main__':
    for p in map(int, sys.argv[1:]):
        h = k.OpenProcess(0x0200, False, p)
        print(p, 'ok' if h and _apply(h) else 'fail %d' % ctypes.get_last_error())
        if h: k.CloseHandle(h)
