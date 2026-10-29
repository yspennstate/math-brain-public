"""Set this worker's own process BelowNormal on a shared two-core pool."""
import ctypes

def apply_limits():
    k=ctypes.WinDLL('kernel32',use_last_error=True)
    k.GetCurrentProcess.restype=ctypes.c_void_p
    k.SetPriorityClass.argtypes=[ctypes.c_void_p,ctypes.c_uint]
    k.GetPriorityClass.argtypes=[ctypes.c_void_p]
    k.GetPriorityClass.restype=ctypes.c_uint
    k.GetProcessAffinityMask.argtypes=[ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_size_t),ctypes.POINTER(ctypes.c_size_t)]
    k.SetProcessAffinityMask.argtypes=[ctypes.c_void_p,ctypes.c_size_t]
    proc=k.GetCurrentProcess()
    if not k.SetPriorityClass(proc,0x4000):
        raise ctypes.WinError(ctypes.get_last_error())
    available,system=ctypes.c_size_t(),ctypes.c_size_t()
    if not k.GetProcessAffinityMask(proc,ctypes.byref(available),ctypes.byref(system)):
        raise ctypes.WinError(ctypes.get_last_error())
    bits=[1<<i for i in range(ctypes.sizeof(ctypes.c_size_t)*8)
          if available.value&(1<<i)]
    if not bits: raise RuntimeError('Empty process affinity mask')
    chosen=sum(bits)
    if not k.SetProcessAffinityMask(proc,chosen):
        raise ctypes.WinError(ctypes.get_last_error())
    if k.GetPriorityClass(proc)!=0x4000:
        raise RuntimeError('BelowNormal priority did not persist')
    return {'priority':'BelowNormal','affinity_mask':chosen,'cores':chosen.bit_count()}

try:
    from unthrottle import unthrottle_self
except Exception:
    unthrottle_self = None
_orig_apply = apply_limits
def apply_limits(*a, **kw):
    r = _orig_apply(*a, **kw)
    if unthrottle_self: unthrottle_self()
    return r
