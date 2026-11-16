#!/usr/bin/env python3
"""Exact rational support, mass, and convex-order certificates."""
import itertools
import json
from pathlib import Path
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
t,x=S.symbols('t x',real=True)
R=S.Rational


def parts(n,floor):
    if n==3:
        e=R(1,10);base=[(0,e,5),(e,1-e,0),(1-e,1,5)]
        h=S.Integer(1)
    else:
        e=R(1,20);base=[(0,e,12),(e,1-e,0),(1-e,1,8)]
        h=R(157,100)-R(57,50)*x
    return [(S.sympify(a),S.sympify(b),R(9,10)*f+h/10 if floor else S.sympify(f)) for a,b,f in base]


def call_polynomial(ss,z,midpoint):
    ans=0
    for a,b,f in ss:
        if midpoint>=b:
            continue
        lower=a if midpoint<=a else z
        ans+=S.integrate((x-z)*f,(x,lower,b))
    return S.expand(ans)


def call_gap_cert(n,floor):
    ss=parts(n,floor)
    mass=sum(S.integrate(f,(x,a,b)) for a,b,f in ss)
    mu=sum(S.integrate(x*f,(x,a,b)) for a,b,f in ss)
    assert mass==1
    c=n-1;K=n*mu
    knots=sorted(set([a for a,b,f in ss]+[b for a,b,f in ss]+[K-c*a for a,b,f in ss]+[K-c*b for a,b,f in ss]))
    records=[]
    for lo,hi in zip(knots[:-1],knots[1:]):
        mid=(lo+hi)/2;s=(K-t)/c
        # Put-call parity: E(s-X)+ = C_X(s)+s-mu.
        d=S.expand(c*(call_polynomial(ss,s,(K-mid)/c)+s-mu)-call_polynomial(ss,t,mid))
        candidates=[lo,hi]
        for z in S.solve(S.diff(d,t),t):
            if z.is_real and bool(z>lo) and bool(z<hi):
                candidates.append(z)
        vals=[S.simplify(d.subs(t,z)) for z in candidates]
        for value in vals:
            assert value.is_nonnegative is True,(n,floor,lo,hi,value)
        records.append(dict(left=str(lo),right=str(hi),polynomial=str(d),
                            minimum=float(min(vals,key=lambda z:float(z)))))
    return mu,records


def main():
    out={}
    for n in (3,4):
        e=R(1,10) if n==3 else R(1,20)
        for floor in (False,True):
            mu,polys=call_gap_cert(n,floor)
            intervals=[(k*(1-e),k*(1-e)+n*e) for k in range(n+1)]
            K=n*mu
            gap=min(min(abs(K-a),abs(K-b)) for a,b in intervals)
            assert all(not a<=K<=b for a,b in intervals)
            ss=parts(n,floor)
            outside=sum(S.integrate(f,(x,max(a,e),min(b,1-e))) for a,b,f in ss if min(b,1-e)>max(a,e))
            lower=S.simplify(gap**2*(1-n*outside))
            assert lower>0
            out[f'n{n}_'+('positive' if floor else 'two_bumps')]=dict(
                mean=str(mu),sum_target=str(K),core_sum_intervals=[[str(a),str(b)] for a,b in intervals],
                gap=str(gap),outside_probability=str(outside),mse_lower_bound=str(lower),
                mse_lower_bound_decimal=float(lower),call_gap_pieces=polys)
    # Same-mean affine filler used for n=4: positive Bernstein certificate.
    mu=R(81,200);s=(4*mu-t)/3
    C=lambda z:(1-z)**2*(R(81,200)-R(19,100)*z)
    d=S.Poly(S.expand(3*(C(s)+s-mu)-C(t)),t)
    bern=[S.simplify(sum(d.nth(k)*S.binomial(i,k)/S.binomial(3,k) for k in range(i+1))) for i in range(4)]
    assert all(b>0 for b in bern)
    out['affine_filler']={'call_gap':str(d.as_expr()),'bernstein_coefficients':list(map(str,bern))}
    # Reachable target, insufficient middle mass: every sum-3 triple has a 1.
    triples=[z for z in itertools.combinations_with_replacement((0,1,2),3) if sum(z)==3]
    assert triples==[(0,1,2),(1,1,1)]
    out['reachable_lattice']={'triples':triples,'middle_mass':'1/50','necessary_middle_mass':'1/3'}
    # Analytic positive polynomial counterexample, symmetric about 1/2.
    f=R(1,10)+R(27,10)*(2*x-1)**2
    assert S.integrate(f,(x,0,1))==1
    assert S.integrate(x*f,(x,0,1))==R(1,2)
    middle=S.integrate(f,(x,R(1,4),R(3,4)))
    outside=S.integrate(f,(x,R(1,5),R(4,5)))
    assert middle==R(13,80)<R(1,3)
    out['positive_polynomial_n3']={'density':str(f),'mean':'1/2',
        'middle_probability':str(middle),'expanded_middle_probability':str(outside),
        'core_gap':'1/10','mse_lower_bound':str(S.simplify((1-3*outside)/100))}
    (ROOT/'data/exact_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Exact rational and algebraic checks passed for all four densities.')
    for name,row in out.items():
        if 'gap' in row:
            print(name,row['mean'],row['gap'],row['outside_probability'],row['mse_lower_bound'])


if __name__=='__main__':
    main()
