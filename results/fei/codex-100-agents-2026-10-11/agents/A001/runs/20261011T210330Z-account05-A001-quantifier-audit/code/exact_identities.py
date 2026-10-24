from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import json, time, argparse

def logs(q):
    result=defaultdict(F)
    for v,sgn in [(q.numerator,1),(q.denominator,-1)]:
        d=2
        while d*d<=v:
            while v%d==0:
                result[d]+=sgn; v//=d
            d+=1
        if v>1: result[v]+=sgn
    return dict(result)

def add(*terms):
    out=defaultdict(F)
    for a,c in terms:
        for p,v in a.items(): out[p]+=c*v
    return {p:v for p,v in out.items() if v}

def entropy(p):
    return add(*[(logs(q),-q) for q in p if q])

def spectrum(v):
    a=list(v); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [F(x,len(a)) for x in a]

def stats(v):
    a=spectrum(v); p=[x*x for x in a]
    return a,p,entropy(p),sum((q*i.bit_count() for i,q in enumerate(p)),F())

def check(nmax):
    start=time.monotonic(); cases=assertions=0
    def eq(a,b):
        nonlocal assertions
        assert a==b,(a,b)
        assertions+=1
    for n in range(nmax+1):
        N=1<<n
        for mask in range(1<<N):
            v=[1 if (mask>>x)&1 else -1 for x in range(N)]
            a,p,H,I=stats(v); cases+=1
            eq(sum(p),F(1))
            inf=[sum((q for s,q in enumerate(p) if (s>>i)&1),F()) for i in range(n)]
            D=sum((min(q,1-q) for q in inf),F())
            charI=[]
            for u in range(N):
                charI.append(sum((q*(s^u).bit_count() for s,q in enumerate(p)),F()))
                eq(entropy([p[s^u] for s in range(N)]),H)
            eq(min(charI),D)
            for i in range(n):
                v0=[v[x] for x in range(N) if not (x>>i)&1]
                v1=[v[x] for x in range(N) if (x>>i)&1]
                aa,pp,H0,I0=stats(v0); bb,qq,H1,I1=stats(v1)
                marginal=[(x+y)/2 for x,y in zip(pp,qq)]
                direct=[p[s]+p[s|(1<<i)] for s in range(N) if not (s>>i)&1]
                eq(marginal,direct)
                B=add((H,1),(entropy(marginal),-1))
                JS=add((entropy(marginal),1),(H0,F(-1,2)),(H1,F(-1,2)))
                eq(add((H,1),(H0,F(-1,2)),(H1,F(-1,2))),add((B,1),(JS,1)))
                eq(I,inf[i]+(I0+I1)/2)
            product=[q*r for q in p for r in p]
            eq(entropy(product),add((H,2)))
            # z is the next physical input, so g is balanced regardless of f.
            gv=v+[-x for x in v]
            ga,gp,GH,GI=stats(gv)
            eq(GH,H); eq(GI,I+1)
            Ng=len(gv)
            mv=[]
            for x in range(4*Ng):
                gx=gv[x%Ng]; y1=1 if (x//Ng)&1 else -1; y2=1 if (x//Ng)&2 else -1
                mv.append(y1 if gx==1 else y2)
            _,_,MH,MI=stats(mv)
            eq(MH,add(({2:F(2)},1),(GH,F(1,2))))
            eq(MI,1+GI/2)
            for r in [1,2]:
                prob=F(1,1<<r)
                av=[gv[x%Ng] if x//Ng==0 else 1 for x in range(Ng*(1<<r))]
                _,_,AH,AI=stats(av)
                expected=add((GH,prob),({2:2*r*prob*(2-prob)},1),(logs((1-prob)**2),-(1-prob)**2))
                eq(AH,expected); eq(AI,prob*(GI+r))
            if time.monotonic()-start>60: raise RuntimeError('Frozen runtime cap exceeded')
    return dict(nmax=nmax,cases=cases,assertions=assertions,runtime_seconds=time.monotonic()-start,failures=0,arithmetic='Fraction and exact rational prime-log coefficients',scope='Finite identity validation only; analytic proofs in REPORT.md supply universal implications')

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--nmax',type=int,choices=[2,3],required=True); args=parser.parse_args()
    result=check(args.nmax)
    out=Path(__file__).resolve().parents[1]/'out'/f'EXACT_CHECK_n{args.nmax}.json'
    out.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
