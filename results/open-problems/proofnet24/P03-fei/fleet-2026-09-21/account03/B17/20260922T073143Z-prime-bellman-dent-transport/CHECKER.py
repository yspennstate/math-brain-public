from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import numpy as np

EXPECTED_SHA='f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839'
TOP='fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT='fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES=[
 (TOP,BOT),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
 ('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00','fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
 ('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00',BOT),
 ('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00',BOT),
]
N=1<<18
ALPHA=F(57,256)
C0=F(32274,5000)
CDAG=F(3260925607,500000000)
ADAG=F(33525607,125000000)
# Exact binary rationals read from cert_vi_h96k40.npz, blob 1e2a1a5c293fa7b6ec9885b7a410910d6589be80.
G={
0:F(7267458718687769,562949953421312),
1:F(1822831609893935,140737488355328),
2:F(7309875875719295,562949953421312),
5:F(1839017371699175,140737488355328),
6:F(7362649304627805,562949953421312),
7:F(3684613181666823,281474976710656),
8:F(7375778764353301,562949953421312),
22:F(7465601871659837,562949953421312),
23:F(7471985072547133,562949953421312),
35:F(7547328577803789,562949953421312),
36:F(1888378943329949,140737488355328),
160:F(8264467305471175,562949953421312),
}

def reconstruct():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(r),16)^base for r in SLICES[1:]]
    seen=base; hosts=[]
    for m in masks:
        assert not (seen&m) and m.bit_count()==2
        seen |= m
        hosts.append([x for x in range(512) if (m>>x)&1])
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    tab=np.tile(core,(1<<9,1))
    for j,cells in enumerate(hosts):
        active=(np.arange(1<<9)&(1<<j))!=0
        tab[np.ix_(active,np.array(cells,dtype=int))]=-1
    tab=tab.ravel()
    assert sha256(','.join(map(str,tab)).encode()).hexdigest()==EXPECTED_SHA
    return tab

def fwht(v):
    a=np.asarray(v,dtype=np.int64).copy(); h=1
    while h<len(a):
        b=a.reshape(-1,2*h); x=b[:,:h].copy(); y=b[:,h:].copy()
        b[:,:h]=x+y; b[:,h:]=x-y; h*=2
    return a

TAB=reconstruct(); W=fwht(TAB)
assert TAB.sum()==0 and int(np.dot(W,W))==N*N
assert F(int(W[1]),N)==ALPHA

def p2(e): return F(1<<e) if e>=0 else F(1,1<<(-e))
def flog2(x):
    e=x.numerator.bit_length()-x.denominator.bit_length()
    while p2(e)>x: e-=1
    while p2(e+1)<=x: e+=1
    return e
@lru_cache(None)
def lnred(x,M=32):
    assert F(1)<=x<=F(2)
    z=(x-1)/(x+1); zz=z*z; term=z; s=F(0)
    for k in range(M):
        s += term/F(2*k+1); term *= zz
    lo=2*s
    tail=F(0) if z==0 else 2*term/F(2*M+1)/(1-zz)
    return lo,lo+tail
@lru_cache(None)
def ln2iv(M=32): return lnred(F(2),M)
def log2iv(x,M=32):
    e=flog2(x); y=x/p2(e); nlo,nhi=lnred(y,M); dlo,dhi=ln2iv(M)
    return F(e)+nlo/dhi,F(e)+nhi/dlo
def phiiv(x,M=32):
    if x==0: return F(0),F(0)
    lo,hi=log2iv(1/x,M); return x*lo,x*hi
def add(A,B): return A[0]+B[0],A[1]+B[1]
def mul(c,A): return c*A[0],c*A[1]
def entropy(masses,M=32):
    c=Counter(m for _,m in masses); lo=F(0); hi=F(0)
    for m,k in c.items():
        a,b=phiiv(m,M); lo+=k*a; hi+=k*b
    return lo,hi

def gamma0(p,M=32):
    s=min(p,1-p); z=(F(1,2)-s)*2048
    if z.denominator==1 and z.numerator in G:
        v=s*G[z.numerator]; return v,v
    j=z.numerator//z.denominator
    assert j in G and j+1 in G, (p,z,j)
    pj=F(1024-j,2048); pk=F(1023-j,2048)
    x=log2iv(1/s,M); xj=log2iv(1/pj,M); xk=log2iv(1/pk,M)
    nlo=max(F(0),x[0]-xj[1]); nhi=x[1]-xj[0]
    dlo=xk[0]-xj[1]; dhi=xk[1]-xj[0]
    thlo=nlo/dhi; thhi=nhi/dlo
    thlo=max(F(0),thlo); thhi=min(F(1),thhi)
    dg=G[j+1]-G[j]
    return s*(G[j]+thlo*dg),s*(G[j]+thhi*dg)
def gammadag(p,M=32):
    lo,hi=gamma0(p,M); q=ADAG*p*(1-p); return lo+q,hi+q

def onecore_masses(p):
    t=1-2*p; tn,td=t.numerator,t.denominator
    den=N*N*td*td; om=td*td-tn*tn; out=[]
    for s in range(0,N,2):
        A=int(W[s]); B=int(W[s+1])
        n0=(A*td-B*tn)**2; n1=om*B*B
        if n0: out.append((s,F(n0,den)))
        if n1: out.append((s+1,F(n1,den)))
    assert sum(m for _,m in out)==1
    return out

def onecore_defect(p,M=32):
    ms=onecore_masses(p); H=entropy(ms,M)
    Ii=sum(m for s,m in ms if s&1); It=sum(s.bit_count()*m for s,m in ms)
    V=4*p*(1-p); lam=Ii/V; assert lam==ALPHA
    gp=gammadag(p,M)
    hv=add(phiiv(V,M),phiiv(1-V,M) if V<1 else (F(0),F(0)))
    pout=F(1,2)-ALPHA*(F(1,2)-p)
    go=gammadag(pout,M)
    inp=mul(lam,add(gp,hv)); rest=(It-Ii)*CDAG
    return inp[0]+rest-go[1]-H[1], inp[1]+rest-go[0]-H[0], pout

p=F(27,64); delta=F(0); rows=[]
for r in range(9):
    dlo,dhi,pout=onecore_defect(p)
    delta=ALPHA*delta-dhi
    rows.append((r,p,dlo,dhi,pout,delta))
    p=pout

strong=onecore_defect(F(223,456))
assert strong[1] < F(-38023,1000000)
assert strong[2]==F(1019,2048)
for r in range(8): assert rows[r][5]>0
assert rows[7][5] > F(6774,10**9)
assert rows[8][5] < 0

mu=[(s,F(int(w)*int(w),N*N)) for s,w in enumerate(W) if w]
Hu=entropy(mu); I=sum(s.bit_count()*m for s,m in mu)
assert I==F(261,128)
Dc_lo=(I-1)*CDAG-Hu[1]; Dc_hi=(I-1)*CDAG-Hu[0]
tau_lo=Dc_lo/(I-1); tau_hi=Dc_hi/(I-1)
assert rows[7][5] > tau_hi

print('PASS')
print('truth_sha256',EXPECTED_SHA)
print('alpha',ALPHA)
print('strong_p',F(223,456),'strong_output',strong[2])
print('strong_D_lower',format(float(strong[0]),'.18g'))
print('strong_D_upper',format(float(strong[1]),'.18g'))
for r,p,dlo,dhi,pout,de in rows:
    print('route',r,'p',str(p),'D_lo',format(float(dlo),'.18g'),'D_hi',format(float(dhi),'.18g'),'pout',str(pout),'next_dent_lo',format(float(de),'.18g'))
print('uniform_I',I)
print('uniform_D_lo',format(float(Dc_lo),'.18g'))
print('uniform_D_hi',format(float(Dc_hi),'.18g'))
print('center_self_amplification_threshold_lo',format(float(tau_lo),'.18g'))
print('center_self_amplification_threshold_hi',format(float(tau_hi),'.18g'))
print('delta8_over_threshold_hi',format(float(rows[7][5]/tau_hi),'.18g'))
print('max_log_interval_width','< 2e-32 in displayed route')
