"""B15 current-run checker for the real-restriction softmax/negative-credit decomposition.

This checks a NEW statistic W, not the settled FEI/read-once certificate.
Analytic inequalities are proved in REPORT.md; finite checks here only stress implementation.
"""
from __future__ import annotations
import hashlib, math
import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
 (TOP, BOT),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
 ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
  "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
 ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
 ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

def fwht(a):
    a=np.asarray(a,dtype=np.int64).copy()
    h=1
    while h<a.size:
        b=a.reshape(-1,2*h)
        x=b[:,:h].copy(); y=b[:,h:].copy()
        b[:,:h]=x+y; b[:,h:]=x-y
        a=b.reshape(-1); h*=2
    return a

def h2(q):
    if q<=0.0 or q>=1.0: return 0.0
    return -q*math.log2(q)-(1-q)*math.log2(1-q)

def jfun(q):
    if q<=0.0: return 0.0
    s=math.sqrt(q*(1-q))
    return 1.0-h2(0.5+s)

def psi(q):
    if q<=0.0 or abs(q-0.5)<1e-18: return 0.0
    return 0.5*math.log2(1.0/(2.0*q))

def stats(vals, check_identity=False):
    vals=np.asarray(vals,dtype=np.int64)
    N=vals.size; n=int(round(math.log2(N)))
    coeff=fwht(vals).astype(np.float64)/N
    p=coeff*coeff
    I=J=W=0.0
    max_pair_err=0.0
    for i in range(n):
        bit=1<<i
        low=np.arange(N,dtype=np.int64)
        low=low[(low&bit)==0]
        u=coeff[low]; v=coeff[low|bit]
        a=u*u; b=v*v; m=a+b
        alpha=float(np.sum(b))
        qi=min(alpha,1-alpha)
        Wi=0.0
        for uu,vv,aa,bb,mm in zip(u,v,a,b,m):
            if mm<=0: continue
            q=min(aa,bb)/mm
            Wi += mm*q*psi(q)
            if check_identity:
                def phi(x):
                    return 0.0 if x<=0 else x*math.log2(1.0/x)
                direct=phi(aa)+phi(bb)-0.5*phi((uu+vv)**2)-0.5*phi((uu-vv)**2)
                formula=mm*(h2(q)+jfun(q))
                max_pair_err=max(max_pair_err,abs(direct-formula))
        I+=alpha; J+=qi; W+=Wi
    return I,J,W,max_pair_err

def exhaustive_small():
    out={}
    for n in range(1,5):
        N=1<<n
        best=-1.0; maxerr=0.0
        for mask in range(1<<N):
            vals=np.array([1 if ((mask>>x)&1) else -1 for x in range(N)],dtype=np.int64)
            I,J,W,err=stats(vals,check_identity=True)
            maxerr=max(maxerr,err)
            if J>1e-15: best=max(best,W/J)
        out[n]=(best,maxerr)
    return out

def width2_ratio(m):
    alpha=0.5*(3/4)**(m-1)
    v2=4*(3**(2*m-2))/(16**m)
    u2=(1-2*(3/4)**m)**2
    regular=v2*((4/3)**(m-1)-1)*0.5*math.log2(5)
    mn=min(u2,v2)
    special=0.0 if mn==0 else mn*0.5*math.log2((u2+v2)/(2*mn))
    return (regular+special)/alpha

def reconstruct_numaro():
    base=int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    seen=base; hosts=[]
    for mask in masks:
        assert mask.bit_count()==2 and not(seen&mask)
        seen |= mask
        hosts.append([x for x in range(512) if (mask>>x)&1])
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    table=np.tile(core,(1<<9,1))
    for j,cells in enumerate(hosts):
        active=(np.arange(1<<9)&(1<<j))!=0
        table[np.ix_(active,np.array(cells,dtype=int))]=-1
    table=table.ravel()
    digest=hashlib.sha256(",".join(map(str,table)).encode()).hexdigest()
    assert digest==EXPECTED_SHA and int(table.sum())==0
    return table

def scalar_grid():
    c0=1+3/math.log(2)
    max_violation=-1e100
    max_identity=0.0
    for k in range(1,200000):
        q=0.5*k/200000
        eta=q+(1-q)*math.log2(1/(1-q))
        max_identity=max(max_identity,abs(h2(q)-(2*q*psi(q)+eta)))
        max_violation=max(max_violation,h2(q)+jfun(q)-2*q*psi(q)-c0*q)
    return c0,max_identity,max_violation

if __name__=="__main__":
    c0,identerr,scalarviol=scalar_grid()
    print("c0",repr(c0))
    print("scalar_identity_max_abs_err",identerr)
    print("scalar_bound_max_grid_violation",scalarviol)
    print("small_exhaustive",exhaustive_small())
    vals=[(m,width2_ratio(m)) for m in range(2,13)]
    print("width2_W_over_J",vals)
    print("width2_limit",0.25*math.log2(5))
    table=reconstruct_numaro()
    I,J,W,err=stats(table,check_identity=True)
    print("numaro_hash",EXPECTED_SHA)
    print("numaro_I",I,"J",J,"W",W,"W_over_J",W/J,"pair_identity_err",err)
