from fractions import Fraction as Q
from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING
from pathlib import Path
import json, math
ROOT=Path(__file__).resolve().parents[1]
N=60
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def scale(c,a):return tuple(sorted((c*a[0],c*a[1])))
def divide(a,b):
    assert b[0]>0
    corners=[x/y for x in a for y in b]
    return min(corners),max(corners)
def atan(x):
    s=sum((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(N))
    nxt=(-1)**N*x**(2*N+1)/Q(2*N+1)
    return min(s,s+nxt),max(s,s+nxt)
PI=plus(scale(16,atan(Q(1,5))),scale(-4,atan(Q(1,239))))
e0=sum(Q(1,math.factorial(k)) for k in range(N+1))
E=(e0,e0+Q(1,math.factorial(N+1))/(1-Q(1,N+2)))
def log_atanh(x):
    assert x>=1
    z=(x-1)/(x+1)
    s=2*sum(z**(2*k+1)/Q(2*k+1) for k in range(N))
    tail=2*z**(2*N+1)/Q(2*N+1)/(1-z*z)
    return s,s+tail
LN2=log_atanh(Q(2))
def ln(x):
    k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    return plus(log_atanh(x),scale(k,LN2))
def ln_interval(x):
    # Widen huge exact series rationals to a fixed rational mesh before powers.
    mesh=10**30
    low=Q((x[0]*mesh).__floor__(),mesh)
    high=Q((x[1]*mesh).__ceil__(),mesh)
    return ln(low)[0],ln(high)[1]
creg=divide(plus(ln_interval(plus((Q(4),Q(4)),E)),scale(2,plus((Q(1),Q(1)),ln_interval(PI)))),LN2)
ct=plus((Q(80),Q(80)),divide((Q(460),Q(460)),LN2))
andc=plus((Q(2),Q(2)),divide((Q(4),Q(4)),LN2))
parity=divide((Q(2),Q(2)),LN2)
beta_squared=divide((Q(2),Q(2)),(1-LN2[1],1-LN2[0]))
assert creg[1]<Q(8937,1000) and creg[0]>4
assert ct[1]<744 and andc[1]<Q(7771,1000)
assert beta_squared[1]<Q(2553,1000)**2
assert ct[1]+Q(2553,1000)<747
def outward(x):
    out=[]
    for z,rounding in zip(x,[ROUND_FLOOR,ROUND_CEILING]):
        with localcontext() as c:
            c.prec=100;c.rounding=rounding
            out.append(str((Decimal(z.numerator)/Decimal(z.denominator)).quantize(Decimal('1e-18'))))
    return out
vals={'C_reg':creg,'4C_reg':scale(4,creg),'C_T':ct,'AND_OR':andc,'parity':parity,'beta_squared':beta_squared,'C_reg_plus_4':plus(creg,(Q(4),Q(4)))}
out={'series_terms':N,'proof':'exp positive series with geometric tail; Machin pi with alternating atan tails; ln range reduction plus atanh geometric tail; all signed interval divisions use four corners','enclosures':{k:outward(v) for k,v in vals.items()},'inequalities':['4<C_reg<8.937','C_T<744','beta<2.553','C_T+beta<747'],'status':'PASS'}
(ROOT/'out/constants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
