import math
import random

S0 = 1.0/(480.0*math.sqrt(7626.0))
C0 = 3.0*(2.0**(1.0/3.0))*math.sqrt(6.0)
K = C0*(2.0**0.25)
gamma = 2.0**-25
a0 = delta0 = 1.0/64.0
e0 = gamma/a0
eta = 5.0*e0/delta0
self_remainder = 122.0*eta + 2.0*e0
full_structural = self_remainder + 1.0/64.0
partner = 34.0*math.sqrt(math.log((2.0**12)*math.e))
defect_gate = K*(S0**-0.25)*(gamma**-0.25)

print(f"S0={S0:.16e}")
print(f"K={K:.15f}")
print(f"gamma={gamma:.16e}")
print(f"defect_gate_bound={defect_gate:.12f}")
print(f"e0={e0:.16e}")
print(f"eta={eta:.16f}")
print(f"self_remainder_op_bound={self_remainder:.12f}")
print(f"full_structural_op_bound={full_structural:.12f}")
print(f"partner_bound={partner:.12f}")

# Regression test of the exact defect-circuit identity and the projected-area lower bound.
# This is not a proof; the proof is algebraic in REPORT.md.
random.seed(20260923)
max_alg_resid = 0.0
min_area_ratio = float("inf")
violations = 0
checked = 0

for _ in range(4000):
    while True:
        m11 = random.uniform(-2, 2)
        m12 = random.uniform(-2, 2)
        m21 = random.uniform(-2, 2)
        m22 = random.uniform(-2, 2)
        detM = m11*m22-m12*m21
        if abs(detM) > 0.15:
            break
    S = abs(detM)

    pi = [random.uniform(-1,1), random.uniform(-1,1)]
    pj = [random.uniform(-1,1), random.uniform(-1,1)]
    pk = [random.uniform(-1,1), random.uniform(-1,1)]
    b00 = random.uniform(-2,2)
    b01 = random.uniform(-2,2)
    b11 = random.uniform(-2,2)
    B0 = [[b00,b01],[b01,b11]]

    def dotB(x,y):
        return x[0]*(B0[0][0]*y[0]+B0[0][1]*y[1]) + x[1]*(B0[1][0]*y[0]+B0[1][1]*y[1])
    def det2(x,y):
        return x[0]*y[1]-x[1]*y[0]

    Eii = random.uniform(-1,1)
    Eji = random.uniform(-1,1)
    Eki = random.uniform(-1,1)
    a = dotB(pi,pi)+Eii
    if abs(a) < 0.05:
        continue
    checked += 1
    Bji = dotB(pj,pi)+Eji
    Bki = dotB(pk,pi)+Eki

    F = Eii*det2(pj,pk) - Eki*det2(pj,pi) - Eji*det2(pi,pk)
    uj = [pj[q]-(Bji/a)*pi[q] for q in range(2)]
    uk = [pk[q]-(Bki/a)*pi[q] for q in range(2)]
    lhs = a*det2(uj,uk)
    scale = 1.0+abs(lhs)+abs(F)
    max_alg_resid = max(max_alg_resid, abs(lhs-F)/scale)

    def row_from_p(p, z):
        return [p[0]*m11+p[1]*m21,
                p[0]*m12+p[1]*m22,
                z]
    zi,zj,zk = [random.uniform(-0.3,0.3) for __ in range(3)]
    ci,cj,ck = row_from_p(pi,zi),row_from_p(pj,zj),row_from_p(pk,zk)
    Di = ci
    Dj = [cj[q]-(Bji/a)*Di[q] for q in range(3)]
    Dk = [ck[q]-(Bki/a)*Di[q] for q in range(3)]
    cross = [Dj[1]*Dk[2]-Dj[2]*Dk[1],
             Dj[2]*Dk[0]-Dj[0]*Dk[2],
             Dj[0]*Dk[1]-Dj[1]*Dk[0]]
    full_area = math.sqrt(sum(x*x for x in cross))
    projected_area = S*abs(det2(uj,uk))
    if projected_area > 1e-14:
        ratio = full_area/projected_area
        min_area_ratio = min(min_area_ratio,ratio)
        if ratio < 1.0-1e-10:
            violations += 1

print(f"checked_instances={checked}")
print(f"max_algebra_residual={max_alg_resid:.6e}")
print(f"min_observed_area_ratio={min_area_ratio:.12f}")
print(f"area_violations={violations}")

assert defect_gate < 11991.0
assert self_remainder < 0.075
assert full_structural < 0.091
assert partner < 104.0
assert max_alg_resid < 1e-10
assert violations == 0
print("QFORM_B19_R41_CHECK_PASS")
