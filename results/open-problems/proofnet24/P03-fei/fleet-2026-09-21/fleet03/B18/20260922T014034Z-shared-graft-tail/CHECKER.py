from fractions import Fraction as F
from functools import lru_cache
from decimal import Decimal, getcontext

getcontext().prec = 100
TERMS = 40
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

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for st in range(0,len(a),2*h):
            for j in range(st,st+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def core_data():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(row),16)^base for row in SLICES[1:]]
    assert all(m.bit_count()==2 for m in masks)
    hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
    a=[-1 if (base>>x)&1 else 1 for x in range(512)]
    for host in hosts:
        for x in host: a[x]=0
    A=fwht(a)
    Q=[]
    for lo,hi in hosts:
        q=[0]*512; q[lo]=1; q[hi]=-1
        Q.append(fwht(q))
    Qsum=[sum(row[s] for row in Q) for s in range(512)]
    assert max(map(abs,A))==114
    assert max(map(abs,Qsum))==18
    assert sum(map(abs,Qsum))==1584
    return A,Qsum

def p2(k):
    return F(1<<k) if k>=0 else F(1,1<<(-k))

def log_unit(x):
    assert F(1)<=x<=F(2)
    if x==1:return F(0),F(0)
    z=(x-1)/(x+1); z2=z*z; p=z; s=F(0)
    for j in range(TERMS):
        s += p/F(2*j+1); p *= z2
    lo=2*s
    hi=lo+2*p/(F(2*TERMS+1)*(1-z2))
    return lo,hi

@lru_cache(None)
def log2i(x):
    x=F(x)
    if x<1:
        lo,hi=log2i(1/x); return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<p2(e): e-=1
    m=x/p2(e)
    a,b=log_unit(m); c,d=log_unit(F(2))
    return F(e)+a/d,F(e)+b/c

def phi_i(x):
    x=F(x)
    if not x:return F(0),F(0)
    a,b=log2i(1/x)
    return x*a,x*b

def hcore_i(A,Q,b):
    lo=hi=F(0)
    for a,q in zip(A,Q):
        z=F(a,512)+b*F(q,512)
        x=z*z
        a0,b0=phi_i(x)
        lo+=a0; hi+=b0
    return lo,hi

def K_i(A,Q,b):
    alpha=F(9,256)
    lo,hi=hcore_i(A,Q,b)
    p0,p1=phi_i(b*b)
    extra=alpha*16*(1-b*b)
    return lo-alpha*p1+extra,hi-alpha*p0+extra

def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

A,Q=core_data()
c1=F(14593,65536)
stepc=lambda c:(F(57)+c**4)/256
c2=stepc(c1); c3=stepc(c2); c4=stepc(c3)
cL=F(22266585228,10**11); cU=F(22266585229,10**11)
assert cL<c4<cU
assert stepc(cL)>cL and stepc(cU)<cU
bL,bU=cL**4,cU**4
b0=F(245818450862,10**14)
dist=max(abs(b0-bL),abs(b0-bU))
Klo,Khi=K_i(A,Q,b0)
# REPORT.md proves |K'(b)|<19 on [bL,bU].
Tlo=F(128,133)*(Klo-19*dist)
Thi=F(128,133)*(Khi+19*dist)
assert Tlo>F('6.52185116734')
assert Thi<F('6.52185116736')

alpha=F(9,256)
stepI=lambda I:F(513,256)+alpha*I**4
I1=F(68013,32768); I2=stepI(I1); I3=stepI(I2); I4=stepI(I3); I5=stepI(I4)
q=F(133,128)
lam4=q/(I5-1)
assert F('0.0045')<lam4<F('0.00452')
assert F(231)<I5<F(232)
lam5up=q/(F(9,256)*F(231)**4)
assert lam5up<F(11,10**9)
sumlam=F('0.00452')+2*lam5up

R4lo=F('6.5218509485644448965490881329959858569477358114202361')
R4hi=F('6.5218509485644448965496895824490791318643557898359042')
tailrise=(Thi-R4lo)*sumlam
assert tailrise<F(1,10**9)
assert R4hi+tailrise<Tlo

R5lo=(1-lam4)*R4lo+lam4*Tlo
assert R5lo>F('6.5218509495504')
Rinfup=R4hi+tailrise

print('PASS')
print('c4='+str(dec(c4)))
print('invariant_c_lower='+str(dec(cL)))
print('invariant_c_upper='+str(dec(cU)))
print('T_lower='+str(dec(Tlo)))
print('T_upper='+str(dec(Thi)))
print('lambda4='+str(dec(lam4)))
print('lambda5_upper='+str(dec(lam5up)))
print('total_lambda_upper='+str(dec(sumlam)))
print('total_future_rise_upper='+str(dec(tailrise)))
print('R5_lower='+str(dec(R5lo)))
print('Rinf_upper='+str(dec(Rinfup)))
print('all_future_gains_positive=PROVED_BY_INDUCTION_IN_REPORT')
print('full_FEI=OPEN_NOT_PROVED')
