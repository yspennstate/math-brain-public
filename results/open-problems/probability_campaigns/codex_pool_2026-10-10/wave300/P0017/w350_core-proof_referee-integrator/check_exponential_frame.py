from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
import ctypes
import json
import time

ROOT=Path(__file__).resolve().parent
out=ROOT/'measurements'
out.mkdir(exist_ok=True)

class MemoryStatus(ctypes.Structure):
    _fields_=[('length',ctypes.c_ulong),('memory_load',ctypes.c_ulong),('total_phys',ctypes.c_ulonglong),('avail_phys',ctypes.c_ulonglong),('total_page',ctypes.c_ulonglong),('avail_page',ctypes.c_ulonglong),('total_virtual',ctypes.c_ulonglong),('avail_virtual',ctypes.c_ulonglong),('avail_extended',ctypes.c_ulonglong)]

class FileTime(ctypes.Structure):
    _fields_=[('low',ctypes.c_ulong),('high',ctypes.c_ulong)]

def cpu_sample():
    idle,kernel,user=FileTime(),FileTime(),FileTime()
    if not ctypes.windll.kernel32.GetSystemTimes(ctypes.byref(idle),ctypes.byref(kernel),ctypes.byref(user)): raise OSError('GetSystemTimes failed')
    return tuple(x.low+(x.high<<32) for x in (idle,kernel,user))

m=MemoryStatus();m.length=ctypes.sizeof(m)
if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m)): raise OSError('memory gate unavailable')
a=cpu_sample();time.sleep(0.2);b=cpu_sample()
idle=b[0]-a[0];total=(b[1]-a[1])+(b[2]-a[2]);load=100*(1-idle/total) if total else 100
gate={'measured_unix_time':time.time(),'cpu_percent_200ms':load,'available_memory_mb':m.avail_phys/(1024**2),'max_cpu_percent':85,'minimum_available_memory_mb':512,'arithmetic_deadline_seconds':15,'maximum_degree':8,'maximum_support_size':4,'training':False,'gpu':False,'processes':1}
(out/'fresh_host_gate.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
if load>85 or m.avail_phys<512*1024**2:
    result={'status':'SKIPPED_RESOURCE_GATE','gate':gate,'command':'python -X utf8 check_exponential_frame.py'}
    (out/'exponential_frame.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result));raise SystemExit(0)

start=time.monotonic()
def compositions(d,s):
    if s==1: return [(d,)]
    return [(a,*tail) for a in range(1,d-s+2) for tail in compositions(d-a,s-1)]

def check_psd(matrix):
    a=[row[:] for row in matrix]
    for k in range(len(a)):
        pivot=a[k][k]
        assert pivot>=0,('negative LDL pivot',k,pivot)
        if pivot==0:
            assert all(a[k][j]==0 for j in range(k+1,len(a))),('zero pivot with nonzero row',k)
        else:
            for i in range(k+1,len(a)):
                for j in range(i,len(a)):
                    a[i][j]-=a[i][k]*a[k][j]/pivot
                    a[j][i]=a[i][j]

blocks=0;maxsize=0
for d in range(1,9):
    bound=comb(2*d-2,d-1)
    for s in range(1,min(d,4)+1):
        indices=compositions(d,s)
        weights=[]
        for alpha in indices:
            product=1
            for a in alpha:product*=factorial(a)
            weights.append(F(product,factorial(d)))
        gram=[]
        for alpha in indices:
            row=[]
            for beta in indices:
                g=1
                for a,b in zip(alpha,beta):g*=comb(a+b-2,a-1)
                row.append(F(g))
            gram.append(row)
        matrix=[[((F(bound)/weights[i]) if i==j else F(0))-gram[i][j] for j in range(len(indices))] for i in range(len(indices))]
        check_psd(matrix)
        if s==1:assert matrix==[[F(0)]],('single-coordinate equality witness failed',d)
        blocks+=1;maxsize=max(maxsize,len(indices))
        if time.monotonic()-start>15:raise RuntimeError('Fresh host arithmetic deadline exceeded')

result={'status':'PASS','command':'python -X utf8 check_exponential_frame.py','exact_psd_blocks':blocks,'maximum_block_size':maxsize,'degree_range':[1,8],'support_size_range':[1,4],'elapsed_arithmetic_seconds':round(time.monotonic()-start,6),'gate_file':'measurements/fresh_host_gate.json','trust':'Exact rational LDL checks of finite Gram blocks; general all-degree proof is the separate written argument, not these tests.'}
(out/'exponential_frame.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result),flush=True)
