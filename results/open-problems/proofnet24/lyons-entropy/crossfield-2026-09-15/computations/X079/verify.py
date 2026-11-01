#!/usr/bin/env python3
"""Exact self-check of X079's determinant-feasible nonlinear comparison.

The all-n proof is in agents/X079.md. This script checks symbolic scalar
identities, all atoms of an exact complex four-site witness outside the old
slab, and logarithmic inequalities by rational interval bounds.
"""
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import sympy as s

out = Path(__file__).resolve().parent
checks = 0

def ck(v):
    global checks
    assert v
    checks += 1

def rat(x):
    x = s.cancel(x)
    return F(int(s.numer(x)), int(s.denom(x)))

def log_unit(q, terms=40):
    """Rational enclosure of log(q), 1<=q<=2."""
    assert F(1) <= q <= F(2)
    z = (q-1)/(q+1)
    lo = 2*sum((z**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    hi = lo + 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lo, hi

def log_bounds(q):
    """Rational enclosure with power-of-two range reduction."""
    q = F(q)
    if q < 1:
        lo, hi = log_bounds(1/q)
        return -hi, -lo
    k = 0
    while q > 2:
        q /= 2
        k += 1
    lo, hi = log_unit(q)
    l2, h2 = log_unit(F(2))
    return lo+k*l2, hi+k*h2

# Scalar identities for arbitrary two-site spectral data and overlap h.
x, y, h = s.symbols('x y h', real=True)
a = (1+x)*(1+y)/4
d = (1-x)*(1-y)/4
u = a+d
r = a*d/(a*d+h)
ff = h*(u/(a*d)+(1-u)/(a*d+h))
ck(s.factor(u-(1+x*y)/2) == 0)
ck(s.factor(ff-((1/r-r)/2+x*y*(1/r+r-2)/2)) == 0)
hmax = (x-y)**2/16
fmax = ff.subs(h, hmax)
claimed = (x-y)**2/(1-x*y)*(1/(2*(1-x*x))+1/(2*(1-y*y)))
ck(s.factor(fmax-claimed) == 0)
ck(s.factor(r.subs(h,hmax)-(1-(x-y)**2/(1-x*y)**2)) == 0)
ratio = (x-y)**2/(1-x*y)
ck(s.factor(s.diff(ratio,x)-(x-y)*(2-x*y-y*y)/(1-x*y)**2) == 0)
ck(s.factor(s.diff(ratio,y)+(x-y)*(2-x*y-x*x)/(1-x*y)**2) == 0)

# Every constant comparison in the analytic three-range proof is exact.
rho = F(4,5)
ck(4*rho*rho/(1-rho**4) == F(1600,369))
ck(F(528,325) < F(80,39))
ck(F(3200,1599) < F(80,39))
ck(F(6,19) < F(41,80))
ck(F(369) > F(19)**2)
ck(F(1)-F(41,80)*F(16,9) == F(4,45))
ck(F(4,45)/F(25,9) == F(4,125))
ck(log_bounds(F(3))[0] > F(13,12))
ck(F(25,9) < 3)

# A physical conditional table where Q is negative, retained by the proof.
negative_table = [F(9,100), F(157,200), F(7,200), F(9,100)]
na, nb, nc, nd = negative_table
nh = nb*nc-na*nd
nF = nh*sum((1/z for z in negative_table), F(0))
nlo,nhi = log_bounds(nb*nc/(na*nd))
ck(nh == F(31,1600))
ck(na+nd == F(9,50))
ck(nlo > nF)
ck(F(39,80)*nF < nlo)
ck(nhi < F(121,80)*nF)

# Exact complex 4-site witness with an asymmetric diagonal perturbation.
n = 4
U = s.Matrix([[3,4*s.I],[4*s.I,3]])/5
H = s.zeros(n)
H[:2,2:] = U
H[2:,:2] = U.conjugate().T
K0 = s.eye(n)/2+s.Rational(3,8)*H
K = K0+s.diag(1,-2,1,-1)/100
D = s.diag(1,-2,3,-4)/60
ck(U*U.conjugate().T == s.eye(2))
ck(H*H == s.eye(n))
ck(set(K0.eigenvals()) == {s.Rational(1,8),s.Rational(7,8)})
ck(s.Rational(1,8)-s.Rational(1,50) > s.Rational(1,10))
ck(s.Rational(7,8)+s.Rational(1,50) < s.Rational(9,10))
xs = list(itertools.product([0,1],repeat=n))
ps, jets = {}, {}
J = s.zeros(n)
W = s.zeros(n)
for bits in xs:
    B = K-s.diag(*[1-b for b in bits])
    R = B.inv()
    p = (-1)**(n-sum(bits))*B.det()
    ck(p>0)
    ck(R == R.conjugate().T)
    z = (R*D).trace()
    acc = z*z-(R*D*R*D).trace()
    ps[bits] = p
    jets[bits] = (s.cancel(p*z), s.cancel(p*acc))
    diagR = s.Matrix([R[i,i] for i in range(n)])
    J += p*diagR*diagR.T
    W += p*R.applyfunc(lambda z:s.expand(z*s.conjugate(z)))
    for i in range(n):
        ck(sum(s.expand(R[i,j]*s.conjugate(R[i,j])) for j in range(n) if j!=i)
           <=s.Rational(16,9)*R[i,i]**2)
    sign = (-1)**(n-sum(bits))
    first = sign*sum(D[i,i]*B.minor_submatrix(i,i).det() for i in range(n))
    second = 0
    for i,j in itertools.combinations(range(n),2):
        ids = [k for k in range(n) if k not in [i,j]]
        second += 2*sign*D[i,i]*D[j,j]*B.extract(ids,ids).det()
    ck((first,second) == jets[bits])

ck(sum(ps.values()) == 1)
ck(sum(p1 for p1,p2 in jets.values()) == 0)
ck(sum(p2 for p1,p2 in jets.values()) == 0)
ck(J == W)
pair_logs = {}
for i,j in itertools.combinations(range(n),2):
    outside = [k for k in range(n) if k not in [i,j]]
    cross = 0
    pair_logs[i,j] = []
    for obs in itertools.product([0,1],repeat=n-2):
        un = []
        for bi,bj in itertools.product([0,1],repeat=2):
            bits = [0]*n
            bits[i],bits[j] = bi,bj
            for k,b in zip(outside,obs):
                bits[k] = b
            un.append(ps[tuple(bits)])
        m = sum(un)
        a,b,c,d = [z/m for z in un]
        hh = b*c-a*d
        ff = hh*(1/a+1/b+1/c+1/d)
        ck(hh >= 0)
        # Eigenvalue slab of this actual conditional, via 2x2 PSD minors.
        ci,cj = c+d,b+d
        ck(ci >= s.Rational(1,10) and cj >= s.Rational(1,10))
        ck(ci <= s.Rational(9,10) and cj <= s.Rational(9,10))
        ck((ci-s.Rational(1,10))*(cj-s.Rational(1,10)) >= hh)
        ck((s.Rational(9,10)-ci)*(s.Rational(9,10)-cj) >= hh)
        ck(ff <= s.Rational(1600,369))
        lo,hi = log_bounds(rat(b*c/(a*d)))
        ck(F(39,80)*rat(ff) <= lo)
        ck(hi <= F(121,80)*rat(ff))
        cross += m*ff
        pair_logs[i,j].append((rat(m),lo,hi))
    ck(cross == J[i,j])

for i in range(n):
    ck(J[i,i]>=4)
    ck(sum(J[i,j] for j in range(n) if j!=i)<=s.Rational(16,9)*J[i,i])

fi = sum((rat(p1*p1/ps[bits]) for bits,(p1,p2) in jets.items()),F(0))
chi = sum((rat(D[i,i]**2*J[i,i]) for i in range(n)),F(0))
ck(fi <= F(25,9)*chi)
lo_curv = hi_curv = fi
for bits,(p1,p2) in jets.items():
    lo,hi = log_bounds(rat(ps[bits]))
    coeff = rat(p2)
    lo_curv += coeff*(lo if coeff>=0 else hi)
    hi_curv += coeff*(hi if coeff>=0 else lo)
ck(lo_curv > F(4,45)*chi)
ck(lo_curv > F(4,125)*fi)
# Independently enclosed pair formula agrees at certified high precision.
lo_pair = hi_pair = chi
for (i,j),ls in pair_logs.items():
    clo = sum((m*lo for m,lo,hi in ls),F(0))
    chi_log = sum((m*hi for m,lo,hi in ls),F(0))
    qlo,qhi = rat(J[i,j])-chi_log,rat(J[i,j])-clo
    coeff = rat(2*D[i,i]*D[j,j])
    lo_pair += coeff*(qlo if coeff>=0 else qhi)
    hi_pair += coeff*(qhi if coeff>=0 else qlo)
ck(lo_pair <= hi_curv and lo_curv <= hi_pair)
ck(max(hi_curv,hi_pair)-min(lo_curv,lo_pair) < F(1,10**30))

result = {
    'status':'PASS',
    'exact_assertions':checks,
    'atoms_checked':len(xs),
    'actual_two_site_conditionals_checked':24,
    'slab':['1/10','9/10'],
    'chi_curvature_coefficient':'4/45',
    'full_fisher_curvature_coefficient':'4/125',
    'signed_acceleration_payment_coefficient':'121/125',
    'witness_center_spectrum':['1/8','7/8'],
    'witness_fisher':float(fi),
    'witness_chi_energy':float(chi),
    'witness_negative_entropy_curvature_interval':[float(lo_curv),float(hi_curv)],
    'witness_curvature_vs_chi_ratio_lower':float(lo_curv/chi),
    'negative_conditional_Q_interval':[float(nF-nhi),float(nF-nlo)],
    'kernel':[[str(K[i,j]) for j in range(n)] for i in range(n)],
    'direction':[[str(D[i,j]) for j in range(n)] for i in range(n)]
}
(out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['kernel','direction']},indent=2))
