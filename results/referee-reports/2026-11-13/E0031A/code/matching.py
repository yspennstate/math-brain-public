"""Complete-graph perfect matching with an exact integer primal/dual check."""
import ctypes as c, os
from pathlib import Path
# Must precede numerical imports, including when imported by another script.
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
 os.environ[key]='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=10, 'run at nice 10 or greater'
import numpy as np
LIB=c.CDLL(str(Path(__file__).resolve().with_name('libmatching.dylib')))
LIB.solve_matching.argtypes=[c.c_int,c.c_int,c.POINTER(c.c_double),c.c_longlong,c.POINTER(c.c_int),c.POINTER(c.c_longlong),c.POINTER(c.c_double)]
LIB.solve_matching.restype=c.c_int
SCALE=10**12

def solve(points,scale=SCALE):
 x=np.ascontiguousarray(points,dtype=np.float64);n,d=x.shape
 partners=np.empty(n,dtype=np.int32);q=c.c_longlong();length=c.c_double()
 status=LIB.solve_matching(n,d,x.ctypes.data_as(c.POINTER(c.c_double)),scale,partners.ctypes.data_as(c.POINTER(c.c_int)),c.byref(q),c.byref(length))
 if status: raise RuntimeError(f'Blossom status {status}; no sample may be silently omitted')
 assert np.array_equal(partners[partners],np.arange(n))
 assert np.all(partners!=np.arange(n))
 return length.value,q.value,partners
