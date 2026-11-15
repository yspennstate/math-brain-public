"""Sparse exploratory floats for the 1778-state length-three/five shortcut count."""
from pathlib import Path
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
import math,json,time,ctypes
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]
def available_memory():
    class MEMORYSTATUSEX(ctypes.Structure):
        _fields_=[('dwLength',ctypes.c_ulong),('dwMemoryLoad',ctypes.c_ulong),('ullTotalPhys',ctypes.c_ulonglong),('ullAvailPhys',ctypes.c_ulonglong),('ullTotalPageFile',ctypes.c_ulonglong),('ullAvailPageFile',ctypes.c_ulonglong),('ullTotalVirtual',ctypes.c_ulonglong),('ullAvailVirtual',ctypes.c_ulonglong),('ullAvailExtendedVirtual',ctypes.c_ulonglong)]
    state=MEMORYSTATUSEX();state.dwLength=ctypes.sizeof(state)
    if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(state)):
        return state.ullAvailPhys
    return None

def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    free=available_memory()
    (ROOT/'logs/chord5_resource_size.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),states=1778,nonzeros=11770,estimated_peak_bytes=256_000_000,available_physical_bytes=free,cores=1,priority='below normal'))+'\n',encoding='utf-8')
    if free is not None and free<2*1024**3:
        print('WAIT: available memory under 2 GB; no numerical run started.',flush=True);return
    import numpy as np
    from scipy.sparse import csr_matrix
    graph=json.loads((ROOT/'scripts/chord5_graph.json').read_text(encoding='utf-8'))
    n=len(graph['states']);indptr=[0];indices=[];signs=[];axisr=[];counts=[]
    for row in graph['rows']:
        for j,sign,r,c in row:
            indices.append(j);signs.append(sign);axisr.append(r);counts.append(c)
        indptr.append(len(indices))
    indices=np.array(indices,dtype=np.int32);indptr=np.array(indptr,dtype=np.int32)
    signs=np.array(signs,dtype=np.int8);axisr=np.array(axisr,dtype=np.int8);counts=np.array(counts,dtype=np.int8)
    old=json.loads((ROOT/'logs/hairpin_measurements.json').read_text(encoding='utf-8'))['rows']
    start=time.monotonic()
    results=[]
    for h in old:
        d=h['d'];dest=ROOT/'logs'/('chord5_measurement_d'+str(d)+'.json')
        if dest.exists():
            results.append(json.loads(dest.read_text()));print('resumed d',d,flush=True);continue
        mult=np.where(axisr==0,1,d-axisr)
        cache={}
        def perron(s,z):
            coeff=mult*np.where(signs==1,z,1/z)/(s+1+counts)
            matrix=csr_matrix((coeff,indices,indptr),shape=(n,n))
            vec=np.ones(n)
            for _ in range(120):
                new=matrix@vec;scale=float(new.max());new/=scale
                diff=float(np.max(np.abs(new-vec)))
                vec=new
                if diff<3e-14:break
            ratios=(matrix@vec)/vec
            return float(ratios.max()),vec
        def solve(theta):
            key=theta
            if key in cache:return cache[key]
            z=math.exp(theta)
            nb=d*math.cosh(theta)+math.sqrt(d*d*math.cosh(theta)**2-(2*d-1))-1
            lo,hi=max(.01,nb-2),nb+.01
            for _ in range(40):
                mid=(lo+hi)/2;rho,_=perron(mid,z)
                if rho>1:lo=mid
                else:hi=mid
            cache[key]=hi
            return hi
        lo,hi=h['theta']-.01,h['theta']+.01
        ratio=(math.sqrt(5)-1)/2
        x,y=hi-ratio*(hi-lo),lo+ratio*(hi-lo)
        value=lambda t: math.sqrt(d)*t/solve(t)
        fx,fy=value(x),value(y)
        for _ in range(18):
            if fx<fy:
                lo,x,fx=x,y,fy;y=lo+ratio*(hi-lo);fy=value(y)
            else:
                hi,y,fy=y,x,fx;x=hi-ratio*(hi-lo);fx=value(x)
        theta=(lo+hi)/2;s=solve(theta);z=math.exp(theta);rho,vec=perron(s,z)
        lower=math.sqrt(d)*theta/s
        obj=dict(at=datetime.now(timezone.utc).isoformat(),d=d,theta=theta,z=z,s=s,value=lower,CEG=h['CEG'],hairpin3=h['value'],relative_gain_over_CEG=lower/h['CEG']-1,relative_gain_over_hairpin3=lower/h['value']-1,rho=rho,vector=[float(a) for a in vec],status='numerical evidence only; exact graph and vector certificate pending')
        dest.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
        results.append(obj)
        print(d,format(lower,'.12f'),'over CEG',format(100*obj['relative_gain_over_CEG'],'.6f'),'%','over 3-step',format(100*obj['relative_gain_over_hairpin3'],'.6f'),'%',flush=True)
        if time.monotonic()-start>180:
            print('Checkpointed 180 second chunk; rerun to resume.',flush=True);break
    (ROOT/'logs/chord5_measurements.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),rows=results),indent=2)+'\n',encoding='utf-8')
    print('Saved',len(results),'dimensions; seconds',time.monotonic()-start,flush=True)

if __name__=='__main__':main()
