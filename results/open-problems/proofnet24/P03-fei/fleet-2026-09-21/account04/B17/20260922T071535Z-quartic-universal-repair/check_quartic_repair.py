#!/usr/bin/env python3
from fractions import Fraction as F

def v(u):
    return u*(1-u)

def eta(u):
    x=v(u)
    return x*(1-2*x)

def gate_increment(bits, ps):
    """Exact additive all-gate defect increment for eta."""
    n=len(ps)
    r=F(0)
    for idx in range(1<<n):
        pr=F(1)
        for j,pj in enumerate(ps):
            pr*=pj if ((idx>>j)&1) else (1-pj)
        r+=pr*bits[idx]
    total=-eta(r)
    for i,pi in enumerate(ps):
        alpha=F(0)
        for idx in range(1<<n):
            if (idx>>i)&1:
                continue
            pr=F(1)
            for j,pj in enumerate(ps):
                if j==i:
                    continue
                pr*=pj if ((idx>>j)&1) else (1-pj)
            if bits[idx] != bits[idx | (1<<i)]:
                alpha+=pr
        total += alpha*eta(pi)
    return total

# eta(p)=(1-(1-2p)^4)/8 exactly on rational p.
for den in (8,16):
    for num in range(den+1):
        p=F(num,den)
        assert eta(p)==(1-(1-2*p)**4)/8

# Scalar induction certificate for the continuum theorem.
# R(d)>0 is the negative discriminant certificate for the endpoint quadratic P(d,t).
def R(d):
    return 3*d**4+4*d**3+12*d**2-32*d+16
def Rp(d):
    return 12*d**3+12*d**2+24*d-32
lo=F(39,50)
hi=F(4,5)
assert Rp(lo)==F(-8893,31250)
assert Rp(hi)==F(128,125)
Rlower=3*lo**4+4*lo**3+12*lo**2-32*hi+16
assert Rlower==F(4434123,6250000)
assert Rlower>0

# Exact universal stress: every 3-bit Boolean gate on the 3^3 grid
# p_i in {1/4,1/2,3/4}.
vals=(F(1,4),F(1,2),F(3,4))
cases=0
min_inc=None
argmin=None
for mask in range(1<<8):
    bits=tuple((mask>>idx)&1 for idx in range(8))
    for p0 in vals:
        for p1 in vals:
            for p2 in vals:
                inc=gate_increment(bits,(p0,p1,p2))
                cases+=1
                assert inc>=0
                if min_inc is None or inc<min_inc:
                    min_inc=inc
                    argmin=(mask,p0,p1,p2)

# Exact affine gain on the source-certified 18-input composition-prime witness.
x=F(3,8)
m=F(1,2)
z=F(967,2048)
L=F(57,256)*eta(x)+F(465,256)*eta(m)-eta(z)
expected_L=F(1141515555425,8796093022208)
assert L==expected_L
assert eta(m)==F(1,8)
assert eta(x)==F(255,2048)

lam=F(13571,100000)
repair=lam*L
deficiency_upper=F(17611420,10**9)  # 0.017611420, above certified d
assert repair > deficiency_upper

Cdag=F(6521851214,10**9)
cap=Cdag+lam*eta(m)
assert cap==F(1634703741,250000000)  # 6.538814964
quad_floor=F(130779577,20000000)      # 6.53897885
assert cap < quad_floor

# B18 local-concavity barrier compatibility for this explicit eta.
r=z
chord=2*r*eta(m)
assert eta(x) <= eta(m)
assert eta(r) >= chord

print("eta_mid", eta(m))
print("eta_3_8", eta(x))
print("eta_output", eta(r))
print("eta_output_minus_chord", eta(r)-chord, float(eta(r)-chord))
print("scalar_Rprime_lo", Rp(lo))
print("scalar_Rprime_hi", Rp(hi))
print("scalar_R_interval_lower_bound", Rlower, float(Rlower))
print("universal_exact_3bit_cases", cases)
print("universal_exact_3bit_min_increment", min_inc, "at", argmin)
print("prime_affine_gain_L", L, float(L))
print("lambda", lam, float(lam))
print("repair_increment", repair, float(repair))
print("deficiency_upper", deficiency_upper, float(deficiency_upper))
print("repair_slack_over_coarse_bound", repair-deficiency_upper, float(repair-deficiency_upper))
print("replacement_center_cap", cap, float(cap))
print("quadratic_only_center_floor", quad_floor, float(quad_floor))
print("center_improvement_vs_quadratic_floor", quad_floor-cap, float(quad_floor-cap))
print("PASS")
