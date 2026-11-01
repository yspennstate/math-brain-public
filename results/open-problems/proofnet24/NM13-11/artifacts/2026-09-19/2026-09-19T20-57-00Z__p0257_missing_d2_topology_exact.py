from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import permutations

# Frozen endpoint from NM13-11 2026-09-19T20-00-00Z.
B_PREV = Fraction(
    12234885369899315774910192590367613149468633559630832101342942986342507415367247043258638762394714330725215296855853141419683832042798882673372297,
    19443351973040638050987304673433346221975007518723198189172396736647229533566751930247359385542476562500000000000000000000000000000000000000000000,
)

# Deliberately asymmetric normalized four-point shape box.
xlo, xhi = Fraction(11, 25), Fraction(49, 100)
ylo, yhi = Fraction(-51, 50), Fraction(-47, 50)
zlo, zhi = Fraction(9, 10), Fraction(49, 50)
wlo, whi = Fraction(-8, 25), Fraction(-11, 50)

# Five strict inequalities suffice for the target nearest-two sets.
# d13 > 1
D13_MIN = xlo*xlo + yhi*yhi
assert D13_MIN == Fraction(2693, 2500)
assert D13_MIN - 1 == Fraction(193, 2500)

# d13 > d14
D14_MAX = zhi*zhi + wlo*wlo
assert D14_MAX == Fraction(2657, 2500)
assert D13_MIN - D14_MAX == Fraction(9, 625)

# x < 1/2 implies d23-d13 = 1-2x > 0.
assert Fraction(1, 2) - xhi == Fraction(1, 100)

# z > 1/2 implies d14-d24 = 2z-1 > 0.
assert zlo - Fraction(1, 2) == Fraction(2, 5)

# d14-d34 = x(2z-x) + r(2s-r), r=-y, s=-w.
# On the box, the first term is increasing in x,z and the second
# is increasing in s and decreasing in r, so its minimum is the endpoint below.
rhi = -ylo
slo = -whi
D14_MINUS_D34_MIN = xlo*(2*zlo-xlo) + rhi*(2*slo-rhi)
assert D14_MINUS_D34_MIN == Fraction(17, 2500)

# Useful redundant check: d24 < 1 uniformly.
D24_MAX = (1-zlo)**2 + wlo*wlo
assert D24_MAX == Fraction(281, 2500)
assert D24_MAX < 1

# Therefore the directed two-nearest-neighbor topology is:
NEW_TOPOLOGY = ((1,3), (0,3), (0,3), (1,2))

def strongly_connected(topo):
    for start in range(4):
        seen = {start}
        stack = [start]
        while stack:
            i = stack.pop()
            for j in topo[i]:
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
        if len(seen) != 4:
            return False
    return True

assert strongly_connected(NEW_TOPOLOGY)

# Compare up to relabeling against the two four-point sink topologies already charged.
CHAIN_TOPOLOGY = ((1,2), (0,2), (1,3), (1,2))
C4_TOPOLOGY = ((1,3), (0,2), (1,3), (0,2))

def canonical(topo):
    reps = []
    for perm in permutations(range(4)):
        # perm maps old labels to new labels.
        transformed = [None]*4
        for old in range(4):
            new = perm[old]
            transformed[new] = tuple(sorted(perm[j] for j in topo[old]))
        reps.append(tuple(transformed))
    return min(reps)

CAN_NEW = canonical(NEW_TOPOLOGY)
CAN_CHAIN = canonical(CHAIN_TOPOLOGY)
CAN_C4 = canonical(C4_TOPOLOGY)
assert CAN_NEW == ((1,2),(0,2),(0,3),(1,2))
assert CAN_CHAIN == ((1,2),(0,2),(0,3),(0,2))
assert CAN_C4 == ((1,2),(0,3),(0,3),(1,2))
assert len({CAN_NEW, CAN_CHAIN, CAN_C4}) == 3

# Shape volume.
V = (xhi-xlo)*(yhi-ylo)*(zhi-zlo)*(whi-wlo)
assert V == Fraction(1, 31250)

# Common internal second-neighbor upper bound.
D13_MAX = xhi*xhi + ylo*ylo
assert D13_MAX == Fraction(2561, 2000)
U = Fraction(1133, 1000)
assert U*U - D13_MAX == Fraction(3189, 1000000)

# External guard and Hamiltonian-boundary surplus.
H = Fraction(71, 50)
DELTA = H-U
assert DELTA == Fraction(287, 1000)

# Every guard disk is contained in K+B_H for
# K=[0,1] x [-51/50,0].  Use pi < 22/7.
PI_UP = Fraction(22, 7)
Q = Fraction(51,50) + 2*H*(1+Fraction(51,50)) + PI_UP*H*H
assert Q == Fraction(114573, 8750)
SQRTQ_UP = Fraction(181, 50)
assert SQRTQ_UP*SQRTQ_UP-Q == Fraction(181,17500)

# pi^(3/2) > 3*(17/10)=51/10.
PI32_LOW = Fraction(51,10)

# Ordered-quadruple / 4! count, two boundary crossings, and exact-binomial limit:
# Delta = (5*pi^(3/2)/64)*V*DELTA*Q^(-7/2).
DELTA_NEW = (
    Fraction(5,64) * PI32_LOW * V * DELTA
    / (Q**3 * SQRTQ_UP)
)
assert DELTA_NEW == Fraction(5229678125, 11614864414623725952)
assert DELTA_NEW > Fraction(9, 20_000_000_000)  # > 4.5e-10

B_NEW = B_PREV + DELTA_NEW
assert B_NEW == Fraction(
    123356367015213956225686430026816569999285347105205235789578226669285816019430347216281660892370824447499831507700145671720464225112188018230742982325281596351347,
    196034632754057046435523101493295438699574759207853713757387582971006827454688604181581860284589920954378396792867187500000000000000000000000000000000000000000000,
)
assert B_NEW > Fraction(629258031, 1_000_000_000)

getcontext().prec = 90
def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print("P0257 missing-D2-topology exact checker")
print("D13_GT_1_SLACK =", D13_MIN-1)
print("D13_GT_D14_SLACK =", D13_MIN-D14_MAX)
print("X_HALF_SLACK =", Fraction(1,2)-xhi)
print("Z_HALF_SLACK =", zlo-Fraction(1,2))
print("D14_GT_D34_SLACK =", D14_MINUS_D34_MIN)
print("D24_LT_1_SLACK =", 1-D24_MAX)
print("CAN_NEW =", CAN_NEW)
print("CAN_CHAIN =", CAN_CHAIN)
print("CAN_C4 =", CAN_C4)
print("TOPOLOGY_CLASSES_DISTINCT =", len({CAN_NEW,CAN_CHAIN,CAN_C4}) == 3)
print("SHAPE_VOLUME =", V)
print("U2_SLACK =", U*U-D13_MAX)
print("DELTA =", DELTA)
print("Q =", Q, dec(Q))
print("SQRTQ_SQUARE_SLACK =", SQRTQ_UP*SQRTQ_UP-Q)
print("DELTA_NEW =", DELTA_NEW, dec(DELTA_NEW))
print("DELTA_NEW_GT_4.5E-10 =", DELTA_NEW > Fraction(9,20_000_000_000))
print("B_PREV_DECIMAL =", dec(B_PREV))
print("B_NEW =", B_NEW)
print("B_NEW_DECIMAL =", dec(B_NEW))
print("B_NEW_GT_0.629258031 =", B_NEW > Fraction(629258031,1_000_000_000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
