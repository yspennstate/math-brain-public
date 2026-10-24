from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import permutations

# Frozen endpoint from NM13-11 2026-09-19T20-00-00Z.
B_PREV = Fraction(
    12234885369899315774910192590367613149468633559630832101342942986342507415367247043258638762394714330725215296855853141419683832042798882673372297,
    19443351973040638050987304673433346221975007518723198189172396736647229533566751930247359385542476562500000000000000000000000000000000000000000000,
)

# Larger deliberately asymmetric normalized four-point shape box:
# p1=(0,0), p2=(1,0), p3=(x,-r), p4=(z,-s).
xlo, xhi = Fraction(13,100), Fraction(49,100)
rlo, rhi = Fraction(29,25), Fraction(7,5)
zlo, zhi = Fraction(51,100), Fraction(81,100)
slo, shi = Fraction(33,50), Fraction(21,25)

# Strict topology separators.
D13_MIN = xlo*xlo + rlo*rlo
D13_MAX = xhi*xhi + rhi*rhi
D14_MAX = zhi*zhi + shi*shi
D24_MAX = (1-zlo)**2 + shi*shi

assert D13_MIN == Fraction(109,80)
assert D13_MAX == Fraction(22001,10000)
assert D14_MAX == Fraction(13617,10000)
assert D24_MAX == Fraction(9457,10000)

# d13 > 1 and d13 > d14 uniformly.
assert D13_MIN - 1 == Fraction(29,80)
assert D13_MIN - D14_MAX == Fraction(1,1250)

# x<1/2 => d23-d13=1-2x>0.
assert Fraction(1,2)-xhi == Fraction(1,100)

# z>1/2 => d14-d24=2z-1>0.
assert zlo-Fraction(1,2) == Fraction(1,100)

# d14-d34 = x(2z-x)+r(2s-r).
# On this box z>x, so x(2z-x) increases in x and z.
# Also r>s, so r(2s-r) increases in s and decreases in r.
D14_MINUS_D34_MIN = xlo*(2*zlo-xlo) + rhi*(2*slo-rhi)
assert D14_MINUS_D34_MIN == Fraction(37,10000)

# Redundant separator making p2's ordering transparent.
assert 1-D24_MAX == Fraction(543,10000)

# The target directed two-nearest-neighbor topology.
NEW_TOPOLOGY = ((1,3), (0,3), (0,3), (1,2))

def strongly_connected(topo):
    for start in range(4):
        seen={start}
        stack=[start]
        while stack:
            i=stack.pop()
            for j in topo[i]:
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
        if len(seen) != 4:
            return False
    return True

assert strongly_connected(NEW_TOPOLOGY)

# Compare up to relabeling with the two four-point sink topologies already charged.
CHAIN_TOPOLOGY = ((1,2), (0,2), (1,3), (1,2))
C4_TOPOLOGY = ((1,3), (0,2), (1,3), (0,2))

def canonical(topo):
    reps=[]
    for perm in permutations(range(4)):
        transformed=[None]*4
        for old in range(4):
            transformed[perm[old]] = tuple(sorted(perm[j] for j in topo[old]))
        reps.append(tuple(transformed))
    return min(reps)

CAN_NEW=canonical(NEW_TOPOLOGY)
CAN_CHAIN=canonical(CHAIN_TOPOLOGY)
CAN_C4=canonical(C4_TOPOLOGY)
assert CAN_NEW == ((1,2),(0,2),(0,3),(1,2))
assert CAN_CHAIN == ((1,2),(0,2),(0,3),(0,2))
assert CAN_C4 == ((1,2),(0,3),(0,3),(1,2))
assert len({CAN_NEW,CAN_CHAIN,CAN_C4}) == 3

# Positive normalized shape volume.
V=(xhi-xlo)*(rhi-rlo)*(zhi-zlo)*(shi-slo)
assert V == Fraction(729,156250)

# Common internal second-neighbor envelope.
U=Fraction(297,200)
assert U*U-D13_MAX == Fraction(41,8000)

# External guard and Hamiltonian-boundary surplus.
H=Fraction(37,20)
DELTA=H-U
assert DELTA == Fraction(73,200)

# All centers lie in K=[0,1]x[-7/5,0]. The union of radius-H disks
# is contained in K+B_H. Use pi<22/7.
PI_UP=Fraction(22,7)
Q=rhi + 2*H*(1+rhi) + PI_UP*H*H
assert Q == Fraction(29451,1400)
SQRTQ_UP=Fraction(1147,250)
assert SQRTQ_UP*SQRTQ_UP-Q == Fraction(11651,875000)

# pi^(3/2) > 3*(17/10)=51/10.
PI32_LOW=Fraction(51,10)

# Exact-binomial / Campbell-Mecke limiting correction:
# ordered quadruples /4!, at least two path-boundary crossings,
# L-side surcharge DELTA*s.
DELTA_NEW = (
    Fraction(5,64) * PI32_LOW * V * DELTA
    / (Q**3 * SQRTQ_UP)
)
assert DELTA_NEW == Fraction(34478703,2170350054230822)
assert DELTA_NEW > Fraction(3,200_000_000)  # > 1.5e-8

B_NEW=B_PREV+DELTA_NEW
assert B_NEW == Fraction(
    428290077362103688393910556289374260624427851669128955928061085239297514491295131572164454010069801964500982465126129692695841537835318496791550852459470618357,
    680627096921253366568966735604927531896699764460645393329189347179240150914086801287321056287307690561375724195312500000000000000000000000000000000000000000000,
)
assert B_NEW > Fraction(629258046,1_000_000_000)

getcontext().prec=90
def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print("P0257 widened missing-D2-topology exact checker")
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
print("SHAPE_VOLUME =", V, dec(V))
print("U2_SLACK =", U*U-D13_MAX)
print("DELTA =", DELTA)
print("Q =", Q, dec(Q))
print("SQRTQ_SQUARE_SLACK =", SQRTQ_UP*SQRTQ_UP-Q)
print("DELTA_NEW =", DELTA_NEW, dec(DELTA_NEW))
print("DELTA_NEW_GT_1.5E-8 =", DELTA_NEW > Fraction(3,200_000_000))
print("B_PREV_DECIMAL =", dec(B_PREV))
print("B_NEW =", B_NEW)
print("B_NEW_DECIMAL =", dec(B_NEW))
print("B_NEW_GT_0.629258046 =", B_NEW > Fraction(629258046,1_000_000_000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
