from fractions import Fraction as F
from collections import Counter
from functools import lru_cache

TERMS=20
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
        for s in range(0,len(a),2*h):
            for j in range(s,s+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a

base=int(''.join(SLICES[0]),16)
masks=[int(''.join(row),16)^base for row in SLICES[1:]]
hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
a=[-1 if (base>>x)&1 else 1 for x in range(512)]
for h in hosts:
    for x in h:a[x]=0
A=fwht(a)
Qs=[]
for lo,hi in hosts:
    q=[0]*512; q[lo]=1; q[hi]=-1; Qs.append(fwht(q))
Qsum=[sum(row[i] for row in Qs) for i in range(512)]

assert max(abs(x) for x in A)==114
assert max(abs(x) for x in Qsum)==18
assert min(abs(x) for x in A if x) == 2
assert all(q==0 for a0,q in zip(A,Qsum) if a0==0)

@lru_cache(maxsize=None)
def ln_unit_interval(x):
    x=F(x); assert 1<=x<=2
    if x==1:return F(0),F(0)
    z=(x-1)/(x+1); z2=z*z; p=z; s=F(0)
    for k in range(TERMS):
        s += p/(2*k+1); p*=z2
    lo=2*s
    rem=2*p/((2*TERMS+1)*(1-z2))
    return lo,lo+rem

LN2_LO,LN2_HI=ln_unit_interval(F(2))
assert LN2_LO > F(2,3)

@lru_cache(maxsize=None)
def log2_interval(x):
    x=F(x)
    if x<1:
        lo,hi=log2_interval(1/x); return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<F(2)**e:e-=1
    m=x/F(2)**e
    lo,hi=ln_unit_interval(m)
    return F(e)+lo/LN2_HI, F(e)+hi/LN2_LO

def entropy_hist(hist,norm):
    lo=hi=F(0)
    for s,m in hist.items():
        if not s:continue
        l,h=log2_interval(F(norm,s)); w=F(s*m,norm)
        lo+=w*l; hi+=w*h
    return lo,hi

def phi_interval(x):
    x=F(x)
    if not x:return F(0),F(0)
    l,h=log2_interval(1/x)
    return x*l,x*h

def hcore_interval(b):
    b=F(b); num,den=b.numerator,b.denominator
    nums=[aa*den+num*q for aa,q in zip(A,Qsum)]
    norm=(512*den)**2
    return entropy_hist(Counter(v*v for v in nums if v),norm)

def parse_decimal(s):
    aa,bb=s.split('.'); return F(int(aa+bb),10**len(bb))

def dec(x,d=30):
    sign='-' if x<0 else ''; x=abs(x); scale=10**d
    q=x.numerator*scale//x.denominator
    return f"{sign}{q//scale}.{q%scale:0{d}d}"

# Rigorous derivative envelope |K'(b)|<200 on 0.0024 <= b <= 0.0026.
pmin=(F(195,100)/512)**2
_,lgp=log2_interval(1/pmin)
assert lgp < F(33,2)
pprime=F(2*18*115,512**2)
Hder=512*18*pprime
assert Hder < 146
bmin=F(24,10000); bmax=F(26,10000)
_,lgb=log2_interval(1/(bmin*bmin))
assert lgb+F(3,2) < 19
scalar_der=F(9,256)*(2*bmax*19+32*bmax)
assert Hder+scalar_der < 200
LIP=F(200)

# Exact source recurrences through F4 for c and I only.
c=F(14593,65536)
I=F(68013,32768)
for _ in range(3):
    c=F(57,256)+c**4/F(256)
    I=F(261,128)+F(9,256)*(I**4-1)
c4,I4=c,I
b4=c4**4
I5=F(261,128)+F(9,256)*(I4**4-1)
w4=F(133,128)/(I5-1)
assert 0<w4<1 and I5>231

# Tiny exact neighborhood of b4 around a low-denominator rational b0.
b0=F(2458184508619374,10**18)
delta4=abs(b4-b0)
hlo,hhi=hcore_interval(b0)
plo,phi=phi_interval(b0*b0)
Klo=hlo+F(9,256)*(-phi+16*(1-b0*b0))
Khi=hhi+F(9,256)*(-plo+16*(1-b0*b0))
T4lo=F(128,133)*(Klo-LIP*delta4)
T4hi=F(128,133)*(Khi+LIP*delta4)

# Certified F4 ratio interval from fleet03/B18 source-exact checker.
R4lo=parse_decimal('6.5218509485644448965490881329959858569477358114202361')
R4hi=parse_decimal('6.5218509485644448965496895824490791318643557898359042')
R5lo=(1-w4)*R4lo+w4*T4lo
R5hi=(1-w4)*R4hi+w4*T4hi
assert R5lo > parse_decimal('6.5218509495504459457')
assert R5hi < parse_decimal('6.5218509495504459460')

# Invariant interval for every c_t, t>=4, and uniform threshold bounds.
cL=F(22266585228,10**11); cU=F(22266585229,10**11)
f=lambda z:F(57,256)+z**4/F(256)
assert cL<c4<cU
assert cL<f(cL) and f(cU)<cU
bL,bU=cL**4,cU**4
dB=max(abs(bL-b0),abs(bU-b0))
Tmin=F(128,133)*(Klo-LIP*dB)
Tmax=F(128,133)*(Khi+LIP*dB)
assert Tmin > parse_decimal('6.52185116729')
assert Tmax < parse_decimal('6.52185116741')
assert R5hi<Tmin

# All-future tail. From I5>200, I6-1 > (9/256)200^4=56,250,000.
sumw=F(18472224,10**15)
assert sumw > F(133,128)/F(56250000)
z=F(1,56250000)
remainder=2*F(133,128)*z*z/(1-z*z)
assert remainder < F(1,10**15)

tail=(Tmax-R5lo)*sumw
Rinf_hi=R5hi+tail
assert tail < F(41,10**16)
assert Rinf_hi < Tmin
assert Rinf_hi < parse_decimal('6.5218509495504501')

print('PASS')
print('c4=',dec(c4,45))
print('I4=',dec(I4,35))
print('I5=',dec(I5,35))
print('T4_lower=',dec(T4lo,45))
print('T4_upper=',dec(T4hi,45))
print('R5_lower=',dec(R5lo,45))
print('R5_upper=',dec(R5hi,45))
print('T_uniform_lower=',dec(Tmin,45))
print('T_uniform_upper=',dec(Tmax,45))
print('future_tail_upper=',dec(tail,30))
print('R_infty_upper=',dec(Rinf_hi,45))
print('new_FEI_lower_bound=6.5218509495504459457')
print('full_FEI=OPEN_NOT_PROVED')
