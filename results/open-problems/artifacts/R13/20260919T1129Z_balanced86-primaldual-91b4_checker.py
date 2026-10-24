from fractions import Fraction as F
from collections import Counter
from decimal import Decimal, getcontext

# R13 exact checker: sharpen the 86-leaf balanced-tree Komlos obstruction and
# certify an almost matching dual ceiling for this fixed support mechanism.
# All acceptance tests are exact integer/Fraction arithmetic.

N=86
Q_LO=F(225925611947,100000000000)
Q_HI=F(225925612084,100000000000)
Q_PREV=F(2259253,1000000)
ORBIT_WEIGHTS=[
((0,1),4857310000),
((2,44),3434636839),
((3,45),2440008214),
((4,46),1735452915),
((5,9,47,51),1227150525),
((6,10,48,52),876677743),
((7,11,49,53),858681865),
((8,12,50,54),598368377),
((13,55),1715180242),
((14,56),1222221961),
((15,57),873156772),
((16,58),855233170),
((17,59),595965170),
((18,60),1203335672),
((19,21,61,63),850886814),
((20,22,62,64),592936433),
((23,65),2417248464),
((24,34,66,76),1709252781),
((25,35,67,77),1217998106),
((26,36,68,78),870139244),
((27,37,69,79),852277584),
((28,38,70,80),593905585),
((29,39,71,81),1199177086),
((30,32,40,42,72,74,82,84),847946249),
((31,33,41,43,73,75,83,85),590887314),
]
W=[None]*N
for orbit,val in ORBIT_WEIGHTS:
    for j in orbit:
        assert W[j] is None
        W[j]=val
assert all(x is not None and x>0 for x in W)

rows=[]
next_col=1

def build(size,path):
    global next_col
    if size==1:
        rows.append([(0,+1)]+path)
        return
    a=size//2
    c=next_col
    next_col+=1
    build(a,path+[(c,+1)])
    build(size-a,path+[(c,-1)])

build(N,[])
assert len(rows)==N and next_col==N
depths=Counter(len(r)-1 for r in rows)
assert depths==Counter({6:42,7:44})

# Exact projective partition.
for i in range(N):
    ri=dict(rows[i])
    for k in range(i+1,N):
        rk=dict(rows[k])
        common=set(ri).intersection(rk)
        assert any(j!=0 and ri[j]==-rk[j] for j in common)
kraft=sum((F(1,2**(len(r)-1)) for r in rows),F(0))
assert kraft==1

# Unit-row-mass primal certificate alpha_{ij} proportional to 1/W_j.
unit_load=[F(0) for _ in range(N)]
for row in rows:
    den=sum((F(1,W[j]) for j,_ in row),F(0))
    s=F(0)
    for j,_ in row:
        a=F(1,W[j])/den
        s+=a
        unit_load[j]+=a*a
    assert s==1
L_PR=max(unit_load)
max_cols=[j for j,x in enumerate(unit_load) if x==L_PR]
assert Q_LO*Q_LO*L_PR < 1
assert Q_LO > Q_PREV

# Dual certificate for the fixed support minimax problem:
# mu_j=W_j/sum_k W_k. For each row S,
# min_{alpha>=0,sum alpha=1} sum_{j in S} mu_j alpha_j^2
# = 1/sum_{j in S}(1/mu_j).
SW=sum(W)
mu=[F(w,SW) for w in W]
D_DUAL=F(0)
for row in rows:
    invsum=sum((1/mu[j] for j,_ in row),F(0))
    D_DUAL += 1/invsum
assert D_DUAL <= L_PR
weighted=sum((mu[j]*unit_load[j] for j in range(N)),F(0))
assert weighted==D_DUAL
assert D_DUAL > 1/(Q_HI*Q_HI)
assert Q_LO < Q_HI

getcontext().prec=70
def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print('R13_BALANCED86_PRIMAL_DUAL_EXACT_PASS')
print('n_rows =',N)
print('n_columns =',N)
print('depth_distribution =',dict(sorted(depths.items())))
print('kraft_sum =',kraft)
print('q_previous =',dec(Q_PREV))
print('q_lower_exact =',f'{Q_LO.numerator}/{Q_LO.denominator}')
print('q_lower_decimal =',dec(Q_LO))
print('q_lower_minus_previous =',dec(Q_LO-Q_PREV))
print('q_upper_fixed_support_exact =',f'{Q_HI.numerator}/{Q_HI.denominator}')
print('q_upper_fixed_support_decimal =',dec(Q_HI))
print('fixed_support_q_gap =',dec(Q_HI-Q_LO))
print('primal_unit_max_load =',dec(L_PR))
print('primal_max_columns =',max_cols)
print('primal_scaled_max_load_at_q_lower =',dec(Q_LO*Q_LO*L_PR))
print('primal_scaled_slack =',dec(1-Q_LO*Q_LO*L_PR))
print('dual_load_lower =',dec(D_DUAL))
print('dual_minus_1_over_qhi_sq =',dec(D_DUAL-1/(Q_HI*Q_HI)))
print('primal_dual_load_gap =',dec(L_PR-D_DUAL))
print('orbit_count =',len(ORBIT_WEIGHTS))
print('orbit_weights =',ORBIT_WEIGHTS)
