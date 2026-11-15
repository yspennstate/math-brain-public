"""Independent exact audit of T067-UNIFORM-LOCAL-001 v1.

Builds D(l) G(l,r) directly from the proof's closed forms, with w=l^2 and
K0=k*w. It imports no solver code or certificate data.
"""

import ctypes
import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

OUT = Path(__file__).with_name("checks")
OUT.mkdir(exist_ok=True)


class MemoryStatus(ctypes.Structure):
    _fields_ = [("dwLength",ctypes.c_ulong),("dwMemoryLoad",ctypes.c_ulong),
                ("ullTotalPhys",ctypes.c_ulonglong),("ullAvailPhys",ctypes.c_ulonglong),
                ("ullTotalPageFile",ctypes.c_ulonglong),("ullAvailPageFile",ctypes.c_ulonglong),
                ("ullTotalVirtual",ctypes.c_ulonglong),("ullAvailVirtual",ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual",ctypes.c_ulonglong)]


def memcheck():
    s=MemoryStatus(); s.dwLength=ctypes.sizeof(s)
    assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(s))
    print("available physical GiB",round(s.ullAvailPhys/2**30,2),flush=True)
    if s.ullAvailPhys<2*2**30:
        raise SystemExit("postpone: below 2 GiB")


def C(x):
    x=F(x)
    return {(0,0):x} if x else {}


def V(axis):
    return {(1,0):F(1)} if axis==0 else {(0,1):F(1)}


def add(*parts):
    o=defaultdict(F)
    for p in parts:
        for e,c in p.items():o[e]+=c
    return {e:c for e,c in o.items() if c}


def neg(p):
    return {e:-c for e,c in p.items()}


def sub(p,q):
    return add(p,neg(q))


def mul(*parts):
    o=C(1)
    for p in parts:
        n=defaultdict(F)
        for (a,b),c in o.items():
            for (i,j),d in p.items():n[(a+i,b+j)]+=c*d
        o={e:c for e,c in n.items() if c}
    return o


def sc(p,c):
    c=F(c)
    return {e:c*v for e,v in p.items() if c*v}


def pw(p,n):
    return mul(*([p]*n)) if n else C(1)


def ev(p,l,r):
    return sum((c*l**i*r**j for (i,j),c in p.items()),F(0))


def deg(p):
    return max(i for i,j in p),max(j for i,j in p)


def polynomial(M,delta,scale):
    l,r=V(0),V(1)
    w=pw(l,2)
    D0=sub(C(1),w)
    K0=add(r,sc(w,2),sc(mul(r,w),-2))
    Kminus=sub(K0,w)
    H1=sub(mul(K0,Kminus),sc(pw(w,2),2))
    H2=mul(K0,Kminus,sub(K0,sc(w,2)))
    N=sc(add(mul(K0,Kminus),sc(sub(C(1),K0),2)),F(5,2))
    J=sc(mul(add(C(1),l),N),F(1,3))
    g=sc(mul(K0,Kminus),F(1,12))
    # A3=D0^3*A_k, from proof (10) after all inverse w powers cancel.
    A3=add(sc(mul(N,pw(w,3),D0),F(1,9)),
           sc(mul(H2,pw(D0,3)),F(1,216)),
           mul(add(C(1),l),
               add(sc(mul(N,H1,w,D0),F(1,18)),
                   sc(mul(H2,pw(D0,2)),F(5,108)))))
    # B3=D0^3*B_k; each bracket is polynomial after cancellation.
    Bfirst=sc(add(sc(mul(pw(J,2),pw(w,3)),3),
                  mul(l,N,J,pw(w,3)),
                  sc(mul(pw(N,2),pw(w,4)),F(1,12))),F(1,9))
    Bleft=mul(add(sc(mul(l,J),3),sc(mul(N,w),F(1,2))),
              add(sc(mul(l,J,H1),F(1,2)),sc(mul(H2,D0),F(5,18))))
    Bright=mul(add(sc(mul(l,J),F(1,2)),sc(mul(N,w),F(1,12))),
               add(sc(mul(N,H1,w),F(1,2)),sc(mul(H2,D0),F(5,6))))
    B3=add(Bfirst,sc(mul(add(C(1),l),add(Bleft,Bright)),F(1,9)))
    G3=add(sc(mul(g,pw(D0,3)),1-delta),sc(A3,-M),sc(B3,-M*M))
    P=sc(G3,scale)
    print("polynomial in l,r",deg(P),"terms",len(P),flush=True)
    assert deg(P)[0]<=17 and deg(P)[1]<=6
    return P


def direct_G(d,k,M,delta):
    d,k=F(d),F(k)
    l=F(1)/int(math.isqrt(int(d)))
    assert l*l*d==1
    Z=k*(k-1)/2+d*(d-k)
    Cu=5*Z/(d*(d-1));Ct=Cu*(1+l)/3
    Kpre=d/(9*(d-1));K=1/(9*(1-l))
    ve=Cu/d**2;te=l*Ct/d
    g=k*(k-1)/(12*d**2)
    A2=Kpre*Cu/d**3
    B2=Kpre*(3*Ct**2/d**3+l*Cu*Ct/d**3+Cu**2/(12*d**4))
    A,B=A2,B2
    for j in range(2,int(k)):
        j=F(j)
        uj=(j*Cu+F(5,2)*j*(j-1))/d**2
        tj=j*l*Ct/d+F(5,6)*j*(j-1)/d**2
        gj=j*(j-1)/(12*d**2)
        A+=gj/(6*d)+K*(uj/(2*d)+j*Cu/(2*d**3))
        B+=K*(3*tj*te+(uj*te+tj*ve)/2+uj*ve/12)
    S1=k*(k-1)/2-1;S2=k*(k-1)*(k-2)/3
    su=(Cu*S1+F(5,2)*S2)/d**2
    st=l*Ct*S1/d+F(5,6)*S2/d**2
    Aclosed=A2+S2/(72*d**3)+K*(Cu*S1+F(5,4)*S2)/d**3
    Bclosed=B2+K*((3*te+ve/2)*st+(te/2+ve/12)*su)
    assert A==Aclosed and B==Bclosed,"recurrence versus closed form"
    return (1-delta)*g-M*Aclosed-M*M*Bclosed


def bern_axis(p,axis,n):
    out=defaultdict(F)
    for e,c in p.items():
        i=e[axis]
        for k in range(i,n+1):
            new=(k,e[1]) if axis==0 else (e[0],k)
            out[new]+=c*F(math.comb(k,i),math.comb(n,i))
    return {e:c for e,c in out.items() if c}


def run(name,M,L,delta,scale):
    P=polynomial(M,delta,scale)
    matches=0
    for d in (4,9,16,25,49,100):
        for k in sorted({2,3,min(d,7),d//2,d}):
            if not 2<=k<=d:continue
            l=F(1,math.isqrt(d));r=F(k-2,d-2)
            expected=scale*(1-l*l)**3*direct_G(d,k,M,delta)
            assert ev(P,l,r)==expected,(name,d,k)
            matches+=1
    print(name,"recurrence/polynomial matches",matches,flush=True)
    Q={(i,j):c*L**i for (i,j),c in P.items()}
    Q=bern_axis(Q,0,17)
    Q=bern_axis(Q,1,6)
    signs={"negative":0,"zero":0,"positive":0}
    positive=[]
    zeros=[]
    for e in itertools.product(range(18),range(7)):
        c=Q.get(e,F(0))
        if c<0:signs["negative"]+=1
        elif c>0:signs["positive"]+=1;positive.append(c)
        else:signs["zero"]+=1;zeros.append(e)
    print(name,"Bernstein",signs,"zero indices",zeros,flush=True)
    assert signs=={"negative":0,"zero":6,"positive":120}
    return {"name":name,"parameters":{"M":str(M),"L":str(L),"delta":str(delta),"D_scale":scale},
            "degrees":deg(P),"raw_terms":len(P),"recurrence_matches":matches,
            "bernstein_signs":signs,"zero_indices":zeros,
            "smallest_positive":str(min(positive))}


if __name__=="__main__":
    memcheck()
    assert 3*2887**2>5000**2
    reports=[run("all_d3",F(27,100),F(2887,5000),F(1,100),12800),
             run("large_d100",F(9,10),F(1,10),F(1,20),1920)]
    path=OUT/"t067_uniform_own_report.json"
    path.write_text(json.dumps(reports,indent=2),encoding="utf-8")
    print("saved",path.name,flush=True)
