"""Replay archived checker with safe in-process time/memory exceptions."""
import pathlib,time,ctypes
started=time.monotonic();calls=0
class Mem(ctypes.Structure):
 _fields_=[('cb',ctypes.c_ulong),('PageFaultCount',ctypes.c_ulong)]+[(n,ctypes.c_size_t) for n in ['PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage','QuotaPagedPoolUsage','QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage']]
def _guard():
 global calls
 calls+=1
 if calls%2048:return
 if time.monotonic()-started>240:raise RuntimeError('bounded prior-check time cap')
 m=Mem();m.cb=ctypes.sizeof(m);ctypes.windll.psapi.GetProcessMemoryInfo(ctypes.c_void_p(-1),ctypes.byref(m),m.cb)
 if m.WorkingSetSize>850000000:raise RuntimeError('bounded prior-check memory cap')
s=pathlib.Path(__file__).with_name('prior_policy_checker.py').read_text(encoding='utf8')
s=s.replace('def norm(ch):\n','def norm(ch):\n    _guard()\n',1)
try:
 exec(compile(s,'prior_policy_checker.py','exec'),globals())
except RuntimeError as e:print('INCOMPLETE',e)
print('Replay seconds',time.monotonic()-started,flush=True)
