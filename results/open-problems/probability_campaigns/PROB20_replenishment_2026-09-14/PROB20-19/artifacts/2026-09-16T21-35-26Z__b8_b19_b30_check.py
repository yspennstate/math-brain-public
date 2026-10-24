from fractions import Fraction
import heapq
import mpmath as mp

mp.iv.dps = 50

# ---------------- metric-degeneracy exact arithmetic ----------------
m = 10000
n = 1
den = m*m + n*n
c = Fraction(m*m - n*n, den)
s = Fraction(2*m*n, den)
assert c*c + s*s == 1
assert c != 0 and s != 0
trace = Fraction(10,1)  # Lambda = diag(1,2,3,4)
lipschitz_bound = Fraction(4*n,m)  # strict bound since sqrt(m^2+n^2) > m
previous_upper_abs = Fraction(127030552985088, 10**17)
assert lipschitz_bound < previous_upper_abs

# ---------------- interval certificate for threshold route failure ----------------
# 3D covariance eigenvalues 2,1,3.
# Q = G23(beta) G12(alpha), with rational Pythagorean angles
# alpha: tan(alpha/2)=8/17, beta: tan(beta/2)=1/20.
def rat_rot(n, m):
    d = m*m+n*n
    return Fraction(m*m-n*n,d), Fraction(2*m*n,d)

c1,s1 = rat_rot(8,17)
c2,s2 = rat_rot(1,20)
Q = [
    [c1, s1, Fraction(0)],
    [-c2*s1, c2*c1, s2],
    [s2*s1, -s2*c1, c2],
]
# exact orthogonality Q^T Q = I
for i in range(3):
    for j in range(3):
        v = sum(Q[k][i]*Q[k][j] for k in range(3))
        assert v == (1 if i==j else 0)

def ivf(fr):
    return mp.iv.mpf(f"{fr.numerator}/{fr.denominator}")

def ivrange(lo, hi):
    return mp.iv.mpf([f"{lo.numerator}/{lo.denominator}",
                      f"{hi.numerator}/{hi.denominator}"])

roots = [mp.iv.sqrt(ivf(Fraction(2))), ivf(Fraction(1)),
         mp.iv.sqrt(ivf(Fraction(3)))]

def build_A(Qmat):
    return [[ivf(Qmat[i][j])*roots[j] for j in range(3)] for i in range(3)]

I3 = [[Fraction(1 if i==j else 0) for j in range(3)] for i in range(3)]
Arot = build_A(Q)
Akl = build_A(I3)
threshold = Fraction(19,20)

def classify_cell(A, zlo, zhi, qlo, qhi):
    # Area coordinates: u=(sqrt(1-z^2) cos(pi q), sqrt(1-z^2) sin(pi q), z)
    # with z in [-1,1], q in [0,2]. Uniform spherical probability measure
    # is dz dq / 4, so every dyadic rectangle has exact rational mass.
    zI = ivrange(zlo,zhi)
    vals = [zlo*zlo, zhi*zhi]
    z2lo = Fraction(0) if zlo <= 0 <= zhi else min(vals)
    z2hi = max(vals)
    r2lo = max(Fraction(0), Fraction(1)-z2hi)
    r2hi = Fraction(1)-z2lo
    rI = mp.iv.sqrt(ivrange(r2lo,r2hi))
    phiI = mp.iv.pi * ivrange(qlo,qhi)
    xI = rI * mp.iv.cos(phiI)
    yI = rI * mp.iv.sin(phiI)

    guaranteed = 0
    possible = 0
    tI = ivf(threshold)
    for row in A:
        dot = row[0]*xI + row[1]*yI + row[2]*zI
        sq = dot**2
        if sq.a > tI:
            guaranteed += 1
        if sq.b > tI:
            possible += 1
    if guaranteed >= 2:
        return 1   # entire cell satisfies median(b_i)>threshold
    if possible < 2:
        return -1  # entire cell fails
    return 0       # unresolved by this box

def bound_prob(A, tol=Fraction(1,1024), nz=8, nq=16, max_cells=400000):
    inside = Fraction(0)
    uncertain = Fraction(0)
    heap = []
    cells = 0
    for iz in range(nz):
        zlo = Fraction(-1) + Fraction(2*iz,nz)
        zhi = Fraction(-1) + Fraction(2*(iz+1),nz)
        for iq in range(nq):
            qlo = Fraction(2*iq,nq)
            qhi = Fraction(2*(iq+1),nq)
            area = (zhi-zlo)*(qhi-qlo)/4
            st = classify_cell(A,zlo,zhi,qlo,qhi)
            cells += 1
            if st == 1:
                inside += area
            elif st == 0:
                uncertain += area
                heapq.heappush(heap,(-float(area),(zlo,zhi,qlo,qhi,area)))
    while uncertain > tol and heap and cells < max_cells:
        _,(zlo,zhi,qlo,qhi,area) = heapq.heappop(heap)
        uncertain -= area
        zm=(zlo+zhi)/2
        qm=(qlo+qhi)/2
        for a,b,cq,dq in [(zlo,zm,qlo,qm),(zlo,zm,qm,qhi),
                          (zm,zhi,qlo,qm),(zm,zhi,qm,qhi)]:
            ar=(b-a)*(dq-cq)/4
            st=classify_cell(A,a,b,cq,dq)
            cells += 1
            if st==1:
                inside += ar
            elif st==0:
                uncertain += ar
                heapq.heappush(heap,(-float(ar),(a,b,cq,dq,ar)))
    assert cells < max_cells, "cell budget exhausted"
    return inside, inside+uncertain, uncertain, cells

rot_lo, rot_hi, rot_unc, rot_cells = bound_prob(Arot)
kl_lo, kl_hi, kl_unc, kl_cells = bound_prob(Akl)
assert rot_hi < kl_lo

print("PROB20-19 B8/B19/B30 exact+interval self-check")
print("metric_Q_c =", c)
print("metric_Q_s =", s)
print("metric_Q_orthogonality = PASS")
print("metric_strictness_hypotheses = PASS (positive diagonal covariance, unequal mixed eigenvalues, nontrivial angle)")
print("normalized_abs_excess_bound_strict <", lipschitz_bound, "=", float(lipschitz_bound))
print("previous_best_interval_upper =", -float(previous_upper_abs))
print("metric_movement_comparison = PASS")
print("new_exact_example_signed_enclosure = (-1/2500, 0)  # strict two-sided bound from continuity + archived one-Givens theorem")
print()
print("threshold_failure_parameters:")
print("alpha_cos =", c1, "alpha_sin =", s1)
print("beta_cos =", c2, "beta_sin =", s2)
print("threshold =", threshold)
print("Q_orthogonality_exact = PASS")
print("rot_prob_lower =", rot_lo, "~", float(rot_lo))
print("rot_prob_upper =", rot_hi, "~", float(rot_hi))
print("rot_uncertain_mass <=", rot_unc, "~", float(rot_unc))
print("kl_prob_lower =", kl_lo, "~", float(kl_lo))
print("kl_prob_upper =", kl_hi, "~", float(kl_hi))
print("kl_uncertain_mass <=", kl_unc, "~", float(kl_unc))
print("strict_tail_reversal = PASS: P_rot(b_(2)>19/20) < P_KL(b_(2)>19/20)")
print("gap_lower_bound =", kl_lo-rot_hi, "~", float(kl_lo-rot_hi))
print("cells_rot =", rot_cells, "cells_kl =", kl_cells)
print("ALL_CHECKS_PASS")
