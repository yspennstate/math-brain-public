"""Exact determinant-jet checks and bounded high-precision Hessian diagnostics.
The all-parameter sign is proved in agents/X036.md, not inferred here.
"""
from pathlib import Path
import json
import sympy as s
import mpmath as mp

OUT = Path(__file__).resolve().parent
mp.mp.dps = 150
I = s.I

def atoms(K):
    n = K.rows
    return [s.expand((-1)**(n-mask.bit_count()) *
            (K-s.diag(*[int(not(mask>>j & 1)) for j in range(n)])).det())
            for mask in range(1 << n)]

def jets(K, A):
    t = s.Symbol('t', real=True)
    out = []
    for p in atoms(K+t*A):
        out.append((p.subs(t,0), s.diff(p,t).subs(t,0),
                    s.diff(p,t,2).subs(t,0)))
    return out

def exact(x):
    return s.cancel(s.expand(x))

def m(x):
    return mp.mpf(str(s.N(x, 165)))

a,x,y,u,v,w,z,c,d = s.symbols('a x y u v w z c d', real=True)
coords = (a,x,y,u,v,w,z,c,d)
Ksym = s.Matrix([[a,u-I*v,w-I*z], [u+I*v,x,c+I*d],
                 [w+I*z,c-I*d,y]])
polys = atoms(Ksym)
grad = [s.Matrix([s.diff(p,j) for j in coords]) for p in polys]
hess = [s.hessian(p,coords) for p in polys]
checks = 0
assert sum(polys) == 1
checks += 1

# Generic rank-one pair path: all four atoms are exactly affine.
bx,by,t,r1,r2 = s.symbols('bx by t r1 r2', real=True)
f1,f2 = s.symbols('f1 f2', real=True)
P = atoms(s.diag(bx,by)+t*s.Matrix([f1,I*f2])*s.Matrix([[f1,-I*f2]]))
for p in P:
    assert s.diff(p,t,2) == 0
    checks += 1

# Scalar constants used in the uniform Young estimate, checked rationally.
loss = s.Rational(25,1024)+s.Rational(1,2048)+s.Rational(1,524288)
assert loss < s.Rational(1,2)
assert 1+s.Rational(1,2048)+s.Rational(3,16*32**4) < 2
assert 1+s.Rational(6,1024) < 2
checks += 3

examples = [
    ('rational_asymmetric', s.Rational(1,10), s.Rational(1,32), s.Rational(1,64)),
    ('near_radius', s.Rational(1,3), s.Rational(1,12), s.Rational(1,12)),
    ('rare_center', s.Rational(1,10**9), s.Rational(1,32), s.Rational(1,64)),
    ('rare_and_unbalanced', s.Rational(1,10**3), s.Rational(1,10**2), s.Rational(1,10**12)),
    ('reverse_unbalanced', s.Rational(1,10**3), s.Rational(1,10**12), s.Rational(1,10**2)),
    ('near_one', s.Rational(10**9), s.Rational(1,32), s.Rational(1,64)),
]
results = []
A = s.Matrix([[s.Rational(2,3), s.Rational(1,5)-I/7, -s.Rational(1,11)+I/13],
              [s.Rational(1,5)+I/7, -s.Rational(3,4), s.Rational(1,17)+I/19],
              [-s.Rational(1,11)-I/13, s.Rational(1,17)-I/19, s.Rational(4,5)]])
for name,T,v1,v2 in examples:
    av = T*T/(1+T*T)
    b = 1-av
    sqrtq = T/(1+T*T)
    q = sqrtq**2
    r = v1*v1+v2*v2
    R = v1*v1*v2*v2
    assert r <= s.Rational(1,72)  # kappa=1/3
    checks += 1
    vals = {a:av,x:s.Rational(1,3),y:s.Rational(2,3),
            u:sqrtq*v1,v:0,w:0,z:sqrtq*v2,c:0,d:0}
    K = Ksym.subs(vals)
    zz = K[1:3,0:1]
    ww = A[1:3,0:1]
    C = A[1:3,1:3]
    alpha = A[0,0]
    J = jets(K,A)
    for bit,pi,pip in [(1,av,alpha),(0,b,-alpha)]:
        den = av if bit else -b
        F = s.diag(s.Rational(1,3),s.Rational(2,3))-zz*zz.conjugate().T/den
        E = C-(ww*zz.conjugate().T+zz*ww.conjugate().T)/den+alpha*zz*zz.conjugate().T/den**2
        rr = ww-alpha*zz/den
        Acc = -2*rr*rr.conjugate().T/den
        je = jets(F,E)
        ja = jets(F,Acc)
        for mask in range(4):
            full = J[(mask<<1)|bit]
            p0,p1,p2 = je[mask]
            assert exact(full[0]-pi*p0) == 0
            assert exact(full[1]-(pip*p0+pi*p1)) == 0
            assert exact(full[2]-(2*pip*p1+pi*(p2+ja[mask][1]))) == 0
            checks += 3
    pv = [exact(p.subs(vals)) for p in polys]
    assert all(p > 0 for p in pv)
    checks += 1
    gv = [g.subs(vals) for g in grad]
    hv = [h.subs(vals) for h in hess]
    H = mp.matrix(9)
    for k in range(8):
        pp = m(pv[k])
        for ii in range(9):
            for jj in range(9):
                H[ii,jj] -= m(gv[k][ii]*gv[k][jj]/pv[k])+m(hv[k][ii,jj])*mp.log(pp)
    weights = [1/q,1,1,v1*v1,v1*v1,v2*v2,v2*v2,q*R,q*R]
    scales = [1/mp.sqrt(m(weight)) for weight in weights]
    slack = mp.matrix(9)
    for ii in range(9):
        for jj in range(9):
            slack[ii,jj] = -H[ii,jj]*scales[ii]*scales[jj]-(mp.mpf('0.25') if ii==jj else 0)
    eig = mp.eigsy(slack,eigvals_only=True)
    assert eig[0] > 0
    results.append({'name':name,'a':str(av),'v1':str(v1),'v2':str(v2),
                    'raw_frobenius_gap':str(q*R/8),
                    'scaled_slack_min_eigenvalue':mp.nstr(eig[0],30),
                    'scaled_slack_max_eigenvalue':mp.nstr(eig[8],30),
                    'precision_decimal_digits':mp.mp.dps})

record = {'exact_assertions':checks,'young_loss':str(loss),
          'scope':'Exact determinant checks; high-precision finite eigenvalues are diagnostics, not a universal sign proof.',
          'full_hessian_cases':results}
(OUT/'results.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
