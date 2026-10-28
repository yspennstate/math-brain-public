from exact import *
from functools import lru_cache
from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parents[1]; checks=0
@lru_cache(None)
def U(a):
    p=spectrum(a); pi=p[:]; n=len(a).bit_length()-1
    for i in range(n):
        for s in range(len(a)):
            if not s>>i&1:pi[s]+=pi[s|(1<<i)]
    return plus(*(mul(lg(q/r),r) for r,q in zip(p,pi) if r))
def G(a,coords=None):
    if coords is None:coords=range(len(a).bit_length()-1)
    return plus(*(plus(U(a),mul(plus(*(U(tuple(restrict(a,i,b))) for b in (0,1))),-Q(1,2))) for i in coords))
def eq(a,b):
    global checks
    checks+=1;assert not plus(a,mul(b,-1)),(a,b)
def ge(a):
    global checks
    checks+=1;assert bounds(a)[0]>=0,a
def run(t,v,a):
    k=3*t;delta=Q(1,8**t);n=2**k;seed=[]
    for x in range(n):
        b=1
        for i in range(t):b*=g(x>>(3*i)&7)
        seed.append(b)
    f=tuple(seed[x]*(a[z] if x==v else 1) for z in range(len(a)) for x in range(n))
    s=Q(sum(a),len(a)); cs=[Q(x,n) for x in fwht(seed)]
    amps=[h+delta*seed[v]*(-1 if (S&v).bit_count()%2 else 1)*(s-1) for S,h in enumerate(cs)]
    p=[x*x for x in amps];tails=[x+delta*delta*(1-s*s) for x in p]
    for i in range(k):
        for S in range(n):
            if not S>>i&1:tails[S]+=tails[S|(1<<i)]
    E=plus(*(mul(lg(z/x),x) for x,z in zip(p,tails) if x))
    qb=plus(E,mul(phi(s*s),-delta),const(delta*k*(1-s*s)/2))
    eq(U(f),plus(mul(U(a),delta),qb));ge(plus(qb,const(delta)))
    error=plus(qb,mul(U(tuple(seed)),-1))
    ge(plus(const(20),error));ge(plus(const(20),mul(error,-1)))
    for i in range(k):
        child=tuple(restrict(f,i,v>>i&1)); seedchild=tuple(restrict(seed,i,v>>i&1))
        err=plus(U(child),mul(U(a),-2*delta),mul(U(seedchild),-1))
        ge(plus(const(20),err));ge(plus(const(20),mul(err,-1)))
    idata=sum(inf(f,i) for i in range(k));ia=sum(inf(a,i) for i in range(len(a).bit_length()-1))
    gd=G(f,range(k));gc=G(f,range(k,k+len(a).bit_length()-1));ga=G(a)
    eq(G(f),plus(gd,gc));ge(plus(const(99*t),mul(gd,-1)))
    ge(plus(mul(ga,delta),const(6*delta*ia+Q(21,2)),mul(gc,-1)))
    ge(plus(mul(ga,delta),const(6*delta*ia+256*idata),mul(G(f),-1)))
    eq(const(idata+delta*ia),const(sum(inf(f,i) for i in range(k+len(a).bit_length()-1))))
    assert idata>=Q(21*t,32)
def main():
    mode=sys.argv[1];start=time.monotonic();cases=[(2,v,tuple(1 if mask>>z&1 else -1 for z in range(4))) for v in (0,1,7,63) for mask in range(16)]
    if mode=='pilot':cases=[cases[i] for i in (0,5,29,63)]
    elif mode=='targeted':cases=[(3,v,tuple(-1 if (z==0 if kind==0 else z&1) else 1 for z in range(8))) for v in (0,511) for kind in (0,1)]
    else:assert mode=='main'
    for c in cases:
        run(*c);assert time.monotonic()-start<({'pilot':60,'main':240,'targeted':180}[mode])
    out={'status':'PASS','cases':len(cases),'assertions':checks,'elapsed_seconds':time.monotonic()-start,'target':'actual signed GU remainder G(F)-delta G(a)-6delta I(a)-256 Idata<=0','peak_memory':'unmeasured','review':'author exact check; infinite passage in GU_PROOF'}
    (ROOT/'out'/f'gu_{mode}.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
