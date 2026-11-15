"""Run only this process's Python work below normal, without power throttling."""
import ctypes,runpy,sys
k=ctypes.windll.kernel32
k.GetCurrentProcess.restype=ctypes.c_void_p
k.SetPriorityClass.argtypes=[ctypes.c_void_p,ctypes.c_ulong]
k.SetProcessInformation.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_ulong]
p=k.GetCurrentProcess()
assert k.SetPriorityClass(p,0x4000)
class Throttle(ctypes.Structure):
    _fields_=[('Version',ctypes.c_ulong),('ControlMask',ctypes.c_ulong),('StateMask',ctypes.c_ulong)]
t=Throttle(1,1,0)
assert k.SetProcessInformation(p,4,ctypes.byref(t),ctypes.sizeof(t))
sys.argv=sys.argv[1:]
runpy.run_path(sys.argv[0],run_name='__main__')
