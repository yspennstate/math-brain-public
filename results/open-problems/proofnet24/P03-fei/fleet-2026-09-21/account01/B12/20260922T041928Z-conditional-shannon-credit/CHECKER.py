import math, random

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def norm(v):
    s=math.sqrt(sum(x*x for x in v))
    return [x/s for x in v]

def credit_bounds(a,b,t):
    q=1.0-t
    m=[q*x*x+t*y*y for x,y in zip(a,b)]
    z=[t*q*(y-x)*(y-x) for x,y in zip(a,b)]
    eta=[(t*y*y/mm if mm>0 else 0.0) for y,mm in zip(b,m)]
    theta=[(zz/mm if mm>0 else 0.0) for zz,mm in zip(z,m)]
    u=sum(z)
    hb=sum(mm*h2(e) for mm,e in zip(m,eta))
    ij=h2(u)-sum(mm*h2(th) for mm,th in zip(m,theta))
    kbr=4*t*q*sum((x*x*y*y/mm if mm>0 else 0.0) for x,y,mm in zip(a,b,m))
    kvar=sum((zz*zz/mm if mm>0 else 0.0) for zz,mm in zip(z,m))-u*u
    kvert=(2/math.log(2))*kvar
    return hb,ij,kbr,kvert,u

# scalar entropy inequality on a dense deterministic grid
ming=1e9
for k in range(1,100000):
    x=k/100000.0
    ming=min(ming,h2(x)-4*x*(1-x))
assert ming > -2e-15

# deterministic random normalized coefficient-vector regression
random.seed(20260922041928)
min_branch=1e9
min_vertical=1e9
for _ in range(10000):
    n=random.randint(2,32)
    a=norm([random.gauss(0,1) for _ in range(n)])
    b=norm([random.gauss(0,1) for _ in range(n)])
    t=0.001+0.998*random.random()
    hb,ij,kbr,kvert,u=credit_bounds(a,b,t)
    min_branch=min(min_branch,hb-kbr)
    min_vertical=min(min_vertical,ij-kvert)
    assert hb+1e-12 >= kbr
    assert ij+1e-12 >= kvert

# exact Boolean zero-credit obstruction: f0=1, f1=chi_1 at t=1/2
a=[1.0,0.0]
b=[0.0,1.0]
hb,ij,kbr,kvert,u=credit_bounds(a,b,0.5)
C=hb+ij
# f0 mean=1 => r0=0; f1 mean=0 => r1=1/2; delta=1/2
W=0.25*(0.5-0.25)
assert abs(C) < 1e-15
assert abs(W-1/16) < 1e-15

# B0 uniform middle-pivot coefficient vectors over supports:
# empty, x3, x0, x0x3, x1, x1x3
a=[-0.5,-0.5,-0.5,0.5,0.0,0.0]
b=[0.5,-0.5,0.0,0.0,-0.5,-0.5]
hb,ij,kbr,kvert,u=credit_bounds(a,b,0.5)
assert abs(hb-0.5)<1e-15
assert abs(ij-0.5)<1e-15
assert abs(kbr-0.5)<1e-15
assert abs(kvert-1/(4*math.log(2)))<1e-15
C0=6.4548
astar=0.2682048
Cstar=6.5218512
gamma_quarter=(C0-2)+astar*(3/16)
Rstar=gamma_quarter-0.5*Cstar-2
Lambda_lb=Rstar+kbr+kvert
assert Lambda_lb > 0
print("PASS")
print("grid_min_h2_minus_4x1mx=%.18g"%ming)
print("random_min_branch_gap=%.18g"%min_branch)
print("random_min_vertical_gap=%.18g"%min_vertical)
print("zero_credit_example_C=%.18g W=%.18g"%(C,W))
print("B0_uniform_HB=%.18g ISJ=%.18g Kbr=%.18g Kvert=%.18g"%(hb,ij,kbr,kvert))
print("B0_uniform_DeltaH_upper=%.18g"%(2-kbr-kvert))
print("B0_uniform_Lambda_lower=%.18g"%Lambda_lb)
