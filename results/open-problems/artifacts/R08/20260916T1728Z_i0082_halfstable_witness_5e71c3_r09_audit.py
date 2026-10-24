#!/usr/bin/env python3
# Independent R08 exact audit of R09-C180 finite core.
from fractions import Fraction
from math import comb

def sphere(r):
    out=[]
    for x in range(-r,r+1):
      for y in range(-r,r+1):
        zabs=r-abs(x)-abs(y)
        if zabs<0: continue
        if zabs==0:
            out.append((x,y,0))
        else:
            out.append((x,y,zabs)); out.append((x,y,-zabs))
    return sorted(set(out))

def adj(a,b):
    return sum(abs(a[i]-b[i]) for i in range(3))==1

S1=sphere(1); S2=sphere(2)
assert len(S1)==6 and len(S2)==18
active=[]
for mask in range(1<<6):
    bm=0
    for j,y in enumerate(S2):
        if any(((mask>>i)&1) and adj(S1[i],y) for i in range(6)):
            bm |= 1<<j
    active.append(bm)

DEN_K=1<<18
best=[None]*19
for Y in range(1,1<<18):
    m=Y.bit_count()
    num=0
    for A in active:
        k=(Y&A).bit_count()
        if k:
            num += DEN_K - (1<<(18-k))
    fr=Fraction(num,128*DEN_K)
    if best[m] is None or fr<best[m]:
        best[m]=fr

reported=[None,Fraction(1,8),Fraction(7,32),Fraction(37,128),Fraction(175,512),Fraction(781,2048),Fraction(417,1024),Fraction(1763,4096),Fraction(3647,8192),Fraction(7435,16384),Fraction(30497,65536),Fraction(61869,131072),Fraction(124849,262144),Fraction(251117,524288),Fraction(1015495,2097152),Fraction(2043531,4194304),Fraction(4100927,8388608),Fraction(8218347,16777216),Fraction(16457991,33554432)]
for m in range(1,19):
    assert best[m]==reported[m], (m,best[m],reported[m])
    print("rho",m,best[m])

def C(n,k):
    if k<0 or k>n: return 0
    return comb(n,k)
def qratio(nminus,n,k):
    den=C(n,k)
    return Fraction(C(nminus,k),den) if den else Fraction(0,1)
def cap(m): return 5*min(m,6)+4*max(m-6,0)
def minm(E):
    for m in range(1,19):
        if cap(m)>=E: return m
    raise ValueError(E)
def chord(mu):
    n=mu.numerator//mu.denominator
    lam=mu-Fraction(n,1)
    return Fraction(1,2**n)*(1-lam/2)

tail=Fraction(0,1); byk={}
for a in range(7):
  for b in range(25):
    for c in range(9):
      k=a+b+c
      if not (13<=k<=38): continue
      cnt=C(6,a)*C(24,b)*C(8,c)
      if cnt==0: continue
      Ein=a+2*b+3*c
      m=minm(Ein)
      qA=qratio(5,6,a); qB1=qratio(23,24,b); qB2=qratio(22,24,b); qC=qratio(7,8,c)
      muZ=6*(1-qA)+24*(1-qA*qB1)+12*(1-qB2)+24*(1-qB2*qC)
      term=Fraction(cnt,1<<38)*best[m]*chord(muZ)
      tail += term
      byk[k]=byk.get(k,Fraction(0,1))+term

TARGET=Fraction(22279745927407414101879263,1<<129)
assert tail==TARGET, (tail,TARGET)
print("TAIL_LOWER",tail)
for k in range(13,39): print("tail_lb_k",k,byk.get(k,Fraction(0,1)))
B12=Fraction(635787895558830340599512346683097,1298074214633706907132624082305024)
BNEW=B12-tail
EXPECTED=Fraction(333335964186725761866309721803685680673,1<<129)
assert BNEW==EXPECTED
print("BNEW",BNEW)
print("IMPROVEMENT",tail)
print("R08_AUDIT_R09_C180_FINITE_CORE_PASS")
