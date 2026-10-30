import gu
from exact import *
from functools import lru_cache
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parents[1]; tests=0
@lru_cache(None)
def V(a):return plus(gu.U(a),mul(phi(Q(sum(a),len(a))**2),-1))
def GV(a,coords):return plus(*(plus(V(a),mul(plus(*(V(tuple(restrict(a,i,b))) for b in (0,1))),-Q(1,2))) for i in coords))
def eq(a,b):
    global tests
    tests+=1;assert not plus(a,mul(b,-1)),(a,b)
def ge(a):
    global tests
    tests+=1;assert bounds(a)[0]>=0,a
def run(t,v,a):
    k=3*t;delta=Q(1,8**t);seed=[]
    for x in range(2**k):
        b=1
        for j in range(t):b*=g(x>>(3*j)&7)
        seed.append(b)
    f=tuple(seed[x]*(a[z] if x==v else 1) for z in range(len(a)) for x in range(2**k))
    p=spectrum(f);m=len(a).bit_length()-1;tail=p[:]
    for i in range(k+m):
        for S in range(len(p)):
            if not S>>i&1:tail[S]+=tail[S|(1<<i)]
    # Direct extraction of nonempty DATA / empty CONTROL rows.
    remainder=plus(*(mul(lg(tail[S]/p[S]),p[S]) for S in range(1,2**k) if p[S]),const(delta*k*(1-Q(sum(a),len(a))**2)/2))
    eq(V(f),plus(mul(V(a),delta),remainder));ge(remainder)
    Id=sum(inf(f,i) for i in range(k));gd=GV(f,range(k));gc=GV(f,range(k,k+m));ga=GV(a,range(m))
    ge(plus(const(Q(243*t,2)),mul(gd,-1)))
    ge(plus(mul(ga,delta),const(Q(21,2)),mul(gc,-1)))
    ge(plus(mul(ga,delta),const(256*Id),mul(plus(gd,gc),-1)))
    ge(plus(mul(V(a),delta),const(24*Id),mul(V(f),-1)))
    # The sufficient universal H endpoint is checked on actual spectra too.
    ge(plus(const(2*(Id+delta*sum(inf(a,i) for i in range(m)))),mul(V(f),2),mul(entropy(p),-1)))
def main():
    mode=sys.argv[1];start=time.monotonic();cases=[(2,v,tuple(1 if mask>>z&1 else -1 for z in range(4))) for v in (0,1,7,63) for mask in range(16)]
    if mode=='pilot':cases=[cases[i] for i in (0,5,29,63)]
    elif mode=='targeted':cases=[(3,v,tuple(-1 if (z==0 if kind==0 else z&1) else 1 for z in range(8))) for v in (0,511) for kind in (0,1)]
    else:assert mode=='main'
    for c in cases:
        run(*c);assert time.monotonic()-start<{'pilot':60,'main':240,'targeted':180}[mode]
    out={'status':'PASS','cases':len(cases),'assertions':tests,'elapsed_seconds':time.monotonic()-start,'target':'actual GV(F)-delta GV(a)-256 Idata and both V endpoints','peak_memory':'unmeasured','review':'author exact check'}
    (ROOT/'out'/f'v_{mode}.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
