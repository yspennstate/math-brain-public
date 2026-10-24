#!/usr/bin/env python3
"""Exact certificates for C061; numerical entropies are illustrations only.

Run from any directory with Python and SymPy. Writes exact_certificate.json
and results.json beside this script. The theorem itself is proved in C061.md.
"""

from itertools import product
from pathlib import Path
import json

import sympy as sp
import mpmath as mp


OUT = Path(__file__).resolve().parent
R = sp.Rational
I = sp.I
BITS = [(0, 0), (1, 0), (0, 1), (1, 1)]


def simp(x):
    return sp.cancel(sp.expand(x))


def atoms(K):
    n = K.rows
    vals = []
    for mask in range(1 << n):
        Q = K.copy()
        missing = 0
        for j in range(n):
            if not (mask >> j) & 1:
                Q[j, j] -= 1
                missing += 1
        vals.append(simp((-1) ** missing * Q.det()))
    assert simp(sum(vals) - 1) == 0
    return vals


def pair_atoms(a, b, off_abs2):
    d = a * b - off_abs2
    return list(map(simp, [1-a-b+d, a-d, b-d, d]))


def push(C1, C2, p):
    # Physical coordinate order: first block, then second block.
    return [simp(sum(C1[y1][x1] * C2[y2][x2] * p[k]
                     for k, (x1, x2) in enumerate(BITS)))
            for y2 in range(len(C2)) for y1 in range(len(C1))]


def balanced(C):
    d = [v[1]-v[0] for v in C]
    pos = [i for i, x in enumerate(d) if x > 0]
    neg = [i for i, x in enumerate(d) if x < 0]
    remain_pos = {i: d[i] for i in pos}
    remain_neg = {j: -d[j] for j in neg}
    groups = []
    for i in pos:
        for j in neg:
            r = min(remain_pos[i], remain_neg[j])
            if not r:
                continue
            lp, ln = r/d[i], r/(-d[j])
            w = simp(lp*C[i][0] + ln*C[j][0])
            rho, slope = simp(lp*C[i][0]/w), simp(r/w)
            assert 0 <= rho <= rho+slope <= 1
            groups.append(dict(positive=i, negative=j, r=r, w=w,
                               rho=rho, slope=slope, lp=lp, ln=ln))
            remain_pos[i] -= r
            remain_neg[j] -= r
    for y, delta in enumerate(d):
        if delta == 0 and C[y][0] != 0:
            groups.append(dict(positive=None, negative=y, r=0,
                               w=C[y][0], rho=0, slope=0, lp=0, ln=1))
    assert all(x == 0 for x in remain_pos.values())
    assert all(x == 0 for x in remain_neg.values())
    assert sum(g['w'] for g in groups) == 1
    tau = sum(abs(x) for x in d)/2
    assert sum(g['w']*g['slope'] for g in groups) == tau
    return groups, tau


def leading_minors(K):
    return [simp(K[:j, :j].det()) for j in range(1, K.rows+1)]


def fisher(p, dp):
    return simp(sum(v*v/q for q, v in zip(p, dp) if q))


def log_signature(coefficients, values):
    """Exact rational coefficients of log primes in sum c*log(q)."""
    signature = {}
    for c, q in zip(coefficients, values):
        c, q = simp(c), simp(q)
        if not c or not q:
            continue
        assert q.is_Rational and q > 0
        num, den = q.as_numer_denom()
        for sign, integer in [(1, num), (-1, den)]:
            for prime, exponent in sp.factorint(integer).items():
                signature[prime] = signature.get(prime, 0) + sign*c*exponent
    return {str(k): simp(v) for k, v in sorted(signature.items()) if simp(v)}


def number(x):
    return mp.mpf(str(sp.N(x, 85)))


def entropy(p):
    return -sum(number(q)*mp.log(number(q)) for q in p if q)


def jsonify(obj):
    if isinstance(obj, sp.MatrixBase):
        return [[str(simp(x)) for x in row] for row in obj.tolist()]
    if isinstance(obj, sp.Basic):
        return str(obj)
    if isinstance(obj, dict):
        return {str(k): jsonify(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonify(v) for v in obj]
    return obj


def main():
    mp.mp.dps = 75
    D1 = sp.Matrix([[R(2,5), R(1,10)], [R(1,10), R(3,5)]])
    D2 = sp.Matrix([[R(3,5), -R(1,10)], [-R(1,10), R(2,5)]])
    u = sp.Matrix([1,1])
    v = sp.Matrix([1,-1])
    D = sp.diag(D1,D2)
    U = sp.Matrix([[1,0],[1,0],[0,1],[0,-1]])
    alphas = [(w.T*B.inv()*w)[0]**-1 for B,w in [(D1,u),(D2,v)]]
    betas = [(w.T*(sp.eye(2)-B).inv()*w)[0]**-1
             for B,w in [(D1,u),(D2,v)]]
    ells = list(map(simp, [a+b for a,b in zip(alphas,betas)]))
    assert alphas == [R(23,80)]*2
    assert betas == [R(23,120)]*2
    assert ells == [R(23,48)]*2
    ell = ells[0]
    channels = []
    endpoints = []
    endpoint_spectra = []
    for B,w,a,b in zip([D1,D2],[u,v],alphas,betas):
        Q0,Q1 = B-a*w*w.T, B+b*w*w.T
        c0,c1 = atoms(Q0),atoms(Q1)
        assert all(p >= 0 for p in c0+c1)
        channels.append(list(map(list,zip(c0,c1))))
        endpoints.append([Q0,Q1])
        endpoint_spectra.append([list(Q0.eigenvals()),list(Q1.eigenvals())])
    C1,C2 = channels
    G1,tau1 = balanced(C1)
    G2,tau2 = balanced(C2)
    assert tau1 == tau2 == R(23,40)

    m1,m2,x,y = sp.symbols('m1 m2 x y', real=True)
    M = sp.Matrix([[m1,x+I*y],[x-I*y,m2]])

    def kernel(F):
        return D+U*(ell*F-sp.diag(*alphas))*U.T

    # Symbolic all-domain atom identity, using all four real parameters.
    p_in = pair_atoms(m1,m2,x*x+y*y)
    p_out = push(C1,C2,p_in)
    p_direct = atoms(kernel(M))
    assert all(simp(p-q) == 0 for p,q in zip(p_out,p_direct))

    # Symbolic balanced-refinement conditional DPP identity, atom by atom.
    group_conditional = []
    group_weights = []
    refined = []
    for g,h in product(G1,G2):
        r1,s1,r2,s2 = g['rho'],g['slope'],h['rho'],h['slope']
        q = pair_atoms(r1+s1*m1,r2+s2*m2,s1*s2*(x*x+y*y))
        wt = g['w']*h['w']
        direct = []
        for b1,b2 in BITS:
            row1 = g['positive'] if b1 else g['negative']
            row2 = h['positive'] if b2 else h['negative']
            lam1 = g['lp'] if b1 else g['ln']
            lam2 = h['lp'] if b2 else h['ln']
            direct.append(simp(lam1*lam2*p_out[row1+4*row2]))
        assert all(simp(a-wt*b) == 0 for a,b in zip(direct,q))
        group_conditional.append(q)
        group_weights.append(wt)
        refined.extend(direct)
    assert simp(sum(refined)-1) == 0

    M0 = sp.Matrix([[R(1,3),(1+I)/12],[(1-I)/12,R(2,5)]])
    M1 = sp.Matrix([[R(3,5),(2-I)/15],[(2+I)/15,R(2,3)]])
    E = M1-M0
    delta = simp(E.det())
    assert delta == R(83,1800)
    K0,K1 = kernel(M0),kernel(M1)
    feasibility = {}
    for name,K in [('M0',M0),('M1',M1),('K0',K0),('K1',K1),('D',D)]:
        mins = leading_minors(K)
        comins = leading_minors(sp.eye(K.rows)-K)
        assert all(x > 0 for x in mins+comins)
        feasibility[name] = dict(kernel_minors=mins,complement_minors=comins)
    commutator = sp.simplify(K0*K1-K1*K0)
    assert commutator[0,0] == R(529,34560)*I
    assert D1*u != u*(u.T*D1*u)[0]/(u.T*u)[0]
    assert D2*v != v*(v.T*D2*v)[0]/(v.T*v)[0]

    t = sp.symbols('t',real=True)
    Mt = M0+t*E
    substitutions = {m1:Mt[0,0],m2:Mt[1,1],
                     x:sp.re(Mt[0,1]),y:sp.im(Mt[0,1])}
    path = [simp(p.subs(substitutions)) for p in p_out]
    dp = [sp.diff(p,t) for p in path]
    ddp = [sp.diff(p,t,2) for p in path]
    assert all(sp.diff(p,t,3) == 0 for p in path)
    midpoint = {t:R(1,2)}
    p = [simp(q.subs(midpoint)) for q in path]
    pd = [simp(q.subs(midpoint)) for q in dp]
    pdd = [simp(q.subs(midpoint)) for q in ddp]
    assert all(q > 0 for q in p)
    Fout = fisher(p,pd)
    Fmix = 0
    curv_log_vals,curv_log_coeffs = [],[]
    for wt,q in zip(group_weights,group_conditional):
        qp = [simp(a.subs(substitutions)) for a in q]
        qm = [simp(a.subs(midpoint)) for a in qp]
        qd = [simp(sp.diff(a,t).subs(midpoint)) for a in qp]
        qdd = [simp(sp.diff(a,t,2).subs(midpoint)) for a in qp]
        assert all(a > 0 for a in qm)
        Fmix += wt*fisher(qm,qd)
        curv_log_vals.extend(qm)
        curv_log_coeffs.extend([wt*a for a in qdd])
    Fmix = simp(Fmix)
    assert Fout == Fmix
    # -H'' = Fisher + sum p'' log p. This compares the logarithmic
    # parts exactly by prime exponents, without numerical log evaluation.
    log_out = log_signature(pdd,p)
    log_mix = log_signature(curv_log_coeffs,curv_log_vals)
    assert log_out == log_mix

    lower_curvature = simp(8*delta*tau1*tau2)
    lower_gap = simp(delta*tau1*tau2)  # 4*t*(1-t) at t=1/2.
    assert lower_curvature == R(43907,360000)
    assert lower_gap == R(43907,2880000)
    curvature = number(Fout)+sum(number(a)*mp.log(number(q)) for a,q in zip(pdd,p))
    p0 = [q.subs(t,0) for q in path]
    p1 = [q.subs(t,1) for q in path]
    h0,hm,h1 = entropy(p0),entropy(p),entropy(p1)
    gap = hm-(h0+h1)/2
    assert curvature > number(lower_curvature)
    assert gap > number(lower_gap)

    cert = dict(
        description='All equalities and signs here use exact symbolic arithmetic.',
        reservoirs=[D1,D2],vectors=[u,v],alpha=alphas,beta=betas,ell=ells,
        channel_endpoints=endpoints,endpoint_eigenvalues=endpoint_spectra,
        channel_columns=channels,groups=[G1,G2],total_variations=[tau1,tau2],
        symbolic_full_domain_atom_identities=16,
        symbolic_balanced_group_atom_identities=36,
        M0=M0,M1=M1,direction=E,direction_determinant=delta,
        K0=K0,K1=K1,feasibility=feasibility,
        noncommutator_entry_11=commutator[0,0],
        midpoint_probabilities=p,midpoint_derivatives=pd,midpoint_second_derivatives=pdd,
        midpoint_fisher=Fout,midpoint_mixture_fisher=Fmix,
        midpoint_log_prime_signature=log_out,
        exact_logarithmic_curvature_decomposition=True,
        curvature_lower_bound=lower_curvature,midpoint_gap_lower_bound=lower_gap,
    )
    results = dict(
        description='High-precision numerical illustrations of the proved bounds.',
        entropy_K0=mp.nstr(h0,45),entropy_midpoint=mp.nstr(hm,45),
        entropy_K1=mp.nstr(h1,45),midpoint_gap=mp.nstr(gap,45),
        midpoint_gap_lower_bound=mp.nstr(number(lower_gap),45),
        minus_midpoint_entropy_hessian=mp.nstr(curvature,45),
        hessian_lower_bound=mp.nstr(number(lower_curvature),45),
        exact_symbolic_checks_passed=True,
    )
    (OUT/'exact_certificate.json').write_text(json.dumps(jsonify(cert),indent=2)+'\n')
    (OUT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))


if __name__ == '__main__':
    main()
