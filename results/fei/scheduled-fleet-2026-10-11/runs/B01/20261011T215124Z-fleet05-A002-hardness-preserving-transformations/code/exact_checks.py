from fractions import Fraction as Q
from collections import defaultdict
from itertools import combinations,product
from pathlib import Path
import argparse,json,time
RUN=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    checks+=1
    assert x,checks
def spectrum(vals):
    N=len(vals)
    return {s:Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals)),N) for s in range(N) if sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals))}
def factors(v):
    d=2
    while d*d<=v:
        k=0
        while v%d==0: v//=d;k+=1
        if k: yield d,k
        d+=1
    if v>1: yield v,1
def ent(a):
    out=defaultdict(Q)
    for c in a.values():
        p=c*c
        for v,sign in [(p.denominator,1),(p.numerator,-1)]:
            for prime,k in factors(v): out[prime]+=sign*k*p
    return {k:v for k,v in out.items() if v}
def hprob(p): return ent({0:p}) # not used: probabilities need direct helper
def phi(p):
    out=defaultdict(Q)
    if p:
        for v,sign in [(p.denominator,1),(p.numerator,-1)]:
            for prime,k in factors(v): out[prime]+=sign*k*p
    return dict(out)
def add(*terms):
    out=defaultdict(Q)
    for scale,term in terms:
        for k,v in term.items(): out[k]+=scale*v
    return {k:v for k,v in out.items() if v}
def inf(a,n): return [sum(c*c for s,c in a.items() if s>>i&1) for i in range(n)]
def val(a,x): return sum(c*(-1 if (s&x).bit_count()%2 else 1) for s,c in a.items())
def codemask(s,n):
    z=0
    for i,c in enumerate([3,5,6][:n]):
        if s>>i&1:z^=c
    return s|(z<<n)
def restriction(a,B,rho):
    out=defaultdict(Q)
    for s,c in a.items():out[s&~B]+=c*(-1 if (s&rho).bit_count()%2 else 1)
    return {s:c for s,c in out.items() if c}
def smooth(a,n):
    # Replace three coded auxiliary variables by Maj3 of three disjoint parity pairs.
    gad=[(3,Q(1,2)),(12,Q(1,2)),(48,Q(1,2)),(63,Q(-1,2))]
    out={}
    for s,c in a.items():
        pieces=[(s&((1<<n)-1),c)]
        for j in range(3):
            if s>>(n+j)&1:
                pieces=[(u|(t<<(n+6*j)),v*w) for u,v in pieces for t,w in gad]
        for u,v in pieces: ck(u not in out);out[u]=v
    return out
def run(nmax):
    started=time.perf_counter();seeds=0;smoothing=0
    for n in range(nmax+1):
        for truth in range(1<<(1<<n)):
            seeds+=1
            vals=[1 if truth>>x&1 else -1 for x in range(1<<n)]
            a=spectrum(vals);ii=inf(a,n);H=ent(a)
            ck(sum(c*c for c in a.values())==1)
            tensor={s|(t<<n):c*d for s,c in a.items() for t,d in a.items()}
            ck(ent(tensor)==add((2,H)))
            ck(sum(inf(tensor,2*n))==2*sum(ii))
            bal={s|(1<<n):c for s,c in a.items()}
            ck(ent(bal)==H);ck(sum(inf(bal,n+1))==1+sum(ii));ck(0 not in bal)
            # Explicit two-cell selector on the balanced seed.
            mux={1<<(n+1):Q(1,2),1<<(n+2):Q(1,2)}
            for s,c in bal.items():mux[s|(1<<(n+1))]=c/2;mux[s|(1<<(n+2))]=-c/2
            ck(ent(mux)==add((1,{2:Q(2)}),(Q(1,2),H)))
            ck(sum(inf(mux,n+3))==1+Q(1,2)*(1+sum(ii)))
            for r in [1,2]:
                p=Q(1,1<<r);N=n+r
                activated=[vals[x&((1<<n)-1)] if x>>n==0 else 1 for x in range(1<<N)]
                ag=spectrum(activated);mean=a.get(0,Q(0));d=1-mean
                expected={0:1-p*d}
                for t in range(1<<r):
                    if t and d:expected[t<<n]=-p*d
                    for s,c in a.items():
                        if s:expected[s|(t<<n)]=p*c
                expected={s:c for s,c in expected.items() if c}
                ck(ag==expected);ck(sum(inf(ag,N))==p*(sum(ii)+r*d))
                rhs=add((p,add((1,H),(-1,phi(mean*mean)))),(1,{2:2*r*p*(1-mean*mean)}),(1,phi(p*p*d*d)))
                # Nonempty pure-control coefficient group has 2^r-1 members.
                rhs=add((p,add((1,H),(-1,phi(mean*mean)))),(1,{2:2*r*p*(1-mean*mean)}),((1<<r)-1,phi(p*p*d*d)),(1,phi((1-p*d)**2)))
                ck(ent(ag)==rhs)
            code={codemask(s,n):c for s,c in a.items()}
            codedvals=[]
            for x in range(1<<(n+3)):
                y=x&((1<<n)-1);z=x>>n
                for i,col in enumerate([3,5,6][:n]):
                    if (col&z).bit_count()%2:y^=1<<i
                codedvals.append(vals[y])
            ck(spectrum(codedvals)==code)
            ck(ent(code)==H)
            jj=inf(code,n+3);ck(jj[:n]==ii)
            V=1-a.get(0,Q(0))**2
            ck(sum(jj)-sum(ii)==sum((s>>n).bit_count()*c*c for s,c in code.items()))
            ck(sum(jj)-sum(ii)<=3*V)
            for j in jj[n:]:ck(j<=V)
            for k in range(3):
                for Bseq in combinations(range(n+3),k):
                    B=sum(1<<i for i in Bseq)
                    for signs in product([0,1],repeat=k):
                        rho=sum(v<<i for i,v in zip(Bseq,signs));child=restriction(code,B,rho)
                        ck(sorted(c*c for c in child.values())==sorted(c*c for c in code.values()))
                        cii=inf(child,n+3)
                        ck(sum(cii)==sum(jj)-sum(jj[i] for i in Bseq))
                        ck(all(cii[i]==jj[i] for i in range(n+3) if i not in Bseq))
                        if 0 in code:ck(child.get(0,Q(0))==code[0])
            # Full Fourier support through two dummy bits and a single physical flip.
            M=n+2;p=Q(1,1<<M)
            flipped=[vals[x&((1<<n)-1)] for x in range(1<<M)];flipped[0]*=-1
            sa=spectrum(flipped)
            ck(len(sa)==1<<M)
            ck(all(sa[s]==a.get(s,Q(0))-2*p*vals[0] for s in range(1<<M)))
            si=inf(sa,M)
            ck(all(abs(si[i]-(ii[i] if i<n else 0))<=2*p for i in range(M)))
            if n==2:
                smoothing+=1;sm=smooth(code,n);mi=inf(sm,n+18)
                aux=sum(jj[n:]);gI=Q(3);gH={2:Q(2)}
                ck(ent(sm)==add((1,H),(aux,gH)))
                ck(sum(mi)==sum(ii)+gI*aux)
                ck(mi[:n]==ii)
                ck(all(mi[n+6*j+l]==jj[n+j]/2 for j in range(3) for l in range(6)))
                ck(all((s^t).bit_count()>=3 for s in sm for t in sm if s!=t))
                for x in range(32):
                    # Deterministic spaced assignments on the 20-cube, no exponential enumeration.
                    xx=(x*104729)%(1<<(n+18));zz=0
                    for j in range(3):
                        bits=[-1 if ((xx>>(n+6*j+2*l))&3).bit_count()%2 else 1 for l in range(3)]
                        if sum(bits)<0:zz|=1<<j
                    y=xx&3
                    for i,col in enumerate([3,5]):
                        if (col&zz).bit_count()%2:y^=1<<i
                    ck(val(sm,xx)==vals[y])
    out=dict(helper_version='A002-exact-ledgers-v1',nmax=nmax,seeds=seeds,smoothed_seeds=smoothing,assertions=checks,failures=0,seconds=time.perf_counter()-started,arithmetic='exact integers/Fraction/formal prime-log entropy',max_final_dimension=20 if nmax>=2 else nmax+3)
    (RUN/'out'/f'EXACT_CHECK_n{nmax}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--nmax',type=int,choices=[2,3],required=True);run(ap.parse_args().nmax)
