"""Independent exact algebra and finite packing check. No claim code is used."""
import os
os.environ.update({k: '1' for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')})
import json
import resource
import time
from pathlib import Path
import sympy as s
import mpmath as mp

assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
started = time.monotonic()
t, z = s.symbols('t z')
f = t**4 + 4*t**2 - 1
def red(p):
    return s.rem(s.expand(p), f, t)

# Derive the three successive gap-insertion maps from their definition.
maps = []
for j in range(3):
    m = s.eye(4)
    m[j, :] = s.Matrix([[2, 2, 2, -1]])
    m[3, :] = s.Matrix([[int(k == j) for k in range(4)]])
    maps.append(m)
T = maps[2] * maps[1] * maps[0]
p = T.charpoly(z).as_expr()
y = 23 + 5*t**2  # 13 + 5 sqrt(5)
h = 47*t + 11*t**3
assert red(h*h-y*y+4) == 0
lam = (y+h)/2
assert red(p.subs(z,lam)) == 0

# Adjugate gives a left eigenvector, without assuming the supplied eigenvector.
adj = (z*s.eye(4)-T).adjugate()
w = s.Matrix([[red(e.subs(z,lam)) for e in adj[0,:]]])
assert all(red(e) == 0 for e in w*T-lam*w)
initial = s.Matrix([[1,1,0], [1,1,2], [4,1,4], [0,-1,0]])
weights = [red(e) for e in w*initial]
a = 1-t
b = t**3+4*t-1
assert red(weights[1]-a*weights[0]) == 0
assert red(weights[2]-b*weights[0]) == 0
assert weights[0] != 0
for row in range(4):
    wr = s.Matrix([[red(e.subs(z,lam)) for e in adj[row,:]]])
    pr = [red(e) for e in wr*initial]
    assert pr[0] != 0
    assert red(pr[1]-a*pr[0]) == 0
    assert red(pr[2]-b*pr[0]) == 0
assert red((b+1)**2-(t*t+4)) == 0
assert s.Poly(f,t).is_irreducible
norm2 = red(a*a+b*b)
coeff = s.Matrix([[s.expand(red(e)).coeff(t,k) for e in [1,a,b,norm2]] for k in range(4)])
assert coeff.det() != 0

# Generate the whole y in [0,2] band period up to a curvature cutoff,
# by subdividing BOTH curvilinear gaps between consecutive unit disks.
def insert(triple, opposite):
    return tuple(2*sum(c[k] for c in triple)-opposite[k] for k in range(3))

bottom, top = (1,1,0), (1,1,2)
left, right = (0,-1,0), (0,1,0)
cutoff = 3000
stack = [((left,bottom,top),right), ((right,bottom,top),left)]
circles = {bottom,top}
while stack:
    tri, opposite = stack.pop()
    child = insert(tri, opposite)
    if child[0] > cutoff:
        continue
    assert child[0] > max(c[0] for c in tri)
    assert child not in circles
    circles.add(child)
    for j in range(3):
        other = list(tri)
        other[j] = child
        stack.append((tuple(other),tri[j]))

mp.mp.dps = 150
tn = mp.sqrt(mp.sqrt(5)-2)
an, bn = 1-tn, mp.sqrt(mp.sqrt(5)+2)-1
min_gap = mp.inf
closest = None
for c,u,v in circles:
    # Exact curvature-center external tangency relation, for new circles,
    # is checked below along the independent orbit as well.
    gap = mp.sqrt((an-mp.mpf(u)/c)**2+(bn-mp.mpf(v)/c)**2)-mp.mpf(1)/c
    assert gap > 0
    if gap < min_gap:
        min_gap, closest = gap,(c,u,v)

# A deep sequence is independent of the branching cutoff above.
tri, opposite = [bottom,top,(4,1,4)],left
sequence = []
for step in range(180):
    child = insert(tri,opposite)
    c,u,v = child
    for d,x,y0 in tri:
        if d:
            assert (u*d-x*c)**2+(v*d-y0*c)**2 == (c+d)**2
    radius = mp.mpf(1)/c
    err = mp.sqrt((an-mp.mpf(u)/c)**2+(bn-mp.mpf(v)/c)**2)
    if step in [0,2,29,59,119,179]:
        sequence.append({'step': step+1,'curvature':str(c), 'radius':mp.nstr(radius,50), 'center_error':mp.nstr(err,50)})
    j = step % 3
    tri[j],opposite = child,tri[j]

result = {
 'nice':os.getpriority(os.PRIO_PROCESS,0), 'thread_limit':1,
 'derived_cycle_matrix':T.tolist(), 'characteristic_polynomial':str(p),
 'field_polynomial':str(f), 'irreducible':True,
 'norm_squared_reduction':str(norm2), 'coefficient_matrix':coeff.tolist(),
 'determinant':str(coeff.det()), 'dominant_eigenvalue_field':str(lam),
 'eigenvalue':mp.nstr((13+5*mp.sqrt(5)+mp.sqrt((13+5*mp.sqrt(5))**2-4))/2,70),
 'center':[mp.nstr(an,90),mp.nstr(bn,90)],
 'numerical_digits':150, 'packing_curvature_cutoff':cutoff,
 'packing_circles_checked':len(circles), 'minimum_distance_minus_radius':mp.nstr(min_gap,70),
 'nearest_checked_circle':closest, 'deep_sequence':sequence,
 'elapsed_seconds':time.monotonic()-started,
 'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
out = Path(__file__).with_name('independent_results.json')
out.write_text(json.dumps(result,indent=2,default=lambda x: int(x) if getattr(x,'is_Integer',False) else str(x))+'\n')
print(out.read_text())
