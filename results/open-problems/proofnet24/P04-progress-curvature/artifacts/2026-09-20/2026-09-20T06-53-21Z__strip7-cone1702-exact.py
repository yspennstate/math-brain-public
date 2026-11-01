from fractions import Fraction as F
from functools import lru_cache
from math import factorial

# P04 T10 exact certificate.
# New finite core: a 7-column, 3-row carry-lane block.
# Consumed theorem: PROB10-10 6-local-SAW endpoint count
# N_l(n;a,b) <= K r^l A^(-an) B^(-bn), certified in
# artifacts/prob10_2026-09-20/PROB10-10/20260920T0619Z__six_local_saw_cone_repro.py/.out.

KBLK=7
verts=[(x,r) for x in range(KBLK+1) for r in range(3)]
idx={v:i for i,v in enumerate(verts)}
out=[[] for _ in verts]
for x in range(KBLK):
    # Undirected vertical physical edges in departure columns only.
    for rr in (0,1):
        a,b=idx[(x,rr)],idx[(x,rr+1)]
        out[a].append(b); out[b].append(a)
    # This admissible policy uses horizontal physical edges only eastward.
    for rr in range(3):
        out[idx[(x,rr)]].append(idx[(x+1,rr)])
targets=[idx[(KBLK,rr)] for rr in range(3)]

def absorption(start_lane):
    states=0
    @lru_cache(None)
    def rec(mask):
        nonlocal states
        states += 1
        for j,t in enumerate(targets):
            if (mask>>t)&1:
                p=[F(0),F(0),F(0)]; p[j]=F(1)
                return F(0),tuple(p)
        rates={}; total=0
        mm=mask
        while mm:
            bit=mm & -mm
            i=bit.bit_length()-1
            mm-=bit
            for j in out[i]:
                if not ((mask>>j)&1):
                    rates[j]=rates.get(j,0)+1
                    total+=1
        assert total>0
        et=F(1,total)
        ps=[F(0),F(0),F(0)]
        for j,mult in rates.items():
            ej,pj=rec(mask | (1<<j))
            w=F(mult,total)
            et += w*ej
            for q0 in range(3):
                ps[q0] += w*pj[q0]
        return et,tuple(ps)
    return rec(1<<idx[(0,start_lane)]),states

((gO,pO),statesO)=absorption(0)
((gC,pC),statesC)=absorption(1)
assert sum(pO,F(0))==1 and sum(pC,F(0))==1
pOC=pO[1]
pCC=pC[1]
lam=pCC-pOC
assert 0 < lam < 1
assert gC < gO
piC=pOC/(pOC+1-pCC)
piO=1-piC
assert 0 < piC < 1
abar=(piC*gC+piO*gO)/KBLK

# Strict improvement over P04's preceding 6-column block.
a6=F(57444100690415803497507130042889304438078500562657949173917,
     94434081367035184054991164646261870153788595690449920000000)
assert abar < a6

# Consumed exact 6-local-SAW count constants.
A=F(1939,1000)
B=F(2795,1000)
r=F(623,125)
K=F(206537443078004097635789290261008243952922715998432755935730363815733,
    3106818744270872322688634630791015045264585436511053053952000000000)

# Lower-tail retuning.
s=F(398401,100000)       # 3.98401, just above r-1=3.984
nu=1+s
q=r/nu
assert q==F(498400,498401)
c=F(12101,20000)         # 0.60505 > abar
rho=F(851,500)           # 1.702
beta_hat=F(999,1000)     # 0.999
assert abar < c

# beta(rho)^500 = A^-500 B^-851 exp(500*s*c) q^1351.
# Exact upper bound on exp: split into 4096 pieces; degree-24 Taylor plus
# a geometric upper bound on the positive remainder in each piece.
x=F(500)*s*c
split=4096
y=x/F(split)
N=24
T=sum((y**j)/F(factorial(j)) for j in range(N+1))
first=y**(N+1)/F(factorial(N+1))
ratio=y/F(N+2)
assert ratio < 1
U=T + first/(1-ratio)
exp_x_upper=U**split
beta500_upper=(A**(-500))*(B**(-851))*exp_x_upper*(q**1351)
assert beta500_upper < beta_hat**500
assert beta_hat < 1

# Infinite-volume reflected strict-triangle defect.
delta=2*(c-abar)
assert delta > F(1,10000)  # > 1e-4

# Finite transfer error. If m=an is divisible by 7, 2m is a multiple of 7,
# so the 7-column axis block applies exactly to the reflected endpoint pair.
# At this q, Cnew=K/(1-q)=498401 K.
Cnew=K/(1-q)
mfinite=35000
assert mfinite%7==0
finite_error=2*c*Cnew*(beta_hat**mfinite) + piO/F(mfinite)
finite_margin=delta-finite_error
assert finite_margin > F(1,100000)  # > 1e-5

print('P04 T10 exact strip-7 carry-lane / cone-1.702 certificate')
print('ALL_EXACT_CHECKS_PASS = True')
print('block_width =',KBLK)
print('block_states_outer =',statesO)
print('block_states_center =',statesC)
print('gO =',gO)
print('gO_float =',float(gO))
print('gC =',gC)
print('gC_float =',float(gC))
print('pOC =',pOC)
print('pOC_float =',float(pOC))
print('pCC =',pCC)
print('pCC_float =',float(pCC))
print('lambda =',lam)
print('lambda_float =',float(lam))
print('piC =',piC)
print('piC_float =',float(piC))
print('piO =',piO)
print('piO_float =',float(piO))
print('axis_policy_bound =',abar)
print('axis_policy_bound_float =',float(abar))
print('previous_a6_float =',float(a6))
print('axis_improvement_float =',float(a6-abar))
print('A =',A,'B =',B,'r =',r)
print('K =',K)
print('s =',s,'q =',q)
print('c =',c,'rho =',rho,'beta_hat =',beta_hat)
print('beta500_upper_float =',float(beta500_upper))
print('beta_hat_500_float =',float(beta_hat**500))
print('Cnew =',Cnew)
print('Cnew_float =',float(Cnew))
print('delta =',delta)
print('delta_float =',float(delta))
print('finite_m =',mfinite)
print('finite_error_num_bits =',finite_error.numerator.bit_length(),'den_bits =',finite_error.denominator.bit_length())
print('finite_error_float =',float(finite_error))
print('finite_margin_num_bits =',finite_margin.numerator.bit_length(),'den_bits =',finite_margin.denominator.bit_length())
print('finite_margin_float =',float(finite_margin))
