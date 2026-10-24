from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import reference_v1 as ref
import json,time,sys
OUT=Path(__file__).resolve().parents[1]/'out'; TARGET=Q(32,25)

def solve(rec,index,deadline):
    coeff={int(A):{} for A in rec['polynomials']}
    for A,terms in rec['polynomials'].items():
        for mask,d,c in terms:
            _,upper=ref.power_interval(Q(1,1<<d))
            coeff[int(A)][mask]=coeff[int(A)].get(mask,Q(0))+Q(c)*upper
    a=ref.walsh(rec['truth'],4); I=sum(A.bit_count()*v*v for A,v in enumerate(a))
    @lru_cache(maxsize=2048)
    def vertex(lam):
        T=__import__('math').prod(1+l/4 for l in lam)-1
        if not T:
            return {A:max((4*c for mask,c in p.items() if mask.bit_count()==1),default=Q(0)) for A,p in coeff.items()}
        products={m:__import__('math').prod(lam[j] for j in range(3) if m>>j&1) for m in range(1,8)}
        return {A:sum(c*products[m] for m,c in p.items())/T for A,p in coeff.items()}
    stack=[('',(Q(0),)*3,(Q(1),)*3)]; leaves=[]; nodes=0; minimum=None
    while stack:
        assert time.monotonic()<deadline,'deadline'
        path,lo,hi=stack.pop(); nodes+=1
        assert nodes<=8000,'node cap'
        if any(sum(lo[l] for l,(m,v) in enumerate(rec['gates']) if m>>j&1)>1 for j in range(4)):
            leaves.append({'path':path,'verdict':'packing_excluded'}); continue
        maxima={A:Q(0) for A in coeff}
        for lam in product(*[(x,y) for x,y in zip(lo,hi)]):
            for A,val in vertex(lam).items(): maxima[A]=max(maxima[A],val)
        lower=None if any(not v for v in maxima.values()) else -sum(Q(a[A]**2,I)*ref.log_interval(m)[1] for A,m in maxima.items())
        if lower is None or lower>=TARGET:
            leaves.append({'path':path,'verdict':'certified','lower':str(lower) if lower is not None else 'infinity'})
            if lower is not None: minimum=lower if minimum is None else min(lower,minimum)
            continue
        if len(path)>=42:
            (OUT/'p4_unresolved.json').write_text(json.dumps({'index':index,'path':path,'lower':str(lower)})); raise RuntimeError('depth cap')
        axis=max(range(3),key=lambda j:hi[j]-lo[j]); mid=(lo[axis]+hi[axis])/2
        lh=list(hi); lh[axis]=mid; rl=list(lo); rl[axis]=mid
        stack.extend([(path+'1',tuple(rl),hi),(path+'0',lo,tuple(lh))])
    result={'index':index,'truth':rec['truth'],'orders':rec['orders'],'target':str(TARGET),'nodes':nodes,'minimum_lower':str(minimum),'leaves':leaves}
    (OUT/f'p4_continuum_{index:02}.json').write_text(json.dumps(result,indent=2))
    print({k:v for k,v in result.items() if k!='leaves'},flush=True)
    return result

if __name__=='__main__':
    start=time.monotonic(); pilot='pilot' in sys.argv; rows=json.loads((OUT/'p4_candidates.json').read_text())['rows']; results=[]
    if pilot: rows=rows[:1]
    for i,rec in enumerate(rows):
        results.append(solve(rec,i,start+(60 if pilot else 1200)))
        ref.log_interval.cache_clear(); ref.ln_interval.cache_clear()
    (OUT/('p4_continuum_pilot.json' if pilot else 'p4_continuum_summary.json')).write_text(json.dumps({'tables':len(results),'nodes':sum(r['nodes'] for r in results),'leaves':sum(len(r['leaves']) for r in results),'target':str(TARGET),'elapsed_seconds':time.monotonic()-start},indent=2))
