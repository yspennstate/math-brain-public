"""Exact independent checks: heterogeneous terminal rows over three cores.

Each terminal row has one activity across its three spokes, but different
rows may have different activities. Enumerate the original graph's forests
as integer monomials, and independently classify terminal bridges.
"""
from collections import Counter
from fractions import Fraction
from functools import reduce
from operator import mul
from pathlib import Path
import json
import random


def prod(values):
    return reduce(mul, values, 1)


def merge(parent, u, v):
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    ru, rv = root(u), root(v)
    if ru == rv:
        return None
    updated = list(parent)
    updated[ru] = rv
    return tuple(updated)


def original_coefficients(m):
    cores = (m,m+1,m+2)
    core_edges = ((cores[0],cores[1]),(cores[0],cores[2]),(cores[1],cores[2]))
    spokes = [(row,v) for row in range(m) for v in cores]
    answer = [Counter() for _ in range(4)]
    for mask in range(8):
        state = tuple(range(m+3))
        for j,edge in enumerate(core_edges):
            if mask >> j & 1:
                state = merge(state,*edge)
                if state is None:
                    break
        if state is None:
            continue
        counts = [0]*m

        def walk(index,parent):
            if index == len(spokes):
                key = (tuple(counts),mask)
                answer[0][key] += 1
                with_e = merge(parent,0,1)
                with_f = merge(parent,2,3)
                if with_e is not None:
                    answer[1][key] += 1
                    if merge(with_e,2,3) is not None:
                        answer[3][key] += 1
                if with_f is not None:
                    answer[2][key] += 1
                return
            walk(index+1,parent)
            row,v = spokes[index]
            updated = merge(parent,row,v)
            if updated is not None:
                counts[row] += 1
                walk(index+1,updated)
                counts[row] -= 1
        walk(0,state)
    return answer


def evaluate(polynomials,activities,core):
    # Use a denominator independent of the selected monomial. Each row has
    # at most three spokes and each of the three core edges appears once.
    activities,core = list(map(Fraction,activities)),list(map(Fraction,core))
    denominator = prod(a.denominator**3 for a in activities)*prod(x.denominator for x in core)
    row_factors = [[a.numerator**k*a.denominator**(3-k) for k in range(4)] for a in activities]
    core_factors = [prod(x.numerator if mask >> j & 1 else x.denominator for j,x in enumerate(core)) for mask in range(8)]
    values = []
    for polynomial in polynomials:
        numerator = sum(c*prod(row_factors[j][k] for j,k in enumerate(counts))*core_factors[mask]
                        for (counts,mask),c in polynomial.items())
        values.append(Fraction(numerator,denominator))
    return values


def bridge(activities,core):
    us = [a*a/(1+3*a) for a in activities]
    vs = [a**3/(1+3*a) for a in activities]
    p,q,r = core
    X = p+q+r
    S,L = 1+X+p*q+p*r+q*r,3+2*X
    pair_sum = sum(us[i]*us[j] for i in range(len(us)) for j in range(i))
    return prod(1+3*a for a in activities)*(S+L*sum(us)+sum(vs)+6*pair_sum)


def proposed_certificate(activities,core):
    alpha = lambda x:x*x/(1+3*x)
    gamma = lambda x:x**3/(1+3*x)**2
    D = prod(1+3*a for a in activities)
    U,Gamma = sum(map(alpha,activities)),sum(map(gamma,activities))
    p,q,r = core
    X = p+q+r
    S,L = 1+X+p*q+p*r+q*r,3+2*X
    Ab = S+L*U+Gamma+3*U*U
    corrections = []
    for i,j in ((0,1),(2,3)):
        a,b = activities[i],activities[j]
        delta = alpha(a+b)-alpha(a)-alpha(b)
        epsilon = gamma(a+b)-gamma(a)-gamma(b)
        correction = (1+3*(a+b))/((1+3*a)*(1+3*b))
        x = delta*(L+6*U)+epsilon+3*delta*delta
        assert delta>0 and epsilon>0
        corrections.append((delta,epsilon,correction,x))
    de,ee,ce,xe = corrections[0]
    df,ef,cf,xf = corrections[1]
    bracket = xe*xf-6*de*df*Ab
    lower = de*df*(L*L-6*S+6*L*U+18*U*U-6*Gamma)
    assert bracket>lower>0
    return D*D*ce*cf*bracket


def main():
    rng = random.Random(4815162342)
    report = dict(status="PASS",direct=[],formula_checks=[],scope="Only the two disjoint added matching marks")
    for m in (4,5):
        polynomials = original_coefficients(m)
        report.setdefault("monomial_counts",{})[str(m)] = [len(x) for x in polynomials]
        cases = [(list(map(Fraction,[1,2,3,4]+([5] if m==5 else []))),list(map(Fraction,[0,0,0]))),
                 ([Fraction(1,100),Fraction(7),Fraction(2,3),Fraction(100)]+([Fraction(3,5)] if m==5 else []),
                  list(map(Fraction,[0,3,1])))]
        for _ in range(18):
            aa = [Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(m)]
            core = [Fraction(rng.randrange(0,10),rng.randrange(1,10)) for _ in range(3)]
            cases.append((aa,core))
        for aa,core in cases:
            actual = evaluate(polynomials,aa,core)
            expected = [bridge(aa,core),bridge([aa[0]+aa[1]]+aa[2:],core),
                        bridge(aa[:2]+[aa[2]+aa[3]]+aa[4:],core),
                        bridge([aa[0]+aa[1],aa[2]+aa[3]]+aa[4:],core)]
            assert actual == expected
            R = actual[1]*actual[2]-actual[0]*actual[3]
            assert R == proposed_certificate(aa,core)>0
            report["direct"].append(dict(m=m,rows=list(map(str,aa)),core=list(map(str,core)),rayleigh=str(R)))
    for m in (4,5,6,10,25,100):
        for _ in range(5):
            aa = [Fraction(rng.randrange(1,30),rng.randrange(1,20)) for _ in range(m)]
            core = [Fraction(rng.randrange(0,20),rng.randrange(1,20)) for _ in range(3)]
            A = bridge(aa,core)
            Be = bridge([aa[0]+aa[1]]+aa[2:],core)
            Bf = bridge(aa[:2]+[aa[2]+aa[3]]+aa[4:],core)
            C = bridge([aa[0]+aa[1],aa[2]+aa[3]]+aa[4:],core)
            assert Be*Bf-A*C == proposed_certificate(aa,core)>0
            report["formula_checks"].append(dict(m=m,rows=list(map(str,aa)),core=list(map(str,core))))
    report["direct_cases"] = len(report["direct"])
    report["formula_cases"] = len(report["formula_checks"])
    Path(__file__).with_name("three_core_heterogeneous_ant_independent_checks.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k not in ("direct","formula_checks")},indent=2))


if __name__ == "__main__":
    main()
