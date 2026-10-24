#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb

EPS = F(113, 5000)
LAMBDA = F(3469, 200000)
COARSE_DEFICIENCY_UPPER = F(17611420, 10**9)
CDAG = F(6521851214, 10**9)

# R(X,T,U) in the exact factorization
# F_scalar = d*t*(1-t)*(2-d)*R(d/2,t,u),
# c = -1+t*d+u*(2-d), eps=113/5000.
POWER = {
    (4, 4, 0): F(-226,625),
    (4, 3, 1): F(1356,625),
    (4, 3, 0): F(-226,625),
    (4, 2, 2): F(-678,125),
    (4, 2, 1): F(1356,625),
    (4, 2, 0): F(-226,625),
    (4, 1, 3): F(904,125),
    (4, 1, 2): F(-678,125),
    (4, 1, 1): F(1356,625),
    (4, 1, 0): F(-226,625),
    (4, 0, 4): F(-678,125),
    (4, 0, 3): F(904,125),
    (4, 0, 2): F(-678,125),
    (4, 0, 1): F(1356,625),
    (4, 0, 0): F(-226,625),
    (3, 4, 0): F(-226,625),
    (3, 3, 0): F(452,625),
    (3, 2, 2): F(678,125),
    (3, 2, 1): F(-678,125),
    (3, 2, 0): F(452,625),
    (3, 1, 3): F(-1808,125),
    (3, 1, 2): F(2034,125),
    (3, 1, 1): F(-678,125),
    (3, 1, 0): F(452,625),
    (3, 0, 4): F(2034,125),
    (3, 0, 3): F(-3164,125),
    (3, 0, 2): F(2034,125),
    (3, 0, 1): F(-678,125),
    (3, 0, 0): F(452,625),
    (2, 4, 0): F(-226,625),
    (2, 3, 0): F(452,625),
    (2, 2, 0): F(2274,625),
    (2, 1, 3): F(904,125),
    (2, 1, 2): F(-1356,125),
    (2, 1, 1): F(-7288,625),
    (2, 1, 0): F(2274,625),
    (2, 0, 4): F(-2034,125),
    (2, 0, 3): F(3616,125),
    (2, 0, 2): F(4152,625),
    (2, 0, 1): F(-7288,625),
    (2, 0, 0): F(2274,625),
    (1, 4, 0): F(-226,625),
    (1, 3, 0): F(452,625),
    (1, 2, 0): F(2274,625),
    (1, 1, 0): F(-4,1),
    (1, 0, 4): F(678,125),
    (1, 0, 3): F(-1356,125),
    (1, 0, 2): F(-10932,625),
    (1, 0, 1): F(14322,625),
    (1, 0, 0): F(-4,1),
    (0, 4, 0): F(-226,625),
    (0, 3, 0): F(452,625),
    (0, 2, 0): F(2274,625),
    (0, 1, 0): F(-4,1),
    (0, 0, 0): F(2,1),
}

def power_to_bernstein(power):
    n = 4
    B = [[[F(0) for _ in range(5)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                z = F(0)
                for a in range(i+1):
                    for b in range(j+1):
                        for c in range(k+1):
                            A = power.get((a,b,c), F(0))
                            if A:
                                z += A * F(comb(i,a), comb(n,a)) * F(comb(j,b), comb(n,b)) * F(comb(k,c), comb(n,c))
                B[i][j][k] = z
    return B

def split_curve(vals):
    levels = [list(vals)]
    while len(levels[-1]) > 1:
        p = levels[-1]
        levels.append([(p[i]+p[i+1])/2 for i in range(len(p)-1)])
    left = [levels[i][0] for i in range(len(levels))]
    right = [levels[-1-i][i] for i in range(len(levels))]
    return left, right

def split_axis(B, axis):
    def blank():
        return [[[F(0) for _ in range(5)] for _ in range(5)] for _ in range(5)]
    L, R = blank(), blank()
    if axis == 0:
        for j in range(5):
            for k in range(5):
                l,r = split_curve([B[i][j][k] for i in range(5)])
                for i in range(5): L[i][j][k],R[i][j][k]=l[i],r[i]
    elif axis == 1:
        for i in range(5):
            for k in range(5):
                l,r = split_curve([B[i][j][k] for j in range(5)])
                for j in range(5): L[i][j][k],R[i][j][k]=l[j],r[j]
    else:
        for i in range(5):
            for j in range(5):
                l,r = split_curve([B[i][j][k] for k in range(5)])
                for k in range(5): L[i][j][k],R[i][j][k]=l[k],r[k]
    return L,R

def octants(B):
    parts=[B]
    for axis in range(3):
        nxt=[]
        for P in parts:
            nxt.extend(split_axis(P,axis))
        parts=nxt
    return parts

def flat(B):
    for plane in B:
        for row in plane:
            yield from row

def certify(B, maxdepth=6):
    stack=[(B,0)]
    leaves=0
    nodes=0
    max_seen=0
    min_terminal=None
    unresolved=[]
    while stack:
        Q, depth=stack.pop()
        nodes += 1
        vals=list(flat(Q))
        m=min(vals)
        if m >= 0:
            leaves += 1
            max_seen=max(max_seen, depth)
            min_terminal=m if min_terminal is None else min(min_terminal,m)
        elif depth >= maxdepth:
            unresolved.append((depth,m))
        else:
            for child in octants(Q):
                stack.append((child,depth+1))
    return leaves,nodes,max_seen,min_terminal,unresolved

def psi_mean(m):
    return 1 - m**4 - EPS*(1-m*m)**3

B0=power_to_bernstein(POWER)
leaves,nodes,maxdepth,mincoef,unresolved=certify(B0,6)
assert not unresolved
assert leaves == 134
assert nodes == 153
assert maxdepth == 6
assert mincoef == F(73043599037,16492674416640000)
assert 0 < EPS < 1

m38 = F(1,4)
mout = F(57,1024)
L = F(57,256)*psi_mean(m38) + F(465,256)*psi_mean(F(0)) - psi_mean(mout)
assert L == F(5853358700981395212159,5764607523034234880000)
repair = LAMBDA * L
assert repair > COARSE_DEFICIENCY_UPPER
repair_slack = repair - COARSE_DEFICIENCY_UPPER
center_increment = LAMBDA * psi_mean(F(0))
assert center_increment == F(16953003,10**9)
cap = CDAG + center_increment
assert cap == F(6538804217,10**9)

print("epsilon", EPS, float(EPS))
print("bernstein_terminal_boxes", leaves)
print("bernstein_nodes", nodes)
print("bernstein_max_depth", maxdepth)
print("bernstein_min_terminal_coefficient", mincoef, float(mincoef))
print("prime_gain_L", L, float(L))
print("lambda", LAMBDA, float(LAMBDA))
print("repair_increment", repair, float(repair))
print("coarse_deficiency_upper", COARSE_DEFICIENCY_UPPER, float(COARSE_DEFICIENCY_UPPER))
print("repair_slack_over_coarse_upper", repair_slack, float(repair_slack))
print("center_increment", center_increment, float(center_increment))
print("replacement_center_cap", cap, float(cap))
print("previous_quartic_center_cap", 6.538814964)
print("center_improvement", 6.538814964-float(cap))
print("PASS")
