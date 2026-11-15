"""Exact polynomial and Sturm certificates for the cubic-graph counterexample."""
import json
from pathlib import Path
import sympy as s
from exact_spectra import polynomial


def main():
    record = json.loads(Path('data/fiedler_counterexamples.json').read_text())[0]
    n = 10
    a = s.zeros(n)
    for u,v in record['edges']:
        a[u,v]=a[v,u]=1
    x,z=s.symbols('x z')
    lap=3*s.eye(n)-a
    cubic=s.Poly(z**3-3*z-1,z)
    assert cubic.count_roots(s.Rational(1879,1000),s.Rational(1880,1000))==1
    f=s.Matrix([2,z*z-z-2,2-z*z,-1,z,-1,0,z,2-z*z,z*z-z-2])
    assert all(s.rem(q,cubic.as_expr(),z)==0 for q in a*f-z*f)
    p=s.Poly(lap.charpoly(x).as_expr(),x)
    assert s.rem(p.as_expr().subs(x,3-z),cubic.as_expr(),z)==0
    pp=p.exquo(s.Poly(x,x))
    assert pp.count_roots(0,s.Rational(6,5))==1
    rows=[]
    for e,lower,upper in [((0,2),47694,47695),((0,8),47694,47695),((2,4),48117,48118)]:
        b=a.copy();u,v=e;b[u,v]=b[v,u]=1
        q=polynomial(b.tolist())
        q0=q.exquo(s.Poly(x,x))
        lo,hi=s.Rational(lower,100000),s.Rational(upper,100000)
        assert q0.count_roots(0,lo)==0 and q0.count_roots(lo,hi)==1
        sturm=q0.sturm()
        def variation(t):
            signs=[s.sign(poly.eval(t)) for poly in sturm]
            signs=[int(v) for v in signs if v]
            return sum(u!=v for u,v in zip(signs,signs[1:]))
        rows.append(dict(edge=e,polynomial=s.factor(q.as_expr()).__str__(),
                         lower=str(lo),upper=str(hi),
                         sturm_variations=[variation(t) for t in [0,lo,hi]]))
    out=dict(graph=record['edges'],graph6=record['graph6'],
             laplacian_characteristic_polynomial=str(s.factor(p.as_expr())),
             adjacency_eigenvalue_polynomial=str(cubic.as_expr()),
             eigenvector=[str(v) for v in f],certificates=rows)
    Path('data/counterexample_exact.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
