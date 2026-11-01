from fractions import Fraction
from decimal import Decimal, getcontext
from collections import defaultdict
getcontext().prec=90

CERT=[
((1080,1081),(3,8),4820718911,661801480960),
((4,1081),(1,4),14462156733,5294411847680),
((1072,1081),(1,4),10350575,43665252352),
((1072,1081),(3,8),1915,2117764739072),
((16,1081),(1,4),14462156733,21177647390720),
((18,1081),(1,2),30640,517032407),
((1026,1081),(1,2),1915,33090074048),
((1024,1081),(1081,2048),443569786466041,572325920734208),
((1024,1081),(1,2),309596144080163,2710738866012160),
((64,1081),(1,4),14462156733,84710589562880),
((1014,1081),(1,2),10350575,5458156544),
((1010,1081),(1,2),1915,2068129628),
((72,1081),(1,4),15320,517032407),
((110,1081),(1,2),1915,66180148096),
((128,1081),(1,2),14462156733,338842358251520),
((912,1081),(1,4),4820718911,41362592560),
((910,1081),(1,2),10350575,170567392),
((880,1081),(1,2),1915,529441184768),
((228,1081),(1,4),4820718911,10340648140),
((268,1081),(1,4),10350575,10916313088),
((1,4),(284,1081),1915,4136259256),
((1,4),(288,1081),3830,517032407),
((1,4),(684,1081),10350575,341134784),
((1,4),(440,1081),1915,132360296192),
((1,4),(512,1081),14462156733,677684716503040),
((794,1081),(1,2),10350575,1364539136),
((768,1081),(1081,2048),1225600,5330231),
((338,1081),(1,2),4820718911,165450370240),
((402,1081),(1,2),1915,1058882369536),
((676,1081),(1,2),4820718911,330900740480),
((626,1081),(1,2),10350575,85283696),
((576,1081),(1,2),1915,1034064814),
((574,1081),(1,2),10350575,2729078272),
((1081,2048),(512,1081),30958168192343,143081480183552),
((568,1081),(1,2),1915,16545037024)
]

def canon(x): return min(x,1-x)
def pow2f(k): return Fraction(2**k) if k>=0 else Fraction(1,2**(-k))
def flog2(x):
    k=x.numerator.bit_length()-x.denominator.bit_length()
    while x<pow2f(k): k-=1
    while x>=pow2f(k+1): k+=1
    return k
def ln2_iv(N=180):
    z=Fraction(1,3); z2=z*z; zp=z; s=Fraction(0)
    for n in range(N):
        s += zp/Fraction(2*n+1); zp*=z2
    lo=2*s
    return lo, lo+Fraction(2)*zp/Fraction(2*N+1)/(1-z2)
LN2=ln2_iv()

def log2_iv(x,N=110):
    k=flog2(x); m=x/pow2f(k)
    z=(m-1)/(m+1); z2=z*z; zp=z; s=Fraction(0)
    for n in range(N):
        s += zp/Fraction(2*n+1); zp*=z2
    lmlo=2*s
    lmhi=lmlo+(Fraction(2)*zp/Fraction(2*N+1)/(1-z2) if z else 0)
    return Fraction(k)+lmlo/LN2[1], Fraction(k)+lmhi/LN2[0]
def neglog2_iv(x):
    lo,hi=log2_iv(x); return -hi,-lo
def add(a,b): return a[0]+b[0], a[1]+b[1]
def scale(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def psi_iv(z):
    w=(1-2*z)**2
    if w==0:return Fraction(0),Fraction(0)
    lo,hi=neglog2_iv(w)
    return w*lo/z,w*hi/z
def E_iv(p,q):
    lp=neglog2_iv(p); lq=neglog2_iv(q)
    out=scale(Fraction(8)*p*(1-q),lp)
    out=add(out,scale(Fraction(8)*q*(1-p),lq))
    c=Fraction(8)*(1-p)*(1-q); out=add(out,(c,c))
    out=add(out,psi_iv(p*q))
    out=add(out,scale(-1,psi_iv(p)))
    out=add(out,scale(-1,psi_iv(q)))
    return out

# Exact dual identity for every symmetric perturbation psi.
coef=defaultdict(Fraction)
for pr,qr,ln,ld in CERT:
    p=Fraction(*pr);q=Fraction(*qr);lam=Fraction(ln,ld)
    coef[canon(p)] -= lam*q
    coef[canon(q)] -= lam*p
    coef[canon(p*q)] += lam
coef={k:v for k,v in coef.items() if v}
target={
 Fraction(3,8):Fraction(57,256),
 Fraction(967,2048):Fraction(-1),
 Fraction(1,2):Fraction(23156036957147,44712962557360)
}
assert coef==target

# Exact quadratic cost.
kappa=sum((Fraction(ln,ld)*Fraction(*pr)*Fraction(*qr)*(1-Fraction(*pr))*(1-Fraction(*qr))
           for pr,qr,ln,ld in CERT),Fraction(0))
assert kappa==Fraction(792001822391570453,11721234856636579840)

# Entropy-side constant C_E = sum lambda * p q E(p,q), rigorously enclosed.
CElo=CEhi=Fraction(0)
for pr,qr,ln,ld in CERT:
    p=Fraction(*pr);q=Fraction(*qr);lam=Fraction(ln,ld)
    lo,hi=E_iv(p,q); fac=lam*p*q
    CElo+=fac*lo; CEhi+=fac*hi

# Source-exact h96 nodes from fleet03/B12.
beta=target[Fraction(1,2)]
G38=Fraction(8766995320315105,562949953421312)
Gr=Fraction(7680879056207109,562949953421312)
gam0_38=Fraction(3,8)*G38
gam0_r=Fraction(967,2048)*Gr
gam0_h=Fraction(16137,2500)
def weighted_slack(a):
    g38=gam0_38+a*Fraction(3,8)*Fraction(5,8)
    r=Fraction(967,2048)
    gr=gam0_r+a*r*(1-r)
    gh=gam0_h+a*Fraction(1,4)
    R=Fraction(57,256)*g38-gr
    c=-R-beta*gh
    return c-CEhi,c-CElo

S0=weighted_slack(Fraction(0))
S01=weighted_slack(Fraction(1,100))
adag=Fraction(268204856,10**9)
Sdag=weighted_slack(adag)
A=adag-Fraction(1,100)
bank=A*kappa

D=lambda x: Decimal(x.numerator)/Decimal(x.denominator)
def show(name,iv):
    print(name+"_lo="+str(D(iv[0])))
    print(name+"_hi="+str(D(iv[1])))
    print(name+"_width="+str(D(iv[1]-iv[0])))

print("dual_support="+str({str(k):str(v) for k,v in sorted(coef.items())}))
print("kappa="+str(D(kappa)))
show("C_E",(CElo,CEhi))
show("S_Gamma0",S0)
show("S_Gamma01",S01)
show("S_Gammadagger",Sdag)
print("uniform_added_bank="+str(D(bank)))
print("increment_lower_minus_bank="+str(D((Sdag[0]-S01[1])-bank)))
print("increment_upper_minus_bank="+str(D((Sdag[1]-S01[0])-bank)))
assert Sdag[0]-S01[1] <= bank <= Sdag[1]-S01[0]
assert Sdag[0] > Fraction(18,100)
print("PASS")
