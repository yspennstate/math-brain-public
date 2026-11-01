#!/usr/bin/env python3
from fractions import Fraction as F
import itertools

# Certified whole-box data inherited from NM13-03 alpha=12.319635
Aq=[[F(-7294853,100000),F(-504965,10000000)],
    [F(-3028867,1000),F(-3758826,1000000)]]
dr=[F(1,10_000_000),F(1,250_000)]
ranges=[(F(-34,1000),F(-28,1000)),
        (F(32,100000),F(51,100000)),
        (F(246,10),F(254,10)),
        (F(-603,1000),F(-600,1000))]

def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def qvertex(hp,hb,ap,ab):
    AJ=mm(Aq,[[hp,hb],[ap,ab]])
    M=[[F(int(i==j))-AJ[i][j] for j in range(2)] for i in range(2)]
    return max(sum(abs(F(1,dr[i])*M[i][j]*dr[j]) for j in range(2)) for i in range(2))

Q=max(qvertex(*v) for v in itertools.product(*ranges))
assert Q == F(70497781,125000000)

# Uniform contraction for every target alpha in [12.31963485,12.319635].
# Old center has |H|<4.7e-12 and |A-12.319635|<3.7e-11.
# New target shift is 1.5e-7, so EA=1.501e-7 is a safe exact ceiling.
EH=F(47,10**13)
EA=F(1501,10**10)
ETA=max(F(1,dr[i])*(abs(Aq[i][0])*EH+abs(Aq[i][1])*EA) for i in range(2))
RHO=ETA/(1-Q)
assert ETA == F(231374183,1600000000)
assert ETA < 1-Q
assert RHO == F(1156870915,3488142016)
assert RHO < 1

# Elementary exact Gaussian second-moment envelope.
# pi < 22/7 and (627/250)^2 > 44/7 imply phi(0)>250/627.
assert F(627,250)**2 > F(44,7)
phi0_lb=F(250,627)

# For 0<=u<=1/2, alternating Taylor gives
# e^{-u} >= 1-u+u^2/2-u^3/6.
# Integrating with u=x^2/2 on x in [0,1] gives A>=479/560.
Aint_lb=F(479,560)
assert Aint_lb == F(1)-F(1,6)+F(1,40)-F(1,336)

# Q(1)=1/2-phi(0)*int_0^1 exp(-x^2/2)dx.
Q1_ub=F(1,2)-phi0_lb*Aint_lb
assert Q1_ub == F(5581,35112)
assert Q1_ub < F(4,25)

# e^{1/2}<33/20: 1+1/2+1/8 plus n>=3 tail,
# whose term ratio is <=1/8, so tail <=(1/48)/(1-1/8)=1/42.
assert F(1)+F(1,2)+F(1,8)+F(1,42) < F(33,20)
# Hence e^{-1/2}>20/33 and phi(1)>5000/20691>6/25.
phi1_lb=phi0_lb*F(20,33)
assert phi1_lb == F(5000,20691)
assert phi1_lb > F(6,25)

# m2 = E[(G-1)_+^2] = 2 Q(1)-phi(1) < 2/25.
m2_ub=F(2,25)

# Whole stationary box has B<6.19766 and c>3.71965.
B_ub=F(619766,100000)
c_lb=F(371965,100000)
assert 3*B_ub < 5*c_lb   # B/c < 5/3
slope_ub=F(5,3)*m2_ub
assert slope_ub == F(2,15)

# Certified true-root objective at alpha0=12.319635.
psi_anchor_lb=F(23584189005311,1090044380000000000000)
delta=F(3,20_000_000)  # 1.5e-7
psi_new_lb=psi_anchor_lb-slope_ub*delta
assert slope_ub*delta == F(1,50_000_000)
assert psi_new_lb == F(1783301405311,1090044380000000000000)
assert psi_new_lb > 0

alpha0=F(12319635,1000000)
alpha1=F(246392697,20000000) # 12.31963485
assert alpha0-alpha1 == delta
alphaL=F(315148718753,50000000000) # 6.30297437506
width0=alpha0-alphaL
width1=alpha1-alphaL
assert width0-width1 == delta

print("Q_EXACT", Q, float(Q))
print("ETA_UNIFORM_EXACT", ETA, float(ETA))
print("RHO_UNIFORM_EXACT", RHO, float(RHO))
print("GAUSS_Q1_UPPER", Q1_ub, float(Q1_ub))
print("GAUSS_PHI1_LOWER", phi1_lb, float(phi1_lb))
print("M2_UPPER", m2_ub, float(m2_ub))
print("ENVELOPE_SLOPE_UPPER", slope_ub, float(slope_ub))
print("ALPHA_BEFORE", float(alpha0))
print("ALPHA_AFTER", float(alpha1))
print("DELTA", delta, float(delta))
print("PSI_ANCHOR_LOWER", psi_anchor_lb, float(psi_anchor_lb))
print("PSI_NEW_LOWER", psi_new_lb, float(psi_new_lb))
print("WIDTH_BEFORE", float(width0))
print("WIDTH_AFTER", float(width1))
print("ALL_EXACT_MICROCONTINUATION_CHECKS_PASS")
