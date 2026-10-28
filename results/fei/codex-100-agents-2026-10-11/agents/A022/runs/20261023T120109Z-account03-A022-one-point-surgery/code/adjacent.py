from exact import *
from gu import U
from v import V
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1];count=0
def eq(a,b):
    global count
    count+=1;assert not plus(a,mul(b,-1)),(a,b)
def equal(a,b):
    global count
    count+=1;assert a==b,(a,b)
def tails(p):
    q=list(p)
    for i in range(len(p).bit_length()-1):
        for S in range(len(p)):
            if not S>>i&1:q[S]+=q[S|(1<<i)]
    return q
start=time.monotonic();cases=0
for v,w,i in ((0,1,0),(1,3,1)):
    b=tuple(g(x&7)*g(x>>3) for x in range(64));eps=b[v]*b[w];delta=Q(1,64)
    for am in (1,3,5,7):
        for cm in (1,6,10,14):
            a=tuple(1 if am>>z&1 else -1 for z in range(4));c=tuple(1 if cm>>z&1 else -1 for z in range(4))
            ac=[Q(x,4) for x in fwht(a)];cc=[Q(x,4) for x in fwht(c)]
            f=tuple(b[x]*(a[z] if x==v else c[z] if x==w else 1) for z in range(4) for x in range(64))
            P=spectrum(f);pi=tails(P);pa=tails([x*x for x in ac]);pc=tails([x*x for x in cc]);cross=tails([x*y for x,y in zip(ac,cc)])
            for T in range(1,4):
                for S in range(64):
                    equal(P[S+64*T],delta**2*(ac[T]+eps*(-1 if S>>i&1 else 1)*cc[T])**2)
                    expected=delta**2*2**(6-S.bit_count())*(pa[T]+pc[T]-(2*eps*cross[T] if S>>i&1 else 0))
                    equal(pi[S+64*T],expected)
            actual=plus(*(mul(lg(q/p),p) for Prow,Qrow in ((P[64:],pi[64:]),) for p,q in zip(Prow,Qrow) if p))
            h=tuple(a[z] if y==0 else eps*c[z] for z in range(4) for y in (0,1));ph=spectrum(h);pih=tails(ph)
            jy=mul(lg(pih[1]/ph[1]),ph[1]) if ph[1] else {}
            va=1-Q(sum(a),4)**2;vc=1-Q(sum(c),4)**2
            rhs=plus(const(delta*Q(5,2)*(va+vc)),mul(plus(V(h),mul(jy,-1)),2*delta))
            eq(actual,rhs)
            dy=plus(V(h),mul(plus(V(a),V(c)),-Q(1,2)))
            eq(actual,plus(const(delta*Q(5,2)*(va+vc)),mul(plus(V(a),V(c),mul(dy,2),mul(jy,-2)),delta)))
            cases+=1;assert time.monotonic()-start<60
out={'status':'PASS','cases':cases,'assertions':count,'elapsed_seconds':time.monotonic()-start,'scope':'exact adjacent signed spectra/upward tails/shared-mux identity; GU payment remains OPEN','peak_memory':'unmeasured'}
(ROOT/'out/adjacent.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
