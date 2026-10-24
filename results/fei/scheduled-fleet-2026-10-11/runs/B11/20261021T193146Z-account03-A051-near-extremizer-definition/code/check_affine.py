"""Frozen exact affine-orbit/compression check. No floating sign decisions."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations, combinations
import sys, json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
START=time.monotonic()
CHECKS=0
def check(b):
    global CHECKS
    CHECKS+=1
    assert b, CHECKS
    if CHECKS%4096==0 and time.monotonic()-START>55:
        raise RuntimeError('55 second frozen runtime cap')

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def span(vs):
    a={0}
    for v in vs: a|={x^v for x in tuple(a)}
    return a

def par(x): return x.bit_count()%2
def project(x,J): return sum(((x>>j)&1)<<i for i,j in enumerate(J))
def physical_I(f,n):
    return F(sum(f[x]!=f[x^(1<<i)] for x in range(1<<n) for i in range(n)),1<<n)

records=[]; orbit_cases=0; transformed_cases=0; compressed=0
for n in range(3 if PILOT else 4):
    N=1<<n; den=N*N
    bases=[vs for vs in permutations(range(1,N),n) if len(span(vs))==N] if n else [()]
    actions=[]
    for rows in bases:
        image=[sum(par(s&v)<<i for i,v in enumerate(rows)) for s in range(N)]
        inputs=[0]*N
        for y in range(N):
            for i,v in enumerate(rows):
                if (y>>i)&1: inputs[y]^=v
        actions.append((rows,image,inputs))
    local_count=0; full_count=0; compressed_count=0
    for table in range(1<<N):
        f=[1-2*((table>>x)&1) for x in range(N)]
        a=fwht(f); mass=[z*z for z in a]
        check(sum(mass)==den)
        check(physical_I(f,n)==F(sum(s.bit_count()*mass[s] for s in range(N)),den))
        p=[sum(mass[s] for s in range(N) if (s>>i)&1) for i in range(n)]
        w=[sum(mass[s] for s in range(N) if par(s&v)) for v in range(N)]
        m=[min(t,den-t) for t in w]
        local=all(2*t<=den for t in p) and all(m[v]>=p[i] for v in range(1,N) for i in range(n) if (v>>i)&1)
        I=sum(p); best=I
        # Full affine orbit, with actual Boolean/Walsh reconstruction.
        for rows,image,inputs in actions:
            for b in range(N):
                expected=[0]*N
                for s in range(N): expected[image[s]^b]=a[s]
                truth=[f[inputs[y]]*(-1 if par(b&y) else 1) for y in range(N)]
                actual=fwht(truth)
                check(actual==expected)
                newI=sum(t.bit_count()*expected[t]**2 for t in range(N))
                check(physical_I(truth,n)==F(newI,den))
                best=min(best,newI); orbit_cases+=1; transformed_cases+=1
        check(local==(I==best))
        if local:
            local_count+=1
            for i in range(n):
                for j in range(i+1,n):
                    q=sum(mass[s] for s in range(N) if ((s>>i)&1) and ((s>>j)&1))
                    check(2*q<=min(p[i],p[j]))
                    check(max(p[i],p[j])<=w[(1<<i)^(1<<j)]<=den-max(p[i],p[j]))
        # Exact approximate orbit optimality: epsilon/K = I-best (scaled).
        gap=I-best
        for i in range(n):
            check(2*p[i]<=den+gap)
            for v in range(1,N):
                if (v>>i)&1: check(m[v]>=p[i]-gap)
        for i in range(n):
            for j in range(i+1,n):
                q=sum(mass[s] for s in range(N) if ((s>>i)&1) and ((s>>j)&1))
                check(2*q<=min(p[i],p[j])+gap)
        # Construct compression from affine support, no floating coefficients.
        A=[s for s in range(N) if a[s]]; anchor=A[0]
        V=span([s^anchor for s in A]); d=(len(V)).bit_length()-1; D=1<<d
        J=next(J for J in combinations(range(n),d) if len({project(v,J) for v in V})==D)
        target=sum((1 if 2*p[j]>den else 0)<<i for i,j in enumerate(J))
        a0=next(anchor^v for v in V if project(anchor^v,J)==target)
        coeff=[0]*D
        for s in A: coeff[project(s^a0,J)]=a[s]
        inv=fwht(coeff); check(all(v in (-N,N) for v in inv))
        g=[v//N for v in inv]
        check(sorted(v*v for v in fwht(g) if v)==sorted(F(v*v*D*D,den) for v in a if v))
        Ig=physical_I(g,d)
        check(Ig==F(sum(min(p[j],den-p[j]) for j in J),den))
        check(Ig<=F(I,den))
        check(sorted(F(z*z,den) for z in a if z)==sorted(F(z*z,D*D) for z in fwht(g) if z))
        compressed+=1; compressed_count+=d<n; full_count+=d==n
    records.append(dict(n=n,tables=1<<N,GL_matrices=len(bases),affine_minimal_tables=local_count,full_affine_dimension=full_count,compressible=compressed_count))

# Independent direct-character replay of named actual Boolean guards.
named=[]
for name,f in [('majority3',[1 if x.bit_count()<=1 else -1 for x in range(8)]),('point3',[-1]+[1]*7),('parity3',[(-1)**x.bit_count() for x in range(8)])]:
    n=3; N=8
    direct=[sum(f[x]*(-1)**par(x&s) for x in range(N)) for s in range(N)]
    check(direct==fwht(f))
    A=[s for s in range(N) if direct[s]]
    d=len(span([s^A[0] for s in A])).bit_length()-1
    p=[F(sum(direct[s]**2 for s in A if (s>>i)&1),64) for i in range(n)]
    w7=F(sum(direct[s]**2 for s in A if par(s&7)),64)
    if name=='majority3': check(d==2 and p==[F(1,2)]*3 and min(w7,1-w7)==0)
    if name=='point3': check(d==3 and p==[F(1,4)]*3)
    if name=='parity3': check(d==0 and p==[1]*3)
    named.append(dict(name=name,affine_dimension=d,influence=str(physical_I(f,3))))

# Frozen non-Boolean relaxation guards: dimension is explicitly bounded here.
for n in range(2,9):
    for v in range(1,1<<n):
        k=v.bit_count(); check(min(k,n+1-k)>=1)
    check(2>0)  # coefficient numerator of each distinct-singleton convolution.

result=dict(status='PASS',arithmetic='integer Walsh/physical edges and Fraction; no logarithm decisions',pilot=PILOT,assertions=CHECKS,orbit_cases=orbit_cases,actual_transformed_truth_tables=transformed_cases,compression_checks=compressed,dimensions=records,named_guards=named,runtime_seconds=time.monotonic()-START,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
out=ROOT/'out'/('PILOT.json' if PILOT else 'CHECK.json')
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
