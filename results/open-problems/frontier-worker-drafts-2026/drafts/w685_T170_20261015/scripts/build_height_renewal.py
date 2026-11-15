"""Size the C3/even-square finite state used by a height-cut renewal operator.

This graph has a marked-first-step input for cut vertices. It is not a
time-constant certificate. One core, below normal,200000-state/120s guard.
"""
from pathlib import Path
from collections import Counter
import json,time,ctypes
from datetime import datetime,timezone
from measure_chord5 import available_memory
ROOT=Path(__file__).resolve().parents[1]
def canon(h):
    axes={};return tuple((axes.setdefault(a,len(axes)),b) for a,b in h)
def norm(h):
    axes={}
    for a,b in h:axes[a]=axes.get(a,0)+b
    return sum(abs(v) for v in axes.values())
def allowed(h):return all(len(h)<k or norm(h[-k:])>0 for k in (2,4))
def seeds():
    out=set()
    def visit(h):
        if len(h)==4:
            c=[0]*4;dirty=set()
            for i in (0,1):
                if norm(h[i:i+3])==1:
                    for e in range(i,i+3):c[e]+=1
                    v=i if i%2==0 else i+3;dirty.update((v//2-1,v//2))
            if norm(h)<=2:dirty.update((0,1))
            eligible=tuple(h[2*k][0]!=h[2*k+1][0] and k not in dirty for k in range(2))
            possible=h[1][1]==h[2][1]==1 and h[1][0]!=h[2][0]
            for bit in ((False,True) if possible else (False,)):
                out.add((0,canon(h[-3:]),tuple(c),eligible,2 in dirty,(bit,False),False,0))
            return
        r=len({a for a,b in h})
        for a in range(r+1):
            for b in (-1,1):
                full=h+((a,b),)
                if allowed(full):visit(full)
    visit(())
    return sorted(out)
def outgoing(state,marked):
    parity,h,c,eligible,future,odd,previous,p=state;r=len({a for a,b in h})
    assert len(c)==(4 if parity==0 else 3) and len(eligible)==(2 if parity==0 else 1)
    assert len(odd)==len(eligible) and (previous or p==0)
    if parity==0:assert not odd[-1]
    for axis in range(r+1):
        for sign in (-1,1):
            full=h+((axis,sign),)
            if not allowed(full):continue
            chord=norm(full[-3:])==1;counts=list(c)+[0]
            if chord:
                for j in range(len(counts)-3,len(counts)):counts[j]+=1
            if parity:
                queue=list(eligible)+[h[-1][0]!=axis and not future]
                if chord:queue[-1]=False
                if norm(full)<=2:queue[-2]=False;queue[-1]=False
                target=(0,canon(full[-3:]),tuple(counts),tuple(queue),chord,odd+(False,),previous,p)
                yield target,sign,(r if axis==r else 0),0,0,0,0,0,int(previous),p,p
            else:
                queue=list(eligible)
                if chord:queue[0]=False;queue[1]=False
                cuts=list(odd)
                if marked and h[-1][1]==sign==1 and h[-1][0]!=axis:cuts[-1]=True
                e,o=queue[0],cuts[0]
                for q in ((0,1) if o else (0,)):
                    target=(1,canon(full[-3:]),tuple(counts[2:]),tuple(queue[1:]),future,tuple(cuts[1:]),o,q)
                    yield target,sign,(r if axis==r else 0),1,counts[0],counts[1],int(e),int(o),int(previous),p,q
def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    free=available_memory()
    if free is not None and free<2*1024**3:print('WAIT: under2GB free.',flush=True);return
    (ROOT/'logs/height_renewal_resource_size.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),estimated_peak_bytes=768000000,available_physical_bytes=free,cores=1,priority='below normal',state_cap=200000))+'\n',encoding='utf-8')
    states=seeds();index={s:i for i,s in enumerate(states)};rows=[];at=0;started=time.monotonic()
    while at<len(states):
        if len(states)>200000 or time.monotonic()-started>120:
            status=dict(at=datetime.now(timezone.utc).isoformat(),states=len(states),processed=at,seconds=time.monotonic()-started,status='size/time guard; no mathematical failure')
            (ROOT/'logs/height_renewal_guard.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8');print(json.dumps(status));return
        both=[]
        for mark in (False,True):
            row=[]
            for item in outgoing(states[at],mark):
                target=item[0]
                if target not in index:index[target]=len(states);states.append(target)
                row.append((index[target],)+item[1:])
            both.append(row)
        rows.append(both);at+=1
    obj=dict(at=datetime.now(timezone.utc).isoformat(),states=states,rows=rows,seconds=time.monotonic()-started,status='finite marked-input graph only; no contraction or FPP bound')
    dest=ROOT/'scripts/height_renewal_graph.json';part=dest.with_suffix('.json.part');part.write_text(json.dumps(obj,separators=(',',':'))+'\n',encoding='utf-8');part.replace(dest)
    print('DONE states',len(states),'unmarked_edges',sum(len(row[0]) for row in rows),'marked_edges',sum(len(row[1]) for row in rows),'seconds',obj['seconds'],flush=True)
if __name__=='__main__':main()
