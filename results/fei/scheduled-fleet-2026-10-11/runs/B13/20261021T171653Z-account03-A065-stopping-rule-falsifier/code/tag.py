"""Frozen finite early-tag stress test; complete physical continuation reserves."""
import kernel as k
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
import json, time, sys
ROOT=Path(__file__).resolve().parents[1]
PRICES=(F(4),F(32609,5000),F(8))

def table(j): return bytes((j>>i)&1 for i in range(4))

def construct(a,u,v,tag=True):
    # w=+1 chooses u when a=+1; bits encode minus signs.
    if not tag:
        return bytes((u if w==0 else v)[x] for w in range(2) for x in range(4))
    return bytes((u if (w^a[z])==0 else v)[x]
                 for w in range(2) for x in range(4) for z in range(4))

@lru_cache(None)
def reserve(t,order):
    h,counts=k.stats(t)
    if not any(counts): return tuple((0,0) for _ in PRICES)
    i=order[0]; new=tuple(j-(j>i) for j in order[1:])
    a,b=k.children(t,i); qa,qb=reserve(a,new),reserve(b,new)
    D=k.sub(h,k.half(k.add(k.stats(a)[0],k.stats(b)[0])))
    d=F(2*counts[i],len(t))
    return tuple(k.pos(k.add(k.sub(D,k.exact(C*d)),k.half(k.add(x,y))))
                 for C,x,y in zip(PRICES,qa,qb))

def scaled(q,t):return (k.floor(q[0]*t),k.ceil(q[1]*t))

def main():
    start=time.monotonic(); pilot='pilot' in sys.argv
    out={'prices':[str(C) for C in PRICES], 'scale':str(k.SCALE), 'cases':0,
         'strict_failures':[0]*3,'certified_dominance':[0]*3,'boundary_overlap':[0]*3,'first_failure':None,'max_gap':[None]*3}
    for ai in range(1,15):
      a=table(ai); qa=reserve(a,(0,1))
      for ui in range(16):
       for vi in range(16):
        u,v=table(ui),table(vi); t=F(sum(x!=y for x,y in zip(u,v)),4)
        m=construct(a,u,v,False); f=construct(a,u,v)
        qm=reserve(m,(0,1,2)); qe=reserve(f,(4,0,1,2,3))
        bank=tuple(k.add(scaled(q,t),r) for q,r in zip(qa,qm))
        gap=tuple(k.sub(q,r) for q,r in zip(qe,bank))
        row={'a':ai,'u':ui,'v':vi,'t':str(t),'Qseed':qa,'Qprofile':qm,'Qearly':qe,'bank':bank,'gap':gap}
        for j,g in enumerate(gap):
            if g[0]>0:
                out['strict_failures'][j]+=1
                if out['first_failure'] is None:out['first_failure']=row
            elif g[1]<=0:out['certified_dominance'][j]+=1
            else:out['boundary_overlap'][j]+=1
            old=out['max_gap'][j]
            if old is None or g[0]>old['gap'][j][0]:out['max_gap'][j]=row
        out['cases']+=1
        k.check(time.monotonic()-start<55)
        if pilot and out['cases']>=32:break
       if pilot and out['cases']>=32:break
      if pilot and out['cases']>=32:break
    out['seconds']=time.monotonic()-start;out['assertions']=k.ASSERTIONS
    (ROOT/'out'/('PILOT.json' if pilot else 'EXHAUSTIVE.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:out[key] for key in ['cases','strict_failures','certified_dominance','boundary_overlap','seconds','assertions']}))
    print('FIRST',json.dumps(out['first_failure']))
if __name__=='__main__':main()
