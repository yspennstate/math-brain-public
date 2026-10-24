"""Verify the infinite Vandermonde family from integers, without an LP solver."""
from itertools import combinations
from pathlib import Path
import json
import sympy as s

root=Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text())
u=s.symbols('u')
x=[s.Integer(i) for i in range(5)]+[6+u]
E=set(range(6))
P=list(combinations(range(6),2))
T=list(combinations(range(6),3))
F=list(combinations(range(6),4))
def vd(r): return s.prod(x[j]-x[i] for i,j in combinations(r,2))
v2={r:s.expand(vd(r)**2) for r in P+T+F}
G2=s.expand(sum(v2[r] for r in P))
G4=s.expand(sum(v2[r] for r in F))
D=s.Poly(G2*G4,u)
edges=[tuple(tuple(a) for a in z) for z in cert['edges']]
assert len(edges)==len(set(edges))==90
assert set(edges)=={(a,j,tuple(sorted(E-set(a)-set(j)))) for a in P for j in combinations(sorted(E-set(a)),2)}
C=[[s.Rational(z) for z in row] for row in cert['coefficients_ascending']]
assert all(len(row)==9 for row in C)
assert all(z.q==1 and z>=0 for row in C for z in row)
assert [D.nth(k) for k in range(9)]==list(map(s.Integer,cert['D_ascending']))
polys=[sum(z*u**k for k,z in enumerate(row)) for row in C]
assert s.expand(sum(polys)-D.as_expr())==0
checks=9
for a in P:
    target=v2[a]*G4
    actual=sum(polys[i] for i,e in enumerate(edges) if e[0]==a)
    assert s.expand(actual-target)==0
    checks+=9
for b in P:
    target=v2[tuple(sorted(E-set(b)))]*G2
    actual=sum(polys[i] for i,e in enumerate(edges) if e[2]==b)
    assert s.expand(actual-target)==0
    checks+=9
sm={m:sum(x[i] for i in m) for m in T}
gn={m:s.expand(v2[m]*sum(v2[n]*(sm[m]-sm[n])**2 for n in T)) for m in T}
for m in T:
    actual=sum(polys[i] for i,(a,j,b) in enumerate(edges) for q in j if tuple(sorted(a+(q,)))==m)
    assert s.expand(actual-gn[m])==0
    checks+=9
for j in P:
    hn=v2[j]*G4+sum(v2[tuple(sorted(E-set(b)))]*G2 for b in P if not set(b)&set(j))-sum(gn[m] for m in T if set(j)<=set(m))
    actual=sum(polys[i] for i,e in enumerate(edges) if e[1]==j)
    assert s.expand(actual-hn)==0
    assert all(z>=0 for z in s.Poly(actual,u).all_coeffs())
    assert actual.subs(u,0)>0
    checks+=9

# Independently compare the middle identity with exact orthogonalization.
for val in [6,9]:
    xx=[0,1,2,3,4,val]
    V=[s.Matrix([y**k for y in xx]) for k in range(4)]
    for k in range(4):
        for z in V[:k]: V[k]-=z*(z.dot(V[k])/z.dot(z))
    Q=s.Matrix.hstack(*V); norms=[z.dot(z) for z in V]
    for m in T:
        direct=sum(Q.extract(m,[0,1,k]).det()**2/(norms[0]*norms[1]*norms[k]) for k in [2,3])
        assert s.factor(gn[m].subs(u,val-6)/D.as_expr().subs(u,val-6)-direct)==0
        checks+=1

at6={''.join(map(str,j)):str(s.factor(sum(polys[i] for i,e in enumerate(edges) if e[1]==j).subs(u,0)/D.nth(0))) for j in P}
# Exact failures of two stronger coefficientwise extensions, not DPP failures.
assert s.Poly(gn[(2,3,4)].subs(u,u-1),u).nth(2)==-1000
base=[0,1,2,3,4,6]
def basevd(r): return s.prod(base[j]-base[i] for i,j in combinations(r,2))
wa={p:basevd(p)**2*basevd(tuple(sorted(E-set(p))))**2 for p in P}
wg={m:basevd(m)**2*basevd(tuple(sorted(E-set(m))))**2*(sum(base[i] for i in m)-sum(base[i] for i in E-set(m)))**2 for m in T}
j=(0,2)
weighted_obstruction=wa[j]+sum(wa[b] for b in P if not set(b)&set(j))-sum(wg[m] for m in T if set(j)<=set(m))
assert weighted_obstruction==-562176
result={'status':'PASS: exact polynomial certificate for every t >= 6',
        'identity_coefficient_checks':checks,
        'nonnegative_integer_coefficients':810,
        'nonzero_coefficients':sum(bool(z>0) for row in C for z in row),
        'union_support':sum(any(row) for row in C),
        'support_by_degree':[sum(bool(row[k]>0) for row in C) for k in range(9)],
        'D_ascending':cert['D_ascending'],
        'active_pair_law_at_t6':at6,
        'min_active_pair_law_at_t6':str(min(s.Rational(v) for v in at6.values())),
        'no_numerical_optimization_in_verifier':True,
        'degree_two_middle_coefficient_at_base_t5':-1000,
        'all_once_weight_monomial_addition_02_coefficient_at_t6':int(weighted_obstruction)}
(root/'verified_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
