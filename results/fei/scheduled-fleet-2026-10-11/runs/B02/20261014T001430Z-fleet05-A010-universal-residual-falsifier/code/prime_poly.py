from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import reference_v1 as ref
import json,time,math,sys

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'

def extract(A,gates,orders,n):
    supports=[g[0] for g in gates]; js=[j for j in range(n) if A>>j&1]; poly={}
    for assignment in product(*[[l for l,m in enumerate(supports) if m>>j&1] for j in js]):
        parts={}
        for j,l in zip(js,assignment): parts[l]=parts.get(l,0)|(1<<j)
        used=tuple(parts); sources=ref.graph_roots(used,parts,supports); d=0
        for l in used:
            s=parts[l].bit_count(); kap=(A&supports[l]).bit_count()
            assert s<=kap<=2
            if s<kap: d+=1
            for j in js:
                if parts[l]>>j&1:
                    rank=orders[l].index(j)+1; pred=sum(A>>i&1 for i in orders[l][:rank-1])
                    if pred+1<rank: d+=1
        choices=[[None]+[l for l in used if l!=k and parts[l]&supports[k]] for k in used]
        for pp in product(*choices):
            pd=dict(zip(used,pp)); roots={k for k in used if pd[k] is None}
            if len(roots)!=len(sources) or any(len(c&roots)!=1 for c in sources): continue
            good=True
            for k in used:
                trail=set(); v=k
                while v is not None:
                    if v in trail: good=False; break
                    trail.add(v); v=pd[v]
                if not good: break
            if not good: continue
            edges=[(pd[k],k) for k in used if pd[k] is not None]
            mult=0
            for attach in product(*[[j for j in js if (parts[p]&supports[k])>>j&1] for p,k in edges]):
                counts={}
                for (p,k),j in zip(edges,attach): counts[p,j]=counts.get((p,j),0)+1
                mult+=math.prod(math.factorial(v) for v in counts.values())
            key=(sum(1<<l for l in used),d)
            poly[key]=poly.get(key,Q(0))+Q(mult,4**len(roots))
    return poly

def eval_interval(poly,lam):
    lo=hi=Q(0)
    for (mask,d),coef in poly.items():
        a,b=ref.power_interval(Q(1,1<<d))
        factor=coef*math.prod(lam[l] for l in range(len(lam)) if mask>>l&1)
        lo+=factor*a; hi+=factor*b
    return lo,hi

def residual(poly_table,lam,walsh,n):
    T=math.prod(1+x/4 for x in lam)-1; lo=hi=Q(0); den=(1<<n)**2
    for A,a in enumerate(walsh):
        if A and a:
            l,h=eval_interval(poly_table[A],lam)
            if not l: return None
            x,_=ref.log_interval(T/h); _,y=ref.log_interval(T/l)
            lo+=Q(a*a,den)*x; hi+=Q(a*a,den)*y
    I=Q(sum(A.bit_count()*a*a for A,a in enumerate(walsh)),den)
    return lo/I,hi/I

def main():
    start=time.monotonic(); tables=[]; grid_results=[]; comparisons=0
    for t in [855,64680]:
        n=4; gates=ref.primes(t,n); N=len(gates); a=ref.walsh(t,n)
        natural=[[j for j in range(n) if m>>j&1] for m,v in gates]
        assert all(len(o)==2 for o in natural)
        for flips in product([0,1],repeat=N):
            assert time.monotonic()-start<120
            orders=[o[::-1] if f else o for o,f in zip(natural,flips)]
            polys={A:extract(A,gates,orders,n) for A in range(1,1<<n) if a[A]}
            if not any(flips):
                read=max(sum(m>>j&1 for m,v in gates) for j in range(n)); lam=Q(1,read)
                for A,poly in polys.items():
                    lo,hi=eval_interval(poly,[lam]*N); oldlo,oldhi,count=ref.mass(A,gates,lam,n)
                    assert lo<=oldhi and oldlo<=hi
                    comparisons+=1
            rec={'truth':t,'gates':gates,'orders':orders,'flips':list(flips),'walsh':a,'polynomials':{str(A):[[mask,d,str(coef)] for (mask,d),coef in sorted(poly.items())] for A,poly in polys.items()}}
            tables.append(rec)
            best=None
            for lam in product([Q(1,4),Q(1,2),Q(3,4),Q(1)],repeat=N):
                if any(sum(lam[l] for l,(m,v) in enumerate(gates) if m>>j&1)>1 for j in range(n)): continue
                val=residual(polys,lam,a,n)
                if val and (best is None or val[1]<best[1]): best=(val[0],val[1],lam)
            grid_results.append({'truth':t,'flips':list(flips),'best_lo':str(best[0]),'best_hi':str(best[1]),'best_ratio':float((best[0]+best[1])/2),'lambda':[str(v) for v in best[2]]})
            (OUT/'poly_checkpoint.json').write_text(json.dumps({'tables':tables,'grid_results':grid_results,'comparisons':comparisons},indent=2))
    result={'tables':tables,'grid_results':grid_results,'comparisons':comparisons,'elapsed_seconds':time.monotonic()-start}
    (OUT/'prime_polynomials.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'comparisons':comparisons,'elapsed_seconds':result['elapsed_seconds'],'grid_results':grid_results},indent=2))

if __name__=='__main__': main()
