from fractions import Fraction as F
from math import comb, factorial

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return trim(out)

def sub(a,b):
    n=max(len(a),len(b))
    return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n)])

def scale(a,c): return trim([c*x for x in a])
def deriv(a): return trim([F(i)*a[i] for i in range(1,len(a))]) if len(a)>1 else [F(0)]

def divrem(a,b):
    a=trim(a[:]); b=trim(b[:]); q=[F(0)]*max(1,len(a)-len(b)+1)
    if b==[0]: raise ZeroDivisionError
    while a != [0] and len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]/b[-1]; q[k]=c
        for j in range(len(b)): a[j+k]-=c*b[j]
        a=trim(a)
    return trim(q),trim(a)

def val(p,x):
    s=F(0)
    for c in reversed(p): s=s*x+c
    return s

def sturm(p):
    seq=[trim(p),deriv(p)]
    while seq[-1] != [0]:
        _,r=divrem(seq[-2],seq[-1])
        if r==[0]: break
        seq.append(scale(r,-1))
    return seq

def sgn(x): return 1 if x>0 else -1 if x<0 else 0
def var(seq,x):
    z=[sgn(val(p,x)) for p in seq]
    z=[s for s in z if s]
    return sum(z[i]!=z[i-1] for i in range(1,len(z)))

def roots(p,a,b):
    seq=sturm(p)
    return var(seq,a)-var(seq,b)

def mH(j): return F(3**j,2*j+1)
def mS(k):
    return F(1,2**k)*sum(F(comb(2*k,2*j))*mH(j)*mH(k-j) for j in range(k+1))
def U(N):
    return [F((-1)**k)*mS(k)/factorial(k) for k in range(N+1)]

# 0<q<=1/2: r(q)^2<1 from the degree-6 Taylor majorant.
u6=U(6)
p6=sub(mul([F(1),F(2)],mul(u6,u6)),[F(1)])
assert p6[0]==p6[1]==0
p6=p6[2:]
assert roots(p6,F(0),F(1,2))==0
assert val(p6,F(0))<0 and val(p6,F(1,2))<0

# 0.49<=q<=1: r(q)^2<0.99^2 from the degree-12 Taylor majorant.
u12=U(12)
p12=sub(mul([F(1),F(2)],mul(u12,u12)),[F(9801,10000)])
assert roots(p12,F(49,100),F(1))==0
assert val(p12,F(49,100))<0 and val(p12,F(1))<0

# q>=1 elementary erf/exponential majorant; these are the cleared quartics.
p1=[F(442225),F(-3851680),F(9271266),F(-7703360),F(773632)]
p99=[F(442225),F(-3851680),F(9271266),F(-7703360),F(1092032)]
assert roots(p1,F(1),F(17,2))==0
assert val(p1,F(1))<0 and val(p1,F(17,2))<0
assert roots(p99,F(1),F(13,4))==0
assert val(p99,F(1))<0 and val(p99,F(13,4))<0

# Elementary constants used in the analytic proof.
e6_lower=sum(F(6**k,factorial(k)) for k in range(14))
assert e6_lower>400
assert F(11,21)<F(181**2,250**2)   # sqrt(pi/6)<181/250 from pi<22/7
assert F(517,490)<F(10609,10000)    # global r(q)<1.03 for q>=70

# Angle split c0=139/141.
c0=F(139,141)
q1_inf=(1+c0)/(2*(1-c0))
q1_min=F(1,2)*(1+c0)/(2*(1+F(1,2)*(1-c0)))
q2_inf=(1-c0)/(2*(1+c0))
assert q1_inf==70
assert q1_min==F(35,71)>F(49,100)
assert q2_inf==F(1,280)

# Tail fraction tau<1/5 because sqrt(10)>tan(2pi/5)=sqrt(5+2sqrt(5));
# after squaring the final radical comparison reduces to 25>20.
assert 25>20
assert F(99,100)+F(4,100)*F(1,5) == F(499,500)

print("PASS")
print("P6 roots on [0,1/2]:", roots(p6,F(0),F(1,2)))
print("P12 roots on [49/100,1]:", roots(p12,F(49,100),F(1)))
print("rough r<=1 quartic roots on [1,17/2]:", roots(p1,F(1),F(17,2)))
print("rough r<=0.99 quartic roots on [1,13/4]:", roots(p99,F(1),F(13,4)))
print("e^6 Taylor lower bound:", e6_lower)
print("angle split:", "q1_inf=",q1_inf,"q1_min=",q1_min,"q2_inf=",q2_inf)
print("high-angle weighted ratio bound: < 499/500 = 0.998")
