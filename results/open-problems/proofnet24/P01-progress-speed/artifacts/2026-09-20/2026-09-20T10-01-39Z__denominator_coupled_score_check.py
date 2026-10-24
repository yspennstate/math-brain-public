from fractions import Fraction as F

def j_new(D, lam):
    c = 1-lam
    M = D-(D-1)*lam
    A = D-1+lam
    b = D*c/M
    return (D-1)*(b/(A+b))**2

def tau(D, lam):
    return (1+lam)/(D+lam)

def theta_bar(D, lam, p):
    t = tau(D, lam)
    return p*t/(1-p+p*t)

def H(D, lam):
    return lam*j_new(D, lam)

def C(D, lam, p):
    return lam/(1-lam)-p*H(D,lam)

def delta(D, lam, p):
    th = theta_bar(D,lam,p)
    cc = C(D,lam,p)
    return 1+(D-1)*th-(D-1)*cc*th*(1-th)

def margin(D, lam, p):
    th = theta_bar(D,lam,p)
    rbar = 1+(D-1)*th
    return 2*delta(D,lam,p)/(rbar+lam)**2

def pmono(D, lam, p):
    t=tau(D,lam)
    h=H(D,lam)
    c0=lam/(1-lam)
    N=(1-c0)+p*(c0*(1+t)+t-1+2*h)-3*h*p*p+h*(1-t)*p**3
    Np=c0*(1+t)+t-1+2*h-6*h*p+3*h*(1-t)*p*p
    return N,Np

def theta_derivative_room(D, lam0, L, p0):
    cmin=C(D,lam0,p0)
    thmax=theta_bar(D,L,p0)
    return cmin*(1-2*thmax)-1

CASES = [
    ("headline",12,F(67023,100000),F(1,2),F(1,185000)),
    ("breadth_2_5",49,F(2,3),F(2,5),F(1,6600)),
    ("breadth_19_50",233,F(2,3),F(19,50),F(1,73000)),
]
lam0=F(61,100)

for name,D,L,p0,clean in CASES:
    d=delta(D,L,p0)
    m=margin(D,L,p0)
    N,Np=pmono(D,L,p0)
    room=theta_derivative_room(D,lam0,L,p0)
    static_room=D*(1-L)-(1+L)
    assert d>0
    assert m>clean
    assert N<0
    assert Np>0
    assert room>0
    assert static_room>=0
    print(name)
    print(" D,L,p0 =",D,L,p0)
    print(" delta =",d,"~",float(d))
    print(" derivative_margin =",m,"~",float(m),">",clean)
    print(" N(p0) =",N,"~",float(N))
    print(" Nprime(p0) =",Np,"~",float(Np))
    print(" theta_monotonicity_room =",room,"~",float(room))
    print(" static_ratio_room =",static_room,"~",float(static_room))
    print()

FAILS=[
    ("headline_next_1e-5",12,F(67024,100000),F(1,2)),
    ("breadth_next_D",50,F(2,3),F(2,5)),
    ("breadth_next_D_19_50",234,F(2,3),F(19,50)),
]
for name,D,L,p in FAILS:
    d=delta(D,L,p)
    assert d<0
    print(name,"delta =",d,"~",float(d))

def j_old(D,lam):
    c=1-lam
    M=D-(D-1)*lam
    return D*D*(D-1)*c*c/(M*M*(D+lam)**2)

for name,D,L,p0,clean in CASES:
    assert j_new(D,L)>j_old(D,L)
    print(name,"J_new/J_old ~",float(j_new(D,L)/j_old(D,L)))

print("ALL_EXACT_CHECKS_PASS")
