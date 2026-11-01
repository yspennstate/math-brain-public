#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb

EPS = F(56721646463783,2500000000000000)
R0 = F(8004417,20000000)
DEF = F(38023735,10**9)
LAM = F(18721807228217,500000000000000)
CDAG = F(6521851214,10**9)
OLD_SHAPED_CENTER = F(327922264791373,50000000000000)
Q4_CENTER = F(6558445589,10**9)

# Exact power coefficients of R(X,T,U) defined by
# G = d*t*(1-t)*(2-d)*R(d/2,t,u), where
# a=-1+u(2-d), b=a+d, c=-1+t*d+u(2-d),
# phi(m)=1-m^4-EPS*(1-m^2)^3, and
# G=(1-t)phi(a)+t phi(b)+(d/2)phi(1-2t)-phi(c).
POWER = {
    (4,4,0): F(-56721646463783,156250000000000),
    (4,3,1): F(170164939391349,78125000000000),
    (4,3,0): F(-56721646463783,156250000000000),
    (4,2,2): F(-170164939391349,31250000000000),
    (4,2,1): F(170164939391349,78125000000000),
    (4,2,0): F(-56721646463783,156250000000000),
    (4,1,3): F(56721646463783,7812500000000),
    (4,1,2): F(-170164939391349,31250000000000),
    (4,1,1): F(170164939391349,78125000000000),
    (4,1,0): F(-56721646463783,156250000000000),
    (4,0,4): F(-170164939391349,31250000000000),
    (4,0,3): F(56721646463783,7812500000000),
    (4,0,2): F(-170164939391349,31250000000000),
    (4,0,1): F(170164939391349,78125000000000),
    (4,0,0): F(-56721646463783,156250000000000),
    (3,4,0): F(-56721646463783,156250000000000),
    (3,3,0): F(56721646463783,78125000000000),
    (3,2,2): F(170164939391349,31250000000000),
    (3,2,1): F(-170164939391349,31250000000000),
    (3,2,0): F(56721646463783,78125000000000),
    (3,1,3): F(-56721646463783,3906250000000),
    (3,1,2): F(510494818174047,31250000000000),
    (3,1,1): F(-170164939391349,31250000000000),
    (3,1,0): F(56721646463783,78125000000000),
    (3,0,4): F(510494818174047,31250000000000),
    (3,0,3): F(-397051525246481,15625000000000),
    (3,0,2): F(510494818174047,31250000000000),
    (3,0,1): F(-170164939391349,31250000000000),
    (3,0,0): F(56721646463783,78125000000000),
    (2,4,0): F(-56721646463783,156250000000000),
    (2,3,0): F(56721646463783,78125000000000),
    (2,2,0): F(568278353536217,156250000000000),
    (2,1,3): F(56721646463783,7812500000000),
    (2,1,2): F(-170164939391349,15625000000000),
    (2,1,1): F(-454835060608651,39062500000000),
    (2,1,0): F(568278353536217,156250000000000),
    (2,0,4): F(-510494818174047,31250000000000),
    (2,0,3): F(56721646463783,1953125000000),
    (2,0,2): F(64210060608651,9765625000000),
    (2,0,1): F(-454835060608651,39062500000000),
    (2,0,0): F(568278353536217,156250000000000),
    (1,4,0): F(-56721646463783,156250000000000),
    (1,3,0): F(56721646463783,78125000000000),
    (1,2,0): F(568278353536217,156250000000000),
    (1,1,0): F(-4,1),
    (1,0,4): F(170164939391349,31250000000000),
    (1,0,3): F(-170164939391349,15625000000000),
    (1,0,2): F(-1364505181825953,78125000000000),
    (1,0,1): F(3579835060608651,156250000000000),
    (1,0,0): F(-4,1),
    (0,4,0): F(-56721646463783,156250000000000),
    (0,3,0): F(56721646463783,78125000000000),
    (0,2,0): F(568278353536217,156250000000000),
    (0,1,0): F(-4,1),
    (0,0,0): F(2,1),
}

def power_to_bernstein(power):
    n=4
    B=[[[F(0) for _ in range(5)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                z=F(0)
                for a in range(i+1):
                    for b in range(j+1):
                        for c in range(k+1):
                            A=power.get((a,b,c),F(0))
                            if A:
                                z += A*F(comb(i,a),comb(n,a))*F(comb(j,b),comb(n,b))*F(comb(k,c),comb(n,c))
                B[i][j][k]=z
    return B

def split_curve(vals):
    levels=[list(vals)]
    while len(levels[-1])>1:
        p=levels[-1]
        levels.append([(p[i]+p[i+1])/2 for i in range(len(p)-1)])
    left=[levels[i][0] for i in range(len(levels))]
    right=[levels[-1-i][i] for i in range(len(levels))]
    return left,right

def split_axis(B,axis):
    blank=lambda: [[[F(0) for _ in range(5)] for _ in range(5)] for _ in range(5)]
    L,R=blank(),blank()
    if axis==0:
        for j in range(5):
            for k in range(5):
                l,r=split_curve([B[i][j][k] for i in range(5)])
                for i in range(5): L[i][j][k],R[i][j][k]=l[i],r[i]
    elif axis==1:
        for i in range(5):
            for k in range(5):
                l,r=split_curve([B[i][j][k] for j in range(5)])
                for j in range(5): L[i][j][k],R[i][j][k]=l[j],r[j]
    else:
        for i in range(5):
            for j in range(5):
                l,r=split_curve([B[i][j][k] for k in range(5)])
                for k in range(5): L[i][j][k],R[i][j][k]=l[k],r[k]
    return L,R

def octants(B):
    parts=[B]
    for axis in range(3):
        nxt=[]
        for P in parts: nxt.extend(split_axis(P,axis))
        parts=nxt
    return parts

def flat(B):
    for plane in B:
        for row in plane:
            yield from row

def certify(B,maxdepth=36):
    stack=[(B,0)]
    leaves=nodes=max_seen=0
    min_terminal=None
    unresolved=[]
    while stack:
        Q,depth=stack.pop()
        nodes += 1
        m=min(flat(Q))
        if m>=0:
            leaves += 1
            max_seen=max(max_seen,depth)
            min_terminal=m if min_terminal is None else min(min_terminal,m)
        elif depth>=maxdepth:
            unresolved.append((depth,m))
        else:
            for child in octants(Q):
                stack.append((child,depth+1))
    return leaves,nodes,max_seen,min_terminal,unresolved

def phi(m):
    return F(1)-m**4-EPS*(F(1)-m*m)**3

B0=power_to_bernstein(POWER)
leaves,nodes,maxdepth,mincoef,unresolved=certify(B0,36)
assert not unresolved
assert (leaves,nodes,maxdepth)==(792,905,27)
MIN_EXPECTED=F(43225860035202095786322675999861897145560250299268834991580273,
 1028440348325753776346855739098344065614209916020987414592880640000000000000000)
assert mincoef==MIN_EXPECTED and mincoef>0

# Source-valid upper obstruction from the actual two-input AND/NAND line:
# t=r, delta=r, a=-1, b=-1+2r, c=-1+2r^2.
r=R0
threshold=(2*r**4+4*r**3+2*r**2-4*r+1)/(8*r**2*(r-1)*(r**5+3*r**4+3*r**3+r**2-2))
assert threshold>EPS
assert threshold-EPS < F(75,10**18)  # < 7.5e-17

# Strong Numaro source: p1=223/456, q=1019/2048.
m1=F(5,228)
mout=F(5,1024)
L=F(57,256)*phi(m1)+F(465,256)*phi(F(0))-phi(mout)
repair=LAM*L
assert repair>DEF
slack=repair-DEF
center=CDAG+LAM*phi(F(0))
assert center<OLD_SHAPED_CENTER
assert center<Q4_CENTER

print("PASS")
print("epsilon", EPS, float(EPS))
print("bernstein_terminal_boxes",leaves)
print("bernstein_nodes",nodes)
print("bernstein_max_depth",maxdepth)
print("bernstein_min_terminal_coefficient",mincoef,float(mincoef))
print("and_line_r",r,float(r))
print("and_line_epsilon_upper",threshold,float(threshold))
print("epsilon_gap_to_upper",threshold-EPS,float(threshold-EPS))
print("numaro_currency",L,float(L))
print("lambda",LAM,float(LAM))
print("repair_slack",slack,float(slack))
print("candidate_center",center,float(center))
print("improvement_over_old_shaped",OLD_SHAPED_CENTER-center,float(OLD_SHAPED_CENTER-center))
print("improvement_over_q4",Q4_CENTER-center,float(Q4_CENTER-center))
