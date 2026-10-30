from fractions import Fraction as F
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
    return tab.ravel()

def fwht(v):
    a=np.asarray(v,dtype=np.int64).copy(); h=1
    while h<len(a):
        b=a.reshape(-1,2*h); x=b[:,:h].copy(); y=b[:,h:].copy()
        b[:,:h]=x+y; b[:,h:]=x-y; h*=2
    return a

def eta4(p):
    return p*(1-p)*(1-2*p*(1-p))

EPS=F(113009,5000000)
def phi(m):
    return 1-m**4-EPS*(1-m**2)**3

TAB=reconstruct()
assert sha256(','.join(map(str,TAB)).encode()).hexdigest()==EXPECTED_SHA
W=fwht(TAB)
assert TAB.sum()==0 and int(np.dot(W,W))==N*N
alpha=F(int(W[1]),N)
assert alpha==F(57,256)

# Strong actual-Boolean one-core witness imported from fleet03/B17.
p=F(223,456)
q=F(1019,2048)
assert q==F(1,2)-alpha*(F(1,2)-p)
t=1-2*p
tn,td=t.numerator,t.denominator
den=N*N*td*td
om=td*td-tn*tn
numI=numIi=0
for s in range(0,N,2):
    A=int(W[s]); B=int(W[s+1])
    n0=(A*td-B*tn)**2
    n1=om*B*B
    numI += s.bit_count()*n0+(s+1).bit_count()*n1
    numIi += n1
I=F(numI,den)
Ii=F(numIi,den)
rest=I-Ii
Vp=4*p*(1-p)
v=4*q*(1-q)
assert Ii/Vp==alpha
assert rest==F(465,256)

# Quadratic, quartic and new shaped defect currencies on this same Boolean source.
M2=(I-v)/4
assert M2==F(62098577,239075328)
L4=alpha*eta4(p)+rest*F(1,8)-eta4(q)
assert L4==F(211575825297187673,1628974855061766144)
Lshape=alpha*phi(t)+rest*phi(F(0))-phi(alpha*t)
assert Lshape==F(3522569893845884171958045614703407,3468518558332143666368348160000000)

# Imported source-certified fleet03/B17 defect has width <2e-32 around
# -0.0380237343652791923.  These deliberately coarser rational endpoints contain it.
Dlo=F(-38023735,10**9)
Dhi=F(-38023734,10**9)

# Previous fleet02/B17 cardinality/quadratic replacement is refuted.
cdag=F(33525607,125000000)  # 0.268204856
c1=F(34,100)
D1_hi=Dhi+(c1-cdag)*M2
assert D1_hi<0

# The earlier fleet02/B14 scale of the universally-safe shaped direction is also refuted.
lam_old_shape=F(867221,50000000)
Doldshape_hi=Dhi+lam_old_shape*Lshape
assert Doldshape_hi<0

# Same-run replacement: rescale the source-valid singleton-restriction direction.
lam=F(374403,10000000)  # 0.0374403
Dnew_lo=Dlo+lam*Lshape
assert Dnew_lo>0
Cdag=F(3260925607,500000000)  # 6.521851214
eta_center=phi(F(0))
Cnew=Cdag+lam*eta_center
assert Cnew==F(327922264791373,50000000000000)

# It beats the center any pure quadratic repair can have for this witness.
quad_center_lower=Cdag+(-Dhi/M2)/4
assert Cnew<quad_center_lower

# It also beats the lower center forced on a pure quartic repair by the same witness.
quartic_center_lower=Cdag+(-Dhi/L4)/8
assert Cnew<quartic_center_lower

# Exact center-efficiency ordering at the strong one-core source.
E2=4*M2
E4=8*L4
Eshape=Lshape/eta_center
assert Eshape>E4>E2

# Guardrail: the obvious pure sixth-moment monotone repair already fails on an
# actual two-input Boolean gate (+1 only at (+1,-1)), biases 7/10 and 2/5.
m1=F(-2,5); m2=F(1,5); mu=F(-19,25)
a1=F(2,5); a2=F(3,10)
gap6=a1*(1-m1**6)+a2*(1-m2**6)-(1-mu**6)
assert gap6==F(-26600994,244140625)
eta6_currency=gap6/12
assert eta6_currency==F(-4433499,488281250)<0

print('PASS')
print('truth_sha256',EXPECTED_SHA)
print('alpha',alpha,'other_pivotal_sum',rest)
print('strong_p',p,'strong_output',q)
print('quadratic_currency_M2',M2,float(M2))
print('quartic_currency_L4',L4,float(L4))
print('shaped_currency_Lshape',Lshape,float(Lshape))
print('Gamma1_defect_upper',float(D1_hi))
print('old_shaped_defect_upper',float(Doldshape_hi))
print('new_shaped_lambda',lam,float(lam))
print('new_shaped_defect_lower',float(Dnew_lo))
print('new_shaped_center',float(Cnew))
print('pure_quadratic_center_lower',float(quad_center_lower))
print('pure_quartic_center_lower',float(quartic_center_lower))
print('shape_efficiency',float(Eshape),'quartic_efficiency',float(E4),'quadratic_efficiency',float(E2))
print('sextic_currency_counterexample',eta6_currency,float(eta6_currency))
