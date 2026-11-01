#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb
from itertools import product
from decimal import Decimal, getcontext

getcontext().prec = 50
NVAR = 3

def clean(p):
    return {k:v for k,v in p.items() if v}

def C(q):
    return {} if q == 0 else {(0,0,0): F(q)}

def V(axis):
    k=[0,0,0]; k[axis]=1
    return {tuple(k): F(1)}

def add(p,q):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,F(0))+v
    return clean(r)

def neg(p):
    return {k:-v for k,v in p.items()}

def sub(p,q):
    return add(p,neg(q))

def scale(p,a):
    a=F(a)
    return clean({k:a*v for k,v in p.items()})

def mul(p,q):
    r={}
    for a,va in p.items():
        for b,vb in q.items():
            k=tuple(a[i]+b[i] for i in range(NVAR))
            r[k]=r.get(k,F(0))+va*vb
    return clean(r)

def power(p,n):
    r=C(1)
    b=p
    while n:
        if n&1:
            r=mul(r,b)
        b=mul(b,b)
        n//=2
    return r

ONE=C(1)
X,T,U=V(0),V(1),V(2)
EPS=F(453773,20000000)

def phi_poly(z):
    z2=power(z,2)
    one_minus_z2=sub(ONE,z2)
    return sub(sub(ONE,power(z,4)),scale(power(one_minus_z2,3),EPS))

d=scale(X,2)
a=add(C(-1),mul(U,sub(C(2),d)))
b=add(a,d)
c=add(mul(sub(ONE,T),a),mul(T,b))
m=sub(ONE,scale(T,2))
# G=(1-t)phi(a)+t phi(b)+(d/2)phi(1-2t)-phi((1-t)a+tb)
G=add(add(mul(sub(ONE,T),phi_poly(a)),mul(T,phi_poly(b))),
      sub(mul(X,phi_poly(m)),phi_poly(c)))

degs=tuple(max((k[i] for k in G), default=0) for i in range(NVAR))
assert degs==(6,6,4), degs

def power_to_bernstein(p,degs):
    out={}
    ranges=[range(n+1) for n in degs]
    for ks in product(*ranges):
        s=F(0)
        for mon,aa in p.items():
            if all(mon[j] <= ks[j] for j in range(NVAR)):
                fac=F(1)
                for j,n in enumerate(degs):
                    fac *= F(comb(ks[j],mon[j]),comb(n,mon[j]))
                s += aa*fac
        out[ks]=s
    return out

def split_axis(arr,degs,axis):
    others=[j for j in range(NVAR) if j!=axis]
    left={}; right={}
    n=degs[axis]
    for oth in product(*[range(degs[j]+1) for j in others]):
        base=[0]*NVAR
        for j,v in zip(others,oth):
            base[j]=v
        line=[]
        for k in range(n+1):
            idx=base.copy(); idx[axis]=k
            line.append(arr[tuple(idx)])
        levels=[line]
        for _ in range(n):
            prev=levels[-1]
            levels.append([(prev[i]+prev[i+1])/2 for i in range(len(prev)-1)])
        lv=[levels[k][0] for k in range(n+1)]
        rv=[levels[n-k][k] for k in range(n+1)]
        for k in range(n+1):
            idx=base.copy(); idx[axis]=k
            left[tuple(idx)]=lv[k]
            right[tuple(idx)]=rv[k]
    return left,right

def certify(arr,degs,max_nodes=100000,max_depth=70):
    stack=[(arr,0)]
    total=terminal=unresolved=depthmax=0
    min_terminal=None
    while stack:
        cur,depth=stack.pop()
        total+=1
        depthmax=max(depthmax,depth)
        mn=min(cur.values())
        if mn>=0:
            terminal+=1
            min_terminal=mn if min_terminal is None or mn<min_terminal else min_terminal
            continue
        if total>=max_nodes or depth>=max_depth:
            unresolved+=1
            continue
        opts=[]
        for ax in range(NVAR):
            lo,hi=split_axis(cur,degs,ax)
            score=min(min(lo.values()),min(hi.values()))
            opts.append((score,-ax,ax,lo,hi))
        _,_,ax,lo,hi=max(opts,key=lambda z:(z[0],z[1]))
        stack.append((hi,depth+1))
        stack.append((lo,depth+1))
    return total,terminal,unresolved,depthmax,min_terminal

bern=power_to_bernstein(G,degs)
total,terminal,unresolved,depthmax,min_terminal=certify(bern,degs)
assert unresolved==0
assert (total,terminal,depthmax)==(159,80,26), (total,terminal,depthmax)
assert min_terminal==0

def phi_num(z,e=EPS):
    return F(1)-z**4-e*(F(1)-z*z)**3

# Genuine two-input Boolean ceiling example: pivot bias 3/5, G0=Y with
# E[Y]=1/5, G1=+1, so delta=Pr(Y=-1)=2/5.
CEILING=F(10625,468288)
critical_currency=F(4,5)*phi_num(F(1,5))-phi_num(F(17,25))
assert critical_currency == -F(288,244140625)*(F(468288)*EPS-F(10625))
assert EPS < CEILING and critical_currency>0

def eta(p):
    return phi_num(F(1)-2*p)

# Strong composition-prime Numaro source from fleet02/B17.
p1=F(223,456)
q=F(1019,2048)
L=F(57,256)*eta(p1)+F(465,256)*eta(F(1,2))-eta(q)
assert L == F(14089027843865471581106016370764179,
              13874074233328574665473392640000000)

lam=F(1872181,50000000)  # 0.03744362
deficit_upper=F(38023735,10**9)
repair_margin=lam*L-deficit_upper
assert repair_margin>0

Cbase=F(6521851214,10**9)
Cnew=Cbase+lam*eta(F(1,2))
Cold=F(327922264791373,50000000000000)  # peer executed center
assert Cnew == F(6558445288811087,10**15)
assert Cnew<Cold

def dec(x):
    return str(Decimal(x.numerator)/Decimal(x.denominator))

print("PASS nearoptimal singleton-restriction repair")
print("epsilon_new", EPS, dec(EPS))
print("epsilon_universal_ceiling", CEILING, dec(CEILING))
print("epsilon_gap_to_ceiling", CEILING-EPS, dec(CEILING-EPS))
print("critical_actual_gate_currency", critical_currency, dec(critical_currency))
print("bernstein_degrees", degs)
print("bernstein_total_boxes", total)
print("bernstein_terminal_boxes", terminal)
print("bernstein_unresolved_boxes", unresolved)
print("bernstein_max_depth", depthmax)
print("bernstein_min_terminal_coeff", min_terminal)
print("strong_prime_currency", L, dec(L))
print("strong_prime_efficiency_per_center", L/eta(F(1,2)), dec(L/eta(F(1,2))))
print("repair_lambda", lam, dec(lam))
print("certified_repair_margin_vs_deficit_upper", repair_margin, dec(repair_margin))
print("new_center", Cnew, dec(Cnew))
print("peer_old_center", Cold, dec(Cold))
print("center_improvement", Cold-Cnew, dec(Cold-Cnew))
