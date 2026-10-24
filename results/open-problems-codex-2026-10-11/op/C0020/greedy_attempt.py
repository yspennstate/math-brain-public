from functools import lru_cache
from fractions import Fraction as Q
from pathlib import Path
import json,time,gc,ctypes
from ctypes import wintypes

R=Path(__file__).resolve().parent

class MemoryInfo(ctypes.Structure):
    _fields_=[('cb',wintypes.DWORD),('faults',wintypes.DWORD)]+[
      (s,ctypes.c_size_t) for s in ['peak','working','quota_peak_paged','quota_paged',
      'quota_peak_nonpaged','quota_nonpaged','pagefile','peak_pagefile']]

def peak_memory():
    kernel=ctypes.WinDLL('kernel32');kernel.GetCurrentProcess.restype=wintypes.HANDLE
    psapi=ctypes.WinDLL('psapi')
    psapi.GetProcessMemoryInfo.argtypes=[wintypes.HANDLE,ctypes.POINTER(MemoryInfo),wintypes.DWORD]
    m=MemoryInfo();m.cb=ctypes.sizeof(m)
    assert psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(),ctypes.byref(m),m.cb)
    return m.peak

def solve(w,h):
    gc.collect()
    start=time.perf_counter(); n=w*h; full=(1<<n)-1
    calls=0
    adj=[]
    for y in range(h):
        for x in range(w):
            adj.append(sum(1<<(yy*w+xx) for dx,dy in
              [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]
              if 0<=(xx:=x+dx)<w and 0<=(yy:=y+dy)<h))
    left=sum(1<<(y*w) for y in range(h));right=left<<(w-1)
    def crossing(m):
        seen=m&left;frontier=seen
        while frontier:
            if frontier&right:return 1
            neighbors=0
            while frontier:
                b=frontier&-frontier;frontier^=b
                neighbors|=adj[b.bit_length()-1]
            frontier=neighbors&m&~seen;seen|=frontier
        return 0
    f=[crossing(m) for m in range(1<<n)]
    @lru_cache(None)
    def count(k,o):
        u=full^k
        if not u:return f[o]
        b=u&-u
        return count(k|b,o)+count(k|b,o|b)
    @lru_cache(None)
    def data(k,o):
        nonlocal calls
        calls+=1
        if calls%1024==0:
            if peak_memory()>768*1024**2:raise MemoryError('768 MiB job safety ceiling')
            if time.perf_counter()-start>480:raise TimeoutError('Eight-minute job ceiling')
        u=full^k;bits=[1<<i for i in range(n) if u&(1<<i)]
        den=1<<u.bit_count(); c=count(k,o)
        if c in [0,den]:return bits,[],Q(c,den),Q(0),Q(0)
        ds=[count(k|b,o|b)-count(k|b,o) for b in bits]
        q=Q(c,den);I=Q(2*sum(ds),den);H=I*I/(4*q*(1-q))
        return bits,ds,q,I,H
    policies={}
    @lru_cache(None)
    def costs(k,o):
        u=full^k;den=1<<u.bit_count();bits,ds,q,I,H=data(k,o)
        if not ds:return 0,0,0
        children=[(b,costs(k|b,o),costs(k|b,o|b)) for b in bits]
        opt=min(a[0]+c[0] for b,a,c in children)
        maxd=max(ds)
        allowed=[t for t,d in zip(children,ds) if d==maxd]
        gb=min(a[1]+c[1] for b,a,c in allowed)
        gw=max(a[2]+c[2] for b,a,c in allowed)
        policies[k,o]=[
          next(b for b,a,c in children if a[0]+c[0]==opt),
          next(b for b,a,c in allowed if a[1]+c[1]==gb),
          next(b for b,a,c in allowed if a[2]+c[2]==gw)]
        return den+opt,den+gb,den+gw
    root=costs(0,0)
    rootbits,rootds,q,I,H=data(0,0)
    # Independent replay of every complete input and all three policy types.
    replay=[0,0,0]; score_square=[0,0,0];score_f=[0,0,0];score_mean=[0,0,0]
    greedy_reachable=set()
    for m in range(1<<n):
        for typ in range(3):
            k=o=depth=score=0
            while (k,o) in policies:
                if typ==1:greedy_reachable.add((k,o))
                b=policies[k,o][typ];k|=b;o|=m&b
                depth+=1;score+=1 if m&b else -1
            assert f[o]==f[o|(full^k)]==f[m]
            replay[typ]+=depth;score_square[typ]+=score*score
            score_f[typ]+=score*(2*f[m]-1);score_mean[typ]+=score
    assert tuple(replay)==root
    assert score_square==replay and score_mean==[0,0,0]
    assert all(Q(v,1<<n)==I for v in score_f)
    worst=None;worst_reachable=None;checks=0
    # Traverse every restriction, including states not visited by these policies.
    for k in range(1<<n):
        o=k
        while True:
            bits,ds,q,Istate,Hstate=data(k,o)
            if ds:
                den=1<<(n-k.bit_count()-1)
                for b,d in zip(bits,ds):
                    a=Q(d,den)
                    _,_,q0,I0,H0=data(k|b,o)
                    _,_,q1,I1,H1=data(k|b,o|b)
                    assert q1-q0==a
                    assert Istate-(I0+I1)/2==a
                    v=q*(1-q);v0=q0*(1-q0);v1=q1*(1-q1)
                    assert v-(v0+v1)/2==a*a/4
                    checks+=1
                    if d==max(ds):
                        drift=Hstate-(H0+H1)/2
                        item={'known_mask':k,'one_mask':o,'query_site':b.bit_length()-1,
                          'q':str(q),'I':str(Istate),'influence':str(a),'H':str(Hstate),
                          'q0':str(q0),'q1':str(q1),'I0':str(I0),'I1':str(I1),
                          'H0':str(H0),'H1':str(H1),'drift':str(drift)}
                        if worst is None or drift<Q(worst['drift']):worst=item
                        if (k,o) in greedy_reachable and (worst_reachable is None or drift<Q(worst_reachable['drift'])):
                            worst_reachable=item
            if not o:break
            o=(o-1)&k
    result={'width':w,'height':h,'sites':n,'optimal':str(Q(root[0],1<<n)),
      'best_greedy':str(Q(root[1],1<<n)),'worst_greedy':str(Q(root[2],1<<n)),
      'root_influences':[str(Q(d,1<<(n-1))) for d in rootds],
      'root_first_query_costs':[str(Q((1<<n)+sum(costs(b,z)[0] for z in [0,b]),1<<n)) for b in rootbits],
      'root_H':str(H),'worst_greedy_H_drift':worst,
      'worst_reachable_greedy_H_drift':worst_reachable,
      'restriction_identity_checks':checks,'all_inputs_replayed':1<<n,
      'peak_working_set_bytes':peak_memory(),
      'seconds':time.perf_counter()-start}
    (R/f'greedy_{w}x{h}.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    rows=[solve(w,h) for w,h in [(2,2),(3,2),(3,3),(4,3)]]
    (R/'greedy_results.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
