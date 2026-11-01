"""Independent finite certificates for A004 flexible floor projection. No imports from producers."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse, json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    checks+=1
    if not x: raise AssertionError(checks)

def project(pi,T,c):
    # Monotone active-set growth, independent of producer code.
    floor=[c*t for t in T]
    active={j for j,p in enumerate(pi) if not p}
    for _ in range(len(pi)+1):
        k=(F(1)-sum(floor[j] for j in active))/(F(1)-sum(pi[j] for j in active))
        added={j for j,p in enumerate(pi) if k*p<floor[j]}-active
        if not added:
            return tuple(max(f,k*p) for f,p in zip(floor,pi)), k
        active|=added
    raise AssertionError('active-set loop')

def enumerate_active(pi,T,c):
    # Independent exhaustive certificate; ties may give multiple masks, same x.
    answers=set()
    for bits in product((0,1),repeat=len(pi)):
        active=[j for j,b in enumerate(bits) if b]
        den=1-sum(pi[j] for j in active)
        if not den: continue
        k=(1-c*sum(T[j] for j in active))/den
        if k<=0: continue
        x=tuple(c*T[j] if bits[j] else k*pi[j] for j in range(len(pi)))
        if all((k*pi[j]<=c*T[j] if bits[j] else k*pi[j]>=c*T[j]) for j in range(len(pi))):
            answers.add(x)
    ck(len(answers)==1)
    return answers.pop()

def certify(pi,T,c,exhaust=False):
    x,k=project(pi,T,c)
    ck(all(isinstance(z,F) for z in (*pi,*T,c,k,*x)))
    ck(sum(x)==1);ck(1-c<=k<=1)
    ck(all(xj>=c*t for xj,t in zip(x,T)))
    ck(all(xj>=k*p for xj,p in zip(x,pi)))
    ck(all(xj==c*t for xj,p,t in zip(x,pi,T) if not p))
    if exhaust: ck(x==enumerate_active(pi,T,c))
    # All vertices of the feasible polytope. Linear tangent inequality at these
    # vertices proves it everywhere, including ghost target mass.
    for j in range(len(pi)):
        y=[c*t for t in T]; y[j]+=1-c
        tangent=sum(p*(yj-xj)/xj for p,yj,xj in zip(pi,y,x) if p)
        ck(tangent<=0)
    return x

def walsh(v):
    a=list(v);h=1
    while h<len(a):
        for off in range(0,len(a),2*h):
            for j in range(off,off+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a

def direct(v):
    return [sum(f*(-1 if (s&t).bit_count()%2 else 1) for t,f in enumerate(v)) for s in range(len(v))]

def main(pilot):
    start=time.monotonic(); cases=0;tables=0;ghostcases=0
    masks=range(1,16 if not pilot else 5)
    laws=[tuple(F(bool(m&(1<<j)),m.bit_count()) for j in range(4)) for m in masks]
    for pi,T,c in product(laws,laws,(F(1,4),F(1,2),F(3,4))):
        certify(pi,T,c,True);cases+=1
        ghostcases+=int(any(not p and t for p,t in zip(pi,T)))
    for n in range(0,3 if pilot else 4):
        N=1<<n
        for mask in range(1<<N):
            v=[1 if mask&(1<<j) else -1 for j in range(N)]
            a=walsh(v);ck(a==direct(v));p=tuple(F(z*z,N*N) for z in a)
            ck(sum(p)==1)
            inf=sum(p[s]*s.bit_count() for s in range(N))
            physical=sum(F(sum(v[j]!=v[j^(1<<i)] for j in range(N)),N) for i in range(n))
            ck(inf==physical);tables+=1
            tail=1-p[0]
            if not tail: continue
            pi=tuple(z/tail for z in p[1:]); d=len(pi)
            targets=[tuple(F(1,d) for _ in pi)]
            for j in sorted({0,d-1}):targets.append(tuple(F(k==j) for k in range(d)))
            for T in targets:
                x=certify(pi,T,F(1,2));cases+=1
                for alpha in (F(1,4),F(3,4)):
                    M=tuple(alpha*z+(1-alpha)/d for z in pi)
                    for mass in (F(1),F(1,2)):
                        old=(mass*p[0],)+tuple(mass*tail*z for z in M)
                        new=(mass*p[0],)+tuple(mass*tail*z for z in x)
                        ck(old[0]==new[0]);ck(sum(old)==sum(new)==mass)
                        # Exact equality of every ratio in full-CE subtraction
                        # with its conditional KL-difference ratio. No log eval.
                        ck(all(o/q==m/z for o,q,m,z,prob in zip(old[1:],new[1:],M,x,pi) if prob))
    # Actual AND2 Fourier witness and both incompatible policy classes.
    a=direct([1,-1,-1,-1]);ck([F(z*z,16) for z in a]==[F(1,4)]*4)
    pi=(F(1,3),)*3;M=(F(1,4),F(5,8),F(1,8));T=(F(1),F(0),F(0))
    x=certify(pi,T,F(1,2));fixed=(F(1,2),F(5,12),F(1,12))
    flexible_ratio=product_ratio(M,x);fixed_ratio=product_ratio(M,fixed)
    ck(x==(F(1,2),F(1,4),F(1,4)))
    ck(flexible_ratio==F(5,8)<1);ck(fixed_ratio==F(9,8)>1)
    # Boundary sharpness for disjoint true and floor supports.
    ck(project((F(1),F(0)),(F(0),F(1)),F(3,4))[0]==(F(1,4),F(3,4)))
    elapsed=time.monotonic()-start;ck(elapsed<55)
    out={'verdict':'PASS','arithmetic':'integer Walsh and Fraction; exact tangent certificates; integer rational log signs','checks':checks,'projection_cases':cases,'Boolean_tables':tables,'ghost_profile_cases':ghostcases,'runtime_seconds':elapsed,'pilot':pilot,'witness':{'flexible_cost':'(1/4)log2(5/8)<0','fixed_profile_cost':'(1/4)log2(9/8)>0'},'scope':'finite validation of independent analytic reconstruction; no FEI closure or formal certificate','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    f=ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json');f.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))

def product_ratio(a,b):
    q=F(1)
    for x,y in zip(a,b):q*=x/y
    return q

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();main(args.pilot)
