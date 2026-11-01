#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb

EPS = F(113009, 5000000)
LAMBDA = F(867221, 50000000)
COARSE_DEFICIENCY_UPPER = F(17611420, 10**9)
CDAG = F(6521851214, 10**9)
QUARTIC_CENTER = F(6538814964, 10**9)

# Exact polynomial R(X,T,U) in
#   scalar_gap = d*t*(1-t)*(2-d)*R(d/2,t,u),
# where c=-1+t*d+u*(2-d) and
# psi(m)=1-m^4-EPS*(1-m^2)^3.
# Degree is at most four in each variable.
POWER = {
    (4,4,0):F(-113009,312500), (4,3,1):F(339027,156250), (4,3,0):F(-113009,312500),
    (4,2,2):F(-339027,62500), (4,2,1):F(339027,156250), (4,2,0):F(-113009,312500),
    (4,1,3):F(113009,15625), (4,1,2):F(-339027,62500), (4,1,1):F(339027,156250),
    (4,1,0):F(-113009,312500), (4,0,4):F(-339027,62500), (4,0,3):F(113009,15625),
    (4,0,2):F(-339027,62500), (4,0,1):F(339027,156250), (4,0,0):F(-113009,312500),
    (3,4,0):F(-113009,312500), (3,3,0):F(113009,156250), (3,2,2):F(339027,62500),
    (3,2,1):F(-339027,62500), (3,2,0):F(113009,156250), (3,1,3):F(-226018,15625),
    (3,1,2):F(1017081,62500), (3,1,1):F(-339027,62500), (3,1,0):F(113009,156250),
    (3,0,4):F(1017081,62500), (3,0,3):F(-791063,31250), (3,0,2):F(1017081,62500),
    (3,0,1):F(-339027,62500), (3,0,0):F(113009,156250),
    (2,4,0):F(-113009,312500), (2,3,0):F(113009,156250), (2,2,0):F(1136991,312500),
    (2,1,3):F(113009,15625), (2,1,2):F(-339027,31250), (2,1,1):F(-910973,78125),
    (2,1,0):F(1136991,312500), (2,0,4):F(-1017081,62500), (2,0,3):F(452036,15625),
    (2,0,2):F(518892,78125), (2,0,1):F(-910973,78125), (2,0,0):F(1136991,312500),
    (1,4,0):F(-113009,312500), (1,3,0):F(113009,156250), (1,2,0):F(1136991,312500),
    (1,1,0):F(-4,1), (1,0,4):F(339027,62500), (1,0,3):F(-339027,31250),
    (1,0,2):F(-2732919,156250), (1,0,1):F(7160973,312500), (1,0,0):F(-4,1),
    (0,4,0):F(-113009,312500), (0,3,0):F(113009,156250), (0,2,0):F(1136991,312500),
    (0,1,0):F(-4,1), (0,0,0):F(2,1),
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
    def blank(): return [[[F(0) for _ in range(5)] for _ in range(5)] for _ in range(5)]
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

def certify(B,maxdepth=6):
    stack=[(B,0)]
    leaves=nodes=max_seen=0
    min_terminal=None
    unresolved=[]
    while stack:
        Q,depth=stack.pop(); nodes+=1
        m=min(flat(Q))
        if m>=0:
            leaves+=1; max_seen=max(max_seen,depth)
            min_terminal=m if min_terminal is None else min(min_terminal,m)
        elif depth>=maxdepth:
            unresolved.append((depth,m))
        else:
            for child in octants(Q): stack.append((child,depth+1))
    return leaves,nodes,max_seen,min_terminal,unresolved

def psi_mean(m):
    return 1-m**4-EPS*(1-m*m)**3

B0=power_to_bernstein(POWER)
leaves,nodes,maxdepth,mincoef,unresolved=certify(B0,6)
assert not unresolved
assert leaves==134 and nodes==153 and maxdepth==6
assert mincoef==F(1999313322941,16492674416640000000)
assert mincoef>0 and 0<EPS<1

# The sixth-power direction alone is unsafe on a genuine two-input NAND at p=q=2/5.
pure_g6_gap=F(4,5)*(1-F(1,5)**6)-(1-F(17,25)**6)
assert pure_g6_gap==F(-24703056,244140625) and pure_g6_gap<0

m38=F(1,4)
mout=F(57,1024)
L=F(57,256)*psi_mean(m38)+F(465,256)*psi_mean(F(0))-psi_mean(mout)
assert L==F(5853348229889641167388287,5764607523034234880000000)
repair=LAMBDA*L
repair_slack=repair-COARSE_DEFICIENCY_UPPER
assert repair_slack==F(294107345260307157640427,288230376151711744000000000000000)
assert repair_slack>0
center_factor=psi_mean(F(0))
assert center_factor==F(4886991,5000000)
center_increment=LAMBDA*center_factor
assert center_increment==F(4238101222011,250000000000000)
cap=CDAG+center_increment
assert cap==F(1634700904722011,250000000000000)
assert QUARTIC_CENTER-cap==F(2836277989,250000000000000)

print('PASS')
print('epsilon',EPS,float(EPS))
print('bernstein_terminal_boxes',leaves)
print('bernstein_nodes',nodes)
print('bernstein_max_depth',maxdepth)
print('bernstein_min_terminal_coefficient',mincoef,float(mincoef))
print('pure_g6_nand_gap',pure_g6_gap,float(pure_g6_gap))
print('prime_gain_L',L,float(L))
print('lambda',LAMBDA,float(LAMBDA))
print('repair_increment',repair,float(repair))
print('repair_slack_over_coarse_upper',repair_slack,float(repair_slack))
print('center_increment',center_increment,float(center_increment))
print('replacement_center_cap',cap,float(cap))
print('quartic_center_improvement',QUARTIC_CENTER-cap,float(QUARTIC_CENTER-cap))
