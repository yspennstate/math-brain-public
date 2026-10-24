from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import numpy as np

# Exact Numaro source used by the current strong-prime witness.
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

def reconstruct():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(r),16)^base for r in SLICES[1:]]
    seen=base; hosts=[]
    for m in masks:
        assert not(seen&m) and m.bit_count()==2
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
assert TAB.sum()==0
P=F(223,456)
t=1-2*P
assert t==F(5,228)
assert F(int(W[1]),N)==F(57,256)

# Current shaped candidate parameters.  Only derivatives are needed below.
ADAG=F(33525607,125000000)
EPS=F(56721646463783,2500000000000000)
LAM=F(18721807228217,500000000000000)
# Exact binary rationals from the committed read-once potential around the two
# cells touched by the center and strong-output knot.
G={
 0:F(7267458718687769,562949953421312),
 1:F(1822831609893935,140737488355328),
 4:F(1835444679309597,140737488355328),
 5:F(1839017371699175,140737488355328),
 6:F(7362649304627805,562949953421312),
}

# Exact packet decomposition for tail bit 9 (input 10 in one-based notation),
# after biasing core bit 0 at P.  At tail mean u=0, each packet has an absent
# coefficient a and a tail-present coefficient b.  Under tail mean u these
# become a+u b and sqrt(1-u^2)b.
def packet_data(j=9):
    n,d=t.numerator,t.denominator
    vnum=d*d-n*n
    bit=1<<j
    den=N*N*d*d
    bright=dark=beta=0
    sumab=0
    Icore_prime=Itot_prime=0
    terms=[]
    for r in range(N):
        if r&1 or r&bit: continue
        A=int(W[r]); B=int(W[r|1]); C=int(W[r|bit]); D=int(W[r|bit|1])
        if not(A or B or C or D): continue
        # core-absent packet
        anum=A*d+B*n; bnum=C*d+D*n
        b2=bnum*bnum; beta += b2
        if b2:
            if anum==0: dark += b2
            else: bright += b2
        ab=anum*bnum; sumab += ab
        if ab:
            Itot_prime += 2*r.bit_count()*ab
            terms.append((F(ab,den),F(anum*anum,den)))
        # core-present packet; the common sqrt(V_core) cancels after squaring.
        b2p=vnum*D*D; beta += b2p
        if b2p:
            if B==0: dark += b2p
            else: bright += b2p
        abp=vnum*B*D; sumab += abp
        if abp:
            Icore_prime += 2*abp
            Itot_prime += 2*(r|1).bit_count()*abp
            terms.append((F(abp,den),F(vnum*B*B,den)))
    assert sumab==0
    return F(bright,den),F(dark,den),F(beta,den),F(Icore_prime,den),F(Itot_prime,den),terms

BRIGHT,DARK,BETA,ICOREP,ITOTP,TERMS=packet_data()
assert BRIGHT==F(1,256)
assert DARK==0
assert BETA==F(1,256)
assert ICOREP==0 and ITOTP==0

# The output mean is affine in tail mean u.  q(0)=1019/2048 and q'(0)=-1/512.
BIT=1<<9
coef_u=F(int(W[BIT]),N)+t*F(int(W[BIT|1]),N)
q0=(1-t*F(int(W[1]),N))/2
qprime=-coef_u/2
assert q0==F(1019,2048)
assert coef_u==F(1,256)
assert qprime==F(-1,512)

# Rigorous rational logarithm intervals, copied in form from the existing exact
# strong-prime checker.  All entropy is in bits.
def p2(e): return F(1<<e) if e>=0 else F(1,1<<(-e))
def flog2(x):
    e=x.numerator.bit_length()-x.denominator.bit_length()
    while p2(e)>x: e-=1
    while p2(e+1)<=x: e+=1
    return e
@lru_cache(None)
def lnred(x,M=44):
    assert F(1)<=x<=F(2)
    z=(x-1)/(x+1); zz=z*z; term=z; s=F(0)
    for k in range(M):
        s += term/F(2*k+1); term *= zz
    lo=2*s
    tail=F(0) if z==0 else 2*term/F(2*M+1)/(1-zz)
    return lo,lo+tail
@lru_cache(None)
def ln2iv(M=44): return lnred(F(2),M)
def log2iv(x,M=44):
    e=flog2(x); y=x/p2(e); nlo,nhi=lnred(y,M); dlo,dhi=ln2iv(M)
    return F(e)+nlo/dhi,F(e)+nhi/dlo

def Hprime_iv():
    # h'(x)=-log2 x-log2 e.  The constant -log2 e cancels because sum a*b=0.
    lo=hi=F(0)
    for ab,a2 in TERMS:
        llo,lhi=log2iv(a2)
        c=-2*ab
        if c>=0: lo+=c*llo; hi+=c*lhi
        else: lo+=c*lhi; hi+=c*llo
    return lo,hi

def div_pos(c,A):
    assert c>=0 and A[0]>0
    return c/A[1],c/A[0]

def tail_center_slope_iv():
    # d/dv Gamma_0((1-v)/2) at v=0+, using the first authentic cell.
    L=lnred(F(1024,1023))
    Q=div_pos((G[1]-G[0])/2,L)
    return -G[0]/2+Q[0],-G[0]/2+Q[1]

def cell_deriv_iv(j,knot):
    # d Gamma_0(s)/ds on cell j, evaluated at the specified endpoint value.
    L=lnred(F(1024-j,1023-j))
    Q=div_pos(G[j+1]-G[j],L)
    return knot-Q[1],knot-Q[0]

def eta_dp(p):
    m=1-2*p
    return 8*m**3-12*EPS*m*(1-m*m)**2

def add_exact(A,x): return A[0]+x,A[1]+x

HP=Hprime_iv()
T=tail_center_slope_iv()
extra=ADAG*(1-2*q0)+LAM*eta_dp(q0)
# u>0 sends q below q0 into cell 5; u<0 sends it above q0 into cell 4.
GD=add_exact(cell_deriv_iv(5,G[5]),extra)
GU=add_exact(cell_deriv_iv(4,G[5]),extra)
LP=(BETA*T[0]+GD[0]/512-HP[1], BETA*T[1]+GD[1]/512-HP[0])
LM=(BETA*T[0]-GU[1]/512+HP[0], BETA*T[1]-GU[0]/512+HP[1])
assert LP[0] > F(6,100)
assert LM[0] > F(8,100)

print('PASS')
print('truth_sha256',EXPECTED_SHA)
print('core_bias',P,'core_mean',t)
print('tail_zero_based',9,'tail_one_based',10)
print('bright_packet_mass',BRIGHT,'dark_packet_mass',DARK,'tail_influence_at_u0',BETA)
print('output_q0',q0,'dq_du',qprime)
print('H_regular_derivative_interval',float(HP[0]),float(HP[1]))
print('tail_center_cusp_slope_interval',float(T[0]),float(T[1]))
print('positive_u_linear_defect_slope_interval',float(LP[0]),float(LP[1]))
print('negative_u_abs_linear_defect_slope_interval',float(LM[0]),float(LM[1]))
print('mixed_entropy_log_coefficient',BRIGHT)
print('full_FEI_status','OPEN')
