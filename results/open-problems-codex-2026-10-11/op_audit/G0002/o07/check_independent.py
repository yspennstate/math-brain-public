import itertools, json, math, urllib.request, urllib.parse
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
out = {}

def piv(A,w,n):
    p1={i for i in range(n) if (w & ~(1<<i)) not in A and (w | (1<<i)) in A}
    p2=set(p1)
    for j in range(n):
        if w & (1<<j):
            v=w & ~(1<<j)
            p2.update(i for i in range(n) if (v & ~(1<<i)) not in A and (v | (1<<i)) in A)
    return p1,p2

# Generate all monotone Boolean functions independently by slicing on the last bit.
families=[0,1]
cube_results=[]
for n in range(1,6):
    half=1<<(n-1)
    families=[a | (b<<half) for a in families for b in families if a & ~b == 0]
    maxima=[-1]*4
    violations=[0]*4
    for mask in families:
        A={w for w in range(1<<n) if mask>>w&1}
        vals=[0]*4
        for w in A:
            p1,p2=piv(A,w,n)
            occ={i for i in range(n) if w>>i&1}
            vals[0]+=len(p2); vals[1]+=len(p2-p1)
            vals[2]+=len(p2&occ); vals[3]+=len((p2-p1)&occ)
            # Independently test the occupied pair-deletion characterization.
            pair={i for i in occ-p1 if any(j!=i and (w&~(1<<j)) in A and (w&~(1<<j)&~(1<<i)) not in A for j in occ)}
            assert pair==(p2-p1)&occ
        band=all((2*w.bit_count()<n+2 or w in A) and (w not in A or 2*w.bit_count()>=n-4) for w in range(1<<n))
        for k,v in enumerate(vals):
            if v>maxima[k]: maxima[k]=v; violations[k]=int(not band)
            elif v==maxima[k]: violations[k]+=int(not band)
    assert not any(violations)
    cube_results.append(dict(n=n,count=len(families),maxima=maxima,band_violations=violations))
out['cube']=cube_results

# Exhaustive clause-array tests, including repeats. Check every successful support,
# not only means. Also recover C1 and the exact singleton/edge probabilities.
cnf_results=[]
for n,r,M in [(3,2,3),(3,3,2),(4,3,2)]:
    clauses=list(itertools.product(range(n),repeat=r))
    checked=0
    for arr in itertools.product(clauses,repeat=M):
        A={w for w in range(1<<n) if all(any(w>>i&1 for i in c) for c in arr)}
        for w in A:
            S=set(); edges=[]
            for c in arr:
                pos=[i for i in c if w>>i&1]
                if len(set(pos))==1: S.update(pos)
                if len(pos)==2 and pos[0]!=pos[1]: edges.append(set(pos))
            C=set().union(*edges) if edges else set()
            bad=[e for e in edges if e&S]
            V=set().union(*bad) if bad else set()
            p1,p2=piv(A,w,n)
            assert S==p1
            assert C-V <= p2-p1
            assert len(p2-p1)>=len(C)-2*len(bad)
            checked+=1
    for s in range(1,n+1):
        z=F(n-s,n); w=(1<<s)-1
        fail=single=edge=incident=0
        for c in clauses:
            pos=[i for i in c if w>>i&1]
            fail+=not pos
            single+=len(set(pos))==1
            e=len(pos)==2 and pos[0]!=pos[1]
            edge+=e; incident+=e and 0 in pos
        assert F(fail,n**r)==z**r
        assert F(single,n**r)==s*((z+F(1,n))**r-z**r)
        assert F(edge,n**r)==math.comb(r,2)*F(s*(s-1),n*n)*z**(r-2)
        assert F(incident,n**r)==r*(r-1)*F(s-1,n*n)*z**(r-2)
    cnf_results.append(dict(n=n,r=r,M=M,arrays=n**(r*M),successful_pairs=checked))
out['cnf']=cnf_results

n=10**14; h=10**7; r=10**6
assert n==h*h==100*r*r
assert r*F(2,h)==F(1,5)
assert r*(F(2,h)+F(2,n))<F(1,4)
assert F(8,15)*r*r/n>=F(r*r,2*n)
assert F(32,3)*r*r/n<1
graph=F(r*r,12)-F(288*r**3,n)
assert graph>=F(r*r,24)
lower=F(3,4)*F(1,81)*F(r*r,24)
assert lower==F(n,259200)>10*h
assert lower>12*h  # also separates a conservative six-level whole-cube bound
out['exact_constants']={k:str(v) for k,v in dict(graph_lower=graph,normalized_lower=lower,band_upper=10*h,margin=lower-10*h,whole_cube_band_upper=12*h).items()}
for d in range(1001):
    assert (2*d+1)**2*(d+2)<=4*(d+1)**3
    assert F(math.comb(2*d,d),4**d)**2<=F(1,d+1)
out['central_binomial_checks']=1001
(ROOT/'checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
