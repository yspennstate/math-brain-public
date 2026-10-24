from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
from itertools import product
import reference_v1 as ref
import json,sys,time

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; SCALE=1<<80

def unpack_table(rec):
    coeff={}
    for A,terms in rec['polynomials'].items():
        combined={}
        for mask,d,c in terms:
            lo,hi=ref.power_interval(Q(1,1<<d)); combined[mask]=combined.get(mask,Q(0))+Q(c)*hi
        coeff[int(A)]={mask:(val*SCALE).__ceil__() for mask,val in combined.items()}
    walsh=rec['walsh']; I=sum(A.bit_count()*a*a for A,a in enumerate(walsh))
    # p(A)/I(f) cancels 2^(2n).
    weights={A:Q(walsh[A]**2,I) for A in coeff}
    return coeff,weights

def prepare(rec):
    coeff,weights=unpack_table(rec); supp=[m for m,v in rec['gates']]
    @lru_cache(maxsize=4096)
    def vertex(lam):
        T=1
        for l in lam: T*=1+l/4
        T-=1
        if not T:
            return {A:max((Q(c,SCALE)*4 for mask,c in poly.items() if mask.bit_count()==1),default=Q(0)) for A,poly in coeff.items()}
        products={mask:Q(1) for mask in range(1,16)}
        for mask in products:
            for l in range(4):
                if mask>>l&1: products[mask]*=lam[l]
        return {A:sum(c*products[mask] for mask,c in poly.items())/(SCALE*T) for A,poly in coeff.items()}
    def feasible(lo): return all(sum(lo[l] for l,m in enumerate(supp) if m>>j&1)<=1 for j in range(4))
    def bound(lo,hi):
        maxima={A:Q(0) for A in coeff}
        for lam in product(*[(a,b) if a!=b else (a,) for a,b in zip(lo,hi)]):
            for A,value in vertex(lam).items(): maxima[A]=max(maxima[A],value)
        total=Q(0)
        for A,w in weights.items():
            if not maxima[A]: return None # identically missing spectral output: infinite lower cost
            a,b=ref.log_interval(maxima[A]); total-=w*b
        return total
    return feasible,bound

def solve(rec,pilot=False):
    start=time.monotonic(); feasible,bound=prepare(rec)
    stack=[('',(Q(0),)*4,(Q(1),)*4)]; leaves=[]; visited=0; min_bound=None
    cap=4000
    while stack:
        if time.monotonic()-start>(60 if pilot else 1200): raise RuntimeError('hard deadline at box boundary')
        path,lo,hi=stack.pop(); visited+=1
        if visited>cap: raise RuntimeError('frozen node cap')
        if not feasible(lo): leaves.append({'path':path,'verdict':'packing_excluded'}); continue
        lower=bound(lo,hi)
        if lower is None or lower>=1:
            leaves.append({'path':path,'verdict':'certified','lower':str(lower) if lower is not None else 'infinity'})
            if lower is not None: min_bound=lower if min_bound is None else min(min_bound,lower)
            continue
        if len(path)>=32:
            (OUT/'continuum_unresolved.json').write_text(json.dumps({'flips':rec['flips'],'path':path,'lo':[str(x) for x in lo],'hi':[str(x) for x in hi],'lower':str(lower)})); raise RuntimeError('frozen depth cap')
        axis=max(range(4),key=lambda j:hi[j]-lo[j]); mid=(lo[axis]+hi[axis])/2
        left_hi=list(hi); left_hi[axis]=mid; right_lo=list(lo); right_lo[axis]=mid
        stack.append((path+'1',tuple(right_lo),hi)); stack.append((path+'0',lo,tuple(left_hi)))
        if visited%100==0:
            (OUT/'continuum_checkpoint.json').write_text(json.dumps({'flips':rec['flips'],'visited':visited,'leaves':len(leaves),'pending':len(stack),'elapsed':time.monotonic()-start}))
    result={'truth':rec['truth'],'flips':rec['flips'],'nodes':visited,'minimum_leaf_lower':str(min_bound),'leaves':leaves,'elapsed_seconds':time.monotonic()-start}
    name='continuum_'+''.join(str(x) for x in rec['flips'])+'.json'; (OUT/name).write_text(json.dumps(result,indent=2))
    print({k:v for k,v in result.items() if k!='leaves'},flush=True)
    return result

def main():
    start=time.monotonic(); data=json.loads((OUT/'prime_polynomials.json').read_text()); records=[r for r in data['tables'] if r['truth']==64680]
    pilot=len(sys.argv)>1 and sys.argv[1]=='pilot'
    if pilot: records=records[:1]
    results=[]
    for rec in records:
        if time.monotonic()-start>1200: raise RuntimeError('total hard deadline')
        results.append(solve(rec,pilot))
        ref.log_interval.cache_clear(); ref.ln_interval.cache_clear()
    (OUT/('continuum_pilot.json' if pilot else 'continuum_summary.json')).write_text(json.dumps({'orders':len(results),'total_nodes':sum(r['nodes'] for r in results),'elapsed_seconds':time.monotonic()-start,'minimum_lower':str(min(Q(r['minimum_leaf_lower']) for r in results))},indent=2))

if __name__=='__main__': main()
