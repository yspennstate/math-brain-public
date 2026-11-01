"""Tiny exact supplemental checks, guarded by fresh conservative local telemetry."""
from pathlib import Path
import ctypes
from ctypes import wintypes as wt
import datetime as dt
import heapq
import json
import time

ROOT = Path(__file__).resolve().parent
STATE = Path('~/.claude/compute/compute_state.json')

class MemoryStatus(ctypes.Structure):
    _fields_ = [('length', wt.DWORD), ('load', wt.DWORD)] + [(n, ctypes.c_ulonglong) for n in ('total_phys','avail_phys','total_page','avail_page','total_virtual','avail_virtual','extended')]

def cpu_ticks():
    values = [wt.FILETIME(), wt.FILETIME(), wt.FILETIME()]
    if not ctypes.windll.kernel32.GetSystemTimes(*(ctypes.byref(v) for v in values)):
        raise OSError('GetSystemTimes failed')
    return [v.dwHighDateTime * 2**32 + v.dwLowDateTime for v in values]

def edge(u,v):
    return tuple(sorted((u,v)))

def trap(w, a, b, start=0):
    length = (a*(4*w+2))//(b-a) + 1
    high = {edge((x,y),(x+1,y)) for x in range(start,start+length) for y in range(-w,w+1)}
    low = {edge((x,w+1),(x+1,w+1)) for x in range(start,start+length)}
    low |= {edge((x,y),(x,y+1)) for x in (start,start+length) for y in range(-w,w+1)}
    return length, high, low

def distance(u,v,w,length,a,b,high,low,ambient):
    upper = w+1 if ambient else w
    todo, best = [(0,u)], {u:0}
    while todo:
        cost,node = heapq.heappop(todo)
        if cost != best[node]:
            continue
        if node == v:
            return cost
        x,y = node
        for nxt in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if not (-1<=nxt[0]<=length+1 and -w<=nxt[1]<=upper):
                continue
            e = edge(node,nxt)
            weight = b if e in high else a if e in low else b
            new = cost+weight
            if new < best.get(nxt,float('inf')):
                best[nxt] = new
                heapq.heappush(todo,(new,nxt))
    raise AssertionError('Finite rectangle disconnected')

def main():
    checked_at = dt.datetime.now(dt.timezone.utc).isoformat()
    try:
        state = json.loads(STATE.read_text(encoding='utf-8-sig'))
        memory = MemoryStatus()
        memory.length = ctypes.sizeof(memory)
        if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
            raise OSError('GlobalMemoryStatusEx failed')
        first = cpu_ticks()
        time.sleep(.25)
        last = cpu_ticks()
        idle,kernel,user = [b-a for a,b in zip(first,last)]
        cpu = 100*(1-idle/max(1,kernel+user))
        age = time.time()-STATE.stat().st_mtime
        commit = state.get('commit_eff_used_pct',state.get('commit_used_pct'))
        gate = {'at_utc':checked_at,'governor_status':state.get('status'),'mode':state.get('mode'),'age_seconds':age,'live_cpu_pct':cpu,'physical_free_mb':memory.avail_phys/2**20,'commit_headroom_mb':memory.avail_page/2**20,'commit_used_pct':commit,'hung_windows':bool(state.get('hung_windows'))}
        gate['permit'] = age<=60 and state.get('status')=='ok' and state.get('mode')!='throttle' and not gate['hung_windows'] and cpu<85 and gate['physical_free_mb']>8192 and gate['commit_headroom_mb']>16384 and isinstance(commit,(int,float)) and commit<85
    except Exception as exc:
        gate = {'at_utc':checked_at,'permit':False,'reason':f'{type(exc).__name__}: {exc}'}
    (ROOT/'GEOMETRY_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
    if not gate['permit']:
        result = {'state':'NOT_RUN_RESOURCE_GATE','endpoint_cases':0,'gate':gate,'math_proof_receipt':False}
        (ROOT/'GEOMETRY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result,indent=2))
        return
    started = time.process_time()
    endpoints = support_checks = 0
    for w in range(3):
        for a,b in ((0,1),(1,2),(1,3)):
            length,high,low = trap(w,a,b)
            assert len(high)==length*(2*w+1)
            assert len(low)==length+4*w+2
            assert not high & low
            assert b*length>a*(length+4*w+2)
            supports = [set.union(*trap(w,a,b,j*(length+1))[1:]) for j in range(4)]
            for i in range(4):
                for j in range(i):
                    assert not supports[i]&supports[j]
                    support_checks+=1
            for y in range(-w,w+1):
                for z in range(-w,w+1):
                    u,v = (0,y),(length,z)
                    restricted = distance(u,v,w,length,a,b,high,low,False)
                    ambient = distance(u,v,w,length,a,b,high,low,True)
                    assert restricted>=b*length
                    assert ambient<=a*(length+4*w+2)<restricted
                    endpoints+=1
                    if time.process_time()-started>3:
                        raise RuntimeError('Declared 3 CPU-second budget exceeded')
    result = {'state':'PASS_SUPPLEMENTAL_FINITE_CHECKS','endpoint_cases':endpoints,'pairwise_support_checks':support_checks,'process_cpu_seconds':time.process_time()-started,'math_proof_receipt':False,'scope':'Finite trap realizations only; does not prove infinite-volume probability, survival, source correctness or the full target.'}
    (ROOT/'GEOMETRY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
