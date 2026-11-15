"""Check actual macOS thread counts during the same numerical kernels."""
import ctypes
import json
import os
from pathlib import Path
import threading
import time
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal

class TaskInfo(ctypes.Structure):
    _fields_=[('virtual_size',ctypes.c_uint64),('resident_size',ctypes.c_uint64),
        ('total_user',ctypes.c_uint64),('total_system',ctypes.c_uint64),
        ('threads_user',ctypes.c_uint64),('threads_system',ctypes.c_uint64),
        *[(x,ctypes.c_int32) for x in ('policy','faults','pageins','cow_faults','messages_sent',
        'messages_received','syscalls_mach','syscalls_unix','csw','threadnum','numrunning','priority')]]

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)==10
    lib=ctypes.CDLL('/usr/lib/libproc.dylib')
    stop=threading.Event()
    samples=[]
    def monitor():
        while not stop.is_set():
            info=TaskInfo()
            size=lib.proc_pidinfo(os.getpid(),4,0,ctypes.byref(info),ctypes.sizeof(info))
            if size!=ctypes.sizeof(info):
                raise RuntimeError('proc_pidinfo failed')
            samples.append((info.threadnum,info.resident_size))
            stop.wait(.005)
    watcher=threading.Thread(target=monitor)
    watcher.start()
    rng=np.random.default_rng(813)
    for n in [64,1024,2048]:
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        h=(z+z.conj().T)/2
        del z
        eigh(h,subset_by_index=(n-2,n-1),eigvals_only=True,check_finite=False,driver='evr')
        del h
    n=4096
    a=rng.normal(size=n)
    b=np.sqrt(rng.chisquare(2*np.arange(n-1,0,-1))/2)
    eigh_tridiagonal(a,b,select='i',select_range=(n-2,n-1))
    stop.set();watcher.join()
    result=dict(samples=len(samples),max_native_threads_including_monitor=max(x[0] for x in samples),
                max_rss_bytes=max(x[1] for x in samples),nice=os.getpriority(os.PRIO_PROCESS,0),
                scope='Separate same-kernel audit, 5 ms polling; not a census of the earlier full run')
    assert result['max_native_threads_including_monitor']<=4
    assert result['max_rss_bytes']<4*1024**3
    (Path(__file__).resolve().parents[1]/'data/resource_audit.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
