from pathlib import Path
from fractions import Fraction as Q
from itertools import product,combinations,permutations
from functools import lru_cache
import json,time

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; ZUP=Q(435276,1000000)
assert ZUP**5>=Q(1,64)

def sources(parts,supp):
    used=set(parts)
    adj={i:{j for j in used if i!=j and parts[i]&supp[j]} for i in used}
    reach={}
    for i in used:
        seen={i}; queue=[i]
        while queue:
            v=queue.pop()
            for w in adj[v]-seen: seen.add(w); queue.append(w)
        reach[i]=seen
    comps={frozenset(j for j in used if j in reach[i] and i in reach[j]) for i in used}
    return [set(c) for c in comps if all(not(adj[i]&c) for i in used-c)]

def queue_poly(A,rec):
    n=4; supp=[m for m,v in rec['gates']]; orders=rec['orders']; js=[j for j in range(n) if A>>j&1]; poly={}
    for assignment in product(*[[l for l,m in enumerate(supp) if m>>j&1] for j in js]):
        parts={}
        for j,l in zip(js,assignment): parts[l]=parts.get(l,0)|(1<<j)
        used=set(parts); rootcomps=sources(parts,supp); d=0
        for l,B in parts.items():
            # Direct cost power: subset ratio plus strict predecessor rank ratio.
            D=Q(B.bit_count(),(A&supp[l]).bit_count())**B.bit_count()
            for j in js:
                if B>>j&1:
                    rank=orders[l].index(j)+1; pred=sum(A>>i&1 for i in orders[l][:rank-1])
                    D*=Q(pred+1,rank)
            assert D.numerator==1 and D.denominator&(D.denominator-1)==0
            d+=D.denominator.bit_length()-1
        count=0
        for roots in product(*[sorted(c) for c in rootcomps]):
            rootset=tuple(sorted(roots)); traces=set()
            def grow(queue,discovered,trace):
                if not queue:
                    if discovered==used: traces.add((rootset,tuple(trace)))
                    return
                parent=queue[0]; available=sorted(used-discovered)
                for k in range(len(available)+1):
                    for group in combinations(available,k):
                        for children in permutations(group):
                            choices=[[j for j in js if (parts[parent]&supp[child])>>j&1] for child in children]
                            for attach in product(*choices):
                                if tuple(sorted(attach))!=attach: continue
                                grow(queue[1:]+list(children),discovered|set(children),trace+[(parent,parts[parent],tuple(zip(attach,children)))])
            grow(list(rootset),set(rootset),[]); count+=len(traces)
        key=(sum(1<<l for l in used),d); poly[key]=poly.get(key,Q(0))+Q(count,4**len(rootcomps))
    return poly

@lru_cache(maxsize=8192)
def log_bounds(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length(); y=x/Q(2)**k
    if y<1: y*=2; k-=1
    assert 1<=y<2
    def ln(y):
        z=(y-1)/(y+1); term=z; total=Q(0)
        for j in range(12): total+=term/(2*j+1); term*=z*z
        lo=2*total; hi=lo+2*term/(25*(1-z*z)); return lo,hi
    a,b=ln(y); c,d=ln(Q(2))
    lo,hi=(a+k*c,b+k*d) if k>=0 else (a+k*d,b+k*c)
    return min(lo/c,lo/d,hi/c,hi/d),max(lo/c,lo/d,hi/c,hi/d)

def decode(path):
    lo=[Q(0)]*4; hi=[Q(1)]*4
    for digit in path:
        axis=max(range(4),key=lambda j:hi[j]-lo[j]); mid=(lo[axis]+hi[axis])/2
        if digit=='0': hi[axis]=mid
        elif digit=='1': lo[axis]=mid
        else: raise AssertionError('nonbinary path')
    return lo,hi

def verify_leaf(leaf,rec):
    lo,hi=decode(leaf['path']); supp=[m for m,v in rec['gates']]
    if leaf['verdict']=='packing_excluded':
        assert any(sum(lo[l] for l,m in enumerate(supp) if m>>j&1)>1 for j in range(4)); return None
    maxima={int(A):Q(0) for A in rec['polynomials']}
    for lam in product(*[(a,b) if a!=b else (a,) for a,b in zip(lo,hi)]):
        T=1
        for l in lam: T*=1+l/4
        T-=1
        for A,terms in rec['polynomials'].items():
            A=int(A)
            if not T:
                val=max((Q(c)*ZUP**d*4 for mask,d,c in terms if mask.bit_count()==1),default=Q(0))
            else:
                val=sum(Q(c)*ZUP**d*__import__('math').prod(lam[l] for l in range(4) if mask>>l&1) for mask,d,c in terms)/T
            maxima[A]=max(maxima[A],val)
    a=rec['walsh']; I=sum(A.bit_count()*v*v for A,v in enumerate(a)); lower=Q(0)
    for A,mass in maxima.items():
        if not mass: return None
        _,upper=log_bounds(mass); lower-=Q(a[A]**2,I)*upper
    assert lower>=1,(rec['flips'],leaf['path'],float(lower))
    return lower

def main():
    start=time.monotonic(); records=json.loads((OUT/'prime_polynomials.json').read_text())['tables']; matches=0; leafcount=0; minima=[]; runs=0
    for rec in records:
        for A,terms in rec['polynomials'].items():
            assert time.monotonic()-start<120
            actual=queue_poly(int(A),rec); expected={(m,d):Q(c) for m,d,c in terms}
            assert actual==expected,(rec['truth'],rec['flips'],A)
            matches+=1
        if rec['truth']!=64680: continue
        certificate=json.loads((OUT/('continuum_'+''.join(str(x) for x in rec['flips'])+'.json')).read_text())
        leaves=certificate['leaves']; paths=sorted(l['path'] for l in leaves)
        assert len(set(paths))==len(paths)
        assert sum(Q(1,1<<len(p)) for p in paths)==1
        assert all(not b.startswith(a) for a,b in zip(paths,paths[1:]))
        for leaf in leaves:
            v=verify_leaf(leaf,rec); leafcount+=1
            if v is not None: minima.append(v)
        log_bounds.cache_clear()
    result={'exact_polynomial_matches':matches,'covered_order_tables':16,'verified_leaves':leafcount,'minimum_independent_lower':str(min(minima)),'minimum_independent_lower_float':float(min(minima)),'elapsed_seconds':time.monotonic()-start,'z_upper':str(ZUP),'review_scope':'Self-validation by distinct code; independent-agent review pending'}
    (OUT/'independent_check.json').write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))

if __name__=='__main__': main()
