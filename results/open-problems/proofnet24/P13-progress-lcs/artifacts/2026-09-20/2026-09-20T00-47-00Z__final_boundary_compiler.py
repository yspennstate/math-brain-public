from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import product

getcontext().prec = 180
UV=((0,0),(0,1),(1,0),(1,1))

# ---------------- source endpoint compiler ----------------
LOW = Fraction(99083249, 125000000)
P02_BEFORE = Fraction(8262759427622826251, 10**19)
XN = YN = 513434
D = 1600000
A = Fraction(4*XN*YN, D*D)
LAM = Fraction(
    10114875937111444750637950885399422919832438289108176982868202874026753,
    29591135160849999997918500618240000000000000000000000000000000000000000
)

def neglog_bounds(x,n):
    u=(1-x)/(1+x)
    s=Fraction(0)
    p=u
    for j in range(n):
        s += p/(2*j+1)
        p *= u*u
    lo=2*s
    hi=lo + 2*p/((2*n+1)*(1-u*u))
    return lo,hi

def dec(q):
    return Decimal(q.numerator)/Decimal(q.denominator)

a_lo,a_hi=neglog_bounds(A,500)
l_lo,l_hi=neglog_bounds(LAM,700)
alpha_lo=a_lo/l_hi
alpha_hi=a_hi/l_lo
SCALE=10**30
P13_AFTER=Fraction((alpha_hi.numerator*SCALE)//alpha_hi.denominator+1,SCALE)
assert alpha_lo<=alpha_hi<P13_AFTER<P02_BEFORE
print("P02_UPPER_BEFORE",dec(P02_BEFORE))
print("P13_UPPER_AFTER",dec(P13_AFTER))
print("WIDTH_BEFORE",dec(P02_BEFORE-LOW))
print("WIDTH_AFTER",dec(P13_AFTER-LOW))
print("STRICT_DECREASE",dec(P02_BEFORE-P13_AFTER))
print("ENDPOINT_PASS")

# ---------------- one-column boundary extinction ----------------
def carries(x,g,v,left):
    cp=left
    out=[]
    for xi,gi in zip(x,g):
        c=0 if gi else max(cp,int(xi==v))
        out.append(c); cp=c
    return tuple(out)

def delta_formula(x,g,v):
    p=1
    out=[]
    for xi,gi in zip(x,g):
        p *= (1-gi)*int(xi!=v)
        out.append(p)
    return tuple(out)

for k in range(1,9):
    survival=0
    total=0
    for x in product((0,1),repeat=k):
        for v in (0,1):
            total += 1
            c0=carries(x,(0,)*k,v,0)
            c1=carries(x,(0,)*k,v,1)
            survival += (c1[-1]-c0[-1]==1)
        for g in product((0,1),repeat=k):
            for v in (0,1):
                c0=carries(x,g,v,0)
                c1=carries(x,g,v,1)
                delta=tuple(b-a for a,b in zip(c0,c1))
                assert delta==delta_formula(x,g,v)
                prev=1
                nz=0
                for d in delta:
                    dg=d-prev
                    assert dg in (-1,0)
                    nz += (dg!=0)
                    prev=d
                assert nz<=1
    assert Fraction(survival,total)==Fraction(1,2**k)
    print("ONE_COLUMN_SURVIVAL",k,Fraction(survival,total))
print("ONE_COLUMN_EXTINCTION_PASS")

# ---------------- one-gradient-discrepancy nonbranching ----------------
def update(w,x,g,u,v):
    L=2*w
    c=[]
    cp=0
    for i in range(L):
        ci=0 if g[i] else max(cp,int(x[i]==v))
        c.append(ci); cp=ci
    gp=[]
    for i in range(L-1):
        gp.append(g[i+1]+c[i+1]-c[i])
    gp.append((1-c[-1])*int(u==v))
    return tuple(gp)

for w in range(1,4):
    L=2*w
    checked=0
    for x in product((0,1),repeat=L):
        for g in product((0,1),repeat=L):
            for p in range(L):
                h=list(g); h[p]^=1; h=tuple(h)
                for u,v in UV:
                    a=update(w,x,g,u,v)
                    b=update(w,x,h,u,v)
                    assert sum(aa!=bb for aa,bb in zip(a,b))<=1
                    checked += 1
    print("NONBRANCHING",w,checked)
print("NONBRANCHING_PASS")

# ---------------- correct finite-horizon boundary error ----------------
# A one-discrepancy right jump J has conditional tail P(J>=r)<=2^{-r}.
# Thus J is mgf-dominated by R with P(R=r)=2^{-(r+1)}.
# For M>t, Chernoff optimization gives:
#   P(sum_{i=1}^t R_i >= M)
#   <= B(M,t)=((M+t)/(2M))^M ((M+t)/(2t))^t.
def B(M,t):
    assert M>t>0
    return Fraction((M+t)**(M+t),(2*M)**M*(2*t)**t)

def EPS(M,T):
    assert M>T>0
    return sum((B(M,t) for t in range(1,T+1)), Fraction(0))

for M,T in [(48,16),(64,16),(96,32),(128,32)]:
    eps=EPS(M,T)
    crude=T*B(M,T)
    assert eps<=crude
    print("FINITE_HORIZON_EPS","M",M,"T",T,
          "exact",eps,
          "decimal",dec(eps),
          "crude_TB",dec(crude))
print("FINITE_HORIZON_CHERNOFF_PASS")
print("ALL_EXACT_CHECKS_PASS")
