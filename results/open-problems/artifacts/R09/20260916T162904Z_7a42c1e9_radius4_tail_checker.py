from fractions import Fraction
from math import comb

def shell(r):
    out=[]
    for x in range(-r,r+1):
      for y in range(-r,r+1):
       for z in range(-r,r+1):
        if abs(x)+abs(y)+abs(z)==r: out.append((x,y,z))
    return sorted(out)
def adj(a,b): return sum(abs(a[i]-b[i]) for i in range(3))==1
S1,S2,S3,S4=map(shell,[1,2,3,4])
assert list(map(len,[S1,S2,S3,S4]))==[6,18,38,66]
counts=[sum(1 for x in S3 if sum(v!=0 for v in x)==m) for m in [1,2,3]]
assert counts==[6,24,8]
def abs_sorted(x): return tuple(sorted((abs(v) for v in x),reverse=True))
from collections import Counter
c4=Counter(abs_sorted(x) for x in S4)
assert c4==Counter({(3,1,0):24,(2,1,1):24,(2,2,0):12,(4,0,0):6})
inmask=[]
for y in S2:
    m=0
    for i,u in enumerate(S1):
        if adj(y,u): m|=1<<i
    inmask.append(m)
R=[]
for sig in range(64):
    r=0
    for j,m in enumerate(inmask):
        if sig&m: r|=1<<j
    R.append(r)
minnum=[None]*19
arg=[None]*19
for Y in range(1,1<<18):
    m=Y.bit_count()
    num=0
    two=1<<m
    for rmask in R:
        rr=(Y&rmask).bit_count()
        num += two-(1<<(m-rr))
    if minnum[m] is None or num<minnum[m]:
        minnum[m]=num; arg[m]=Y
rho=[None]*19
for m in range(1,19):
    rho[m]=Fraction(minnum[m],1<<(m+7))
expected={
1:Fraction(1,8),2:Fraction(7,32),3:Fraction(37,128),4:Fraction(175,512),
5:Fraction(781,2048),6:Fraction(417,1024),7:Fraction(1763,4096),8:Fraction(3647,8192),
9:Fraction(7435,16384),10:Fraction(30497,65536),11:Fraction(61869,131072),12:Fraction(124849,262144),
13:Fraction(251117,524288),14:Fraction(1015495,2097152),15:Fraction(2043531,4194304),
16:Fraction(4100927,8388608),17:Fraction(8218347,16777216),18:Fraction(16457991,33554432)}
assert all(rho[m]==expected[m] for m in expected)

def nohit(total,chosen,k):
    if chosen>total-k: return Fraction(0)
    return Fraction(comb(total-k,chosen),comb(total,chosen))

def muZ(a,b,c):
    qA=nohit(6,a,1)
    qB1=nohit(24,b,1)
    qB2=nohit(24,b,2)
    qC=nohit(8,c,1)
    return 6*(1-qA)+24*(1-qA*qB1)+12*(1-qB2)+24*(1-qB2*qC)

def m_from_E(E):
    for m in range(1,19):
        cap=5*min(m,6)+4*max(m-6,0)
        if cap>=E: return m
    raise AssertionError

def chord_lb(mu):
    n=mu.numerator//mu.denominator
    lam=mu-n
    return Fraction(1,1<<n)*(1-lam/2)

tail=Fraction(0)
byk={}
compositions=0
for a in range(7):
  for b in range(25):
    for c in range(9):
      k=a+b+c
      if not 13<=k<=38: continue
      cnt=comb(6,a)*comb(24,b)*comb(8,c)
      if not cnt: continue
      compositions+=1
      Ein=a+2*b+3*c
      m=m_from_E(Ein)
      term=Fraction(cnt,1<<38)*rho[m]*chord_lb(muZ(a,b,c))
      tail += term
      byk[k]=byk.get(k,Fraction(0))+term
TARGET=Fraction(22279745927407414101879263,1<<129)
assert tail==TARGET
B12=Fraction(635787895558830340599512346683097,1298074214633706907132624082305024)
BNEW=B12-tail
EXPECTED_B=Fraction(333335964186725761866309721803685680673,1<<129)
assert BNEW==EXPECTED_B and BNEW<B12
print('R09 tail checker')
print('shells',len(S1),len(S2),len(S3),len(S4),'S3 types',counts,'compositions',compositions)
for m in range(1,19): print('rho_min',m,rho[m])
for k in range(13,39): print('tail_lb_k',k,byk[k])
print('TAIL_LOWER',tail)
print('B12',B12)
print('BNEW',BNEW)
print('IMPROVEMENT',B12-BNEW)
print('PASS')
