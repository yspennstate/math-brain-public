#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter
from math import comb
from fractions import Fraction

# R15 / I0124 exact certificate for H_288 >= 112.
# Everything below is integer/rational arithmetic.

# --- Global hyperplane-incidence moments for a hypothetical 288-cap in AG(7,3).
N_DIR = (3**7 - 1)//2                    # 1093 hyperplane directions
N_HYP = 3*N_DIR                          # 3279 affine hyperplanes
n = 288
S1 = n*N_DIR
Sbin2 = comb(n,2)*((3**6 - 1)//2)
Sbin3 = comb(n,3)*((3**5 - 1)//2)
S2 = 2*Sbin2 + S1
S3 = 6*Sbin3 + 6*Sbin2 + S1
D2 = S2 - 2*96*S1 + 96**2*N_HYP
D3 = S3 - 3*96*S2 + 3*96**2*S1 - 96**3*N_HYP
assert (S1,Sbin2,Sbin3,S2,S3,D2,D3) == (
    314784,15043392,476732256,30401568,2950968672,182304,-2584224
)

# --- Under the hypothesis "no 112-slice", Prop. 4.1(b) excludes (66,111,111);
# hence every direction type has 67 <= a <= b <= c <= 111, a+b+c=288.
types=[]
for a in range(67,112):
    for b in range(a,112):
        c=288-a-b
        if b <= c <= 111:
            x,y,z=a-96,b-96,c-96
            q2=x*x+y*y+z*z
            q3=x*x*x+y*y*y+z*z*z
            v4=comb(a,4)+comb(b,4)+comb(c,4)
            t111=(a==111)+(b==111)+(c==111)
            types.append((a,b,c,q2,q3,v4,t111))
assert len(types)==191

# Lemma A: every admissible direction satisfies
#   602*1_{a,b,c contains 111} + 14*q2 + q3 >= 0.
# Summing gives t_111 >= ceil(31968/602)=54.
gaps_A=[]
for a,b,c,q2,q3,v4,t111 in types:
    gap=602*t111 + 14*q2 + q3
    assert gap >= 0
    gaps_A.append((gap,(a,b,c)))
eqA=[t for g,t in gaps_A if g==0]
assert eqA == [(67,110,111),(68,110,110),(96,96,96)]
num = -(14*D2 + D3)
assert num==31968
t111_lower=(num+601)//602
assert t111_lower==54

# Lemma B: exact rational supporting-plane inequality for the fourth moment.
#   v4 <= 9,965,880 + (3,032,159/1,350) q2 + (903,493/60,750) q3.
alpha=Fraction(9965880,1)
beta=Fraction(3032159,1350)
gamma=Fraction(903493,60750)
gaps_B=[]
for a,b,c,q2,q3,v4,t111 in types:
    gap=alpha + beta*q2 + gamma*q3 - v4
    assert gap >= 0
    gaps_B.append((gap,(a,b,c)))
eqB=[t for g,t in gaps_B if g==0]
assert eqB == [(67,110,111),(88,89,111),(96,96,96)]
S4_upper=alpha*N_DIR + beta*D2 + gamma*D3
q_upper=(S4_upper - 40*comb(288,4))/81
assert q_upper == Fraction(13094476424,30375)
q_upper_int=q_upper.numerator//q_upper.denominator
assert q_upper_int==431093

# --- An explicit doubled-Hill representative H in AG(6,3).
# Blocks are a 2-(6,3,2) design. D consists of weight-3 vectors supported on them,
# and R consists of full-support {1,2}-vectors with an even number of 2s.
BLOCKS=[
    (0,1,2),(0,1,3),(0,2,4),(0,3,5),(0,4,5),
    (1,2,5),(1,3,4),(1,4,5),(2,3,4),(2,3,5),
]
pair_mult=Counter()
for B in BLOCKS:
    for p in combinations(B,2):
        pair_mult[p]+=1
assert len(pair_mult)==15 and set(pair_mult.values())=={2}

H=set()
for B in BLOCKS:
    for vals in product((1,2), repeat=3):
        x=[0]*6
        for i,v in zip(B,vals):
            x[i]=v
        H.add(tuple(x))
for vals in product((1,2), repeat=6):
    if sum(v==2 for v in vals)%2==0:
        H.add(tuple(vals))
assert len(H)==112

def midpoint(x,y):
    # In characteristic 3, midpoint m solves x+y=2m=-m.
    return tuple((-(a+b))%3 for a,b in zip(x,y))

Hlist=sorted(H)
rH=Counter()
for i,x in enumerate(Hlist):
    for y in Hlist[i+1:]:
        m=midpoint(x,y)
        # This simultaneously certifies that H is a cap.
        assert m not in H
        rH[m]+=1
assert sum(rH.values())==comb(112,2)
assert len(rH)==3**6-112
dist=Counter(rH.values())
assert dist==Counter({10:616,56:1})
anchors=[m for m,v in rH.items() if v==56]
assert anchors==[(0,0,0,0,0,0)]

# Therefore every affine-isomorphic 112-cap has exactly one center with 56
# antipodal cap pairs and every other external point has exactly 10 secants.
# In particular, deleting one cap point leaves exactly 55 complete antipodal
# pairs about the unique center.

# --- Planar-four-set count q(A).
# For a 288-cap A in AG(7,3), all C(288,2) pairs have midpoint outside A.
# If k distinct complement points each have r_m >= 55, convexity gives the
# following exact minimum of q=sum_m C(r_m,2).
def qmin_with_k_anchors(k):
    total=comb(288,2)-55*k
    bins=(3**7-288)-k
    lo,rem=divmod(total,bins)
    return k*comb(55,2)+(bins-rem)*comb(lo,2)+rem*comb(lo+1,2),lo,rem

q4,lo4,rem4=qmin_with_k_anchors(4)
assert (q4,lo4,rem4)==(431463,21,1313)
assert q4 > q_upper_int
# So at most three distinct anchors can occur among 111-slices.

# --- A fixed anchor can support at most 15 distinct 111-slices.
# Its antipodal-pair directions form a projective cap S in PG(6,3), so |S|<=136.
# Each 111-slice through that anchor contributes a block of 55 points in S.
# Two such blocks meet in a PG(4,3) cap, hence in at most 20 points.
# Cauchy then gives:
#   ((55 t)^2/136 - 55 t)/2 <= 20*C(t,2).
# Check exactly that t=16 already violates it.
def lower_pair_intersections(t):
    return (Fraction((55*t)**2,136)-55*t)/2
def upper_pair_intersections(t):
    return 20*comb(t,2)
assert lower_pair_intersections(15) <= upper_pair_intersections(15)
assert lower_pair_intersections(16) > upper_pair_intersections(16)
# Algebraically t <= 952/61 < 16.
assert Fraction(952,61) < 16

# Combining: at least 54 distinct 111-hyperplanes, at most 3 anchors,
# and at most 15 such hyperplanes per anchor would give t<=45, contradiction.
assert t111_lower > 3*15

print("PASS R15 I0124 exact H_288>=112 certificate")
print(f"N_DIR={N_DIR}; admissible_no112_direction_types={len(types)}")
print(f"D2={D2}; D3={D3}")
print(f"direction_111_lower={t111_lower}; lemmaA_equalities={eqA}")
print(f"q_upper={q_upper} < {q_upper_int+1}; integer_q_upper={q_upper_int}")
print(f"lemmaB_equalities={eqB}")
print(f"doubled_Hill_size={len(H)}; external_secant_distribution={dict(sorted(dist.items()))}")
print(f"four_anchor_q_min={q4} > q_upper_int={q_upper_int}")
print("projective literature inputs used by the proof: m_2(PG(4,3))=20; m_2(PG(6,3))<=136")
print("fixed_anchor_111_slices<=15; total_111_slices>=54; 3*15=45")
print("CONCLUSION: assuming no 112-slice is impossible; H_288 >= 112")
