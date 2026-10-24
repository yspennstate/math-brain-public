from exact_crossings import solve
from ctypes import wintypes as w
import ctypes,json
from pathlib import Path
solve(4,3)
class PMC(ctypes.Structure):
    _fields_=[('cb',w.DWORD),('PageFaultCount',w.DWORD),
      ('PeakWorkingSetSize',ctypes.c_size_t),('WorkingSetSize',ctypes.c_size_t),
      ('QuotaPeakPagedPoolUsage',ctypes.c_size_t),('QuotaPagedPoolUsage',ctypes.c_size_t),
      ('QuotaPeakNonPagedPoolUsage',ctypes.c_size_t),('QuotaNonPagedPoolUsage',ctypes.c_size_t),
      ('PagefileUsage',ctypes.c_size_t),('PeakPagefileUsage',ctypes.c_size_t)]
m=PMC();m.cb=ctypes.sizeof(m)
k=ctypes.WinDLL('kernel32'); k.GetCurrentProcess.restype=w.HANDLE
p=ctypes.WinDLL('psapi')
p.GetProcessMemoryInfo.argtypes=[w.HANDLE,ctypes.POINTER(PMC),w.DWORD]
p.GetProcessMemoryInfo.restype=w.BOOL
ok=p.GetProcessMemoryInfo(k.GetCurrentProcess(),ctypes.byref(m),m.cb)
assert ok and m.PeakWorkingSetSize<1024**3
result={'success':bool(ok),'peak_working_set_bytes':m.PeakWorkingSetSize}
Path(__file__).resolve().with_name('memory_check.json').write_text(json.dumps(result),encoding='utf8')
print(result)
