"""Independent exact original-graph checks of the three-core twin family.

Enumerates each acyclic unmarked subset once, storing its a,p,q,r monomial.
The two marked edges are actually inserted successively to test the mixed
coefficient; no transfer matrices or author's helper imports are used.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json


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
    core = (m, m + 1, m + 2)
    core_edges = ((core[0], core[1]), (core[0], core[2]), (core[1], core[2]))
    spokes = [(j, v) for j in range(m) for v in core]
    coeff = [Counter() for _ in range(4)]
    for core_mask in range(8):
        parent = tuple(range(m + 3))
        for j, edge in enumerate(core_edges):
            if core_mask >> j & 1:
                parent = merge(parent, *edge)
                if parent is None:
                    break
        if parent is None:
            continue

        def walk(index, state, spoke_count):
            if index == len(spokes):
                key = (spoke_count, core_mask)
                coeff[0][key] += 1
                after_e = merge(state, 0, 1)
                after_f = merge(state, 2, 3)
                if after_e is not None:
                    coeff[1][key] += 1
                    if merge(after_e, 2, 3) is not None:
                        coeff[3][key] += 1
                if after_f is not None:
                    coeff[2][key] += 1
                return
            walk(index + 1, state, spoke_count)
            included = merge(state, *spokes[index])
            if included is not None:
                walk(index + 1, included, spoke_count + 1)

        walk(0, parent, 0)
    return coeff


def evaluate(coeff, a, p, q, r):
    answer = []
    for polynomial in coeff:
        total = Fraction(0)
        for (spokes, core_mask), multiplicity in polynomial.items():
            weight = multiplicity * a ** spokes
            for j, value in enumerate((p, q, r)):
                if core_mask >> j & 1:
                    weight *= value
            total += weight
        answer.append(total)
    return answer


def bridge_formula(terminal_activities, p, q, r):
    """Independent core-component enumeration, allowing heterogeneous twins."""
    prefactor = Fraction(1)
    us, vs = [], []
    for a in terminal_activities:
        d = 1 + 3 * a
        prefactor *= d
        us.append(a * a / d)
        vs.append(a ** 3 / d)
    X = p + q + r
    S, L = 1 + X + p*q + p*r + q*r, 3 + 2*X
    pair_sum = sum(us[i]*us[j] for i in range(len(us)) for j in range(i))
    return prefactor * (S + L*sum(us) + sum(vs) + 6*pair_sum)


def certificate(m, a, p, q, r):
    d, X = 1 + 3*a, p + q + r
    t = p*q + p*r + q*r
    G = d*d*(3 + 6*X + 4*X*X - 6*t) + 6*a*d*(1 + m*a)*(3 + 2*X)
    G += 9*a*a + 30*m*a**3 + 18*m*m*a**4
    return 4*a**4*d**(2*m - 8)*G


def string_row(m, a, p, q, r, values):
    return dict(m=m, a=str(a), core=[str(p),str(q),str(r)],
                A_Be_Bf_C=[str(x) for x in values],
                rayleigh=str(values[1]*values[2]-values[0]*values[3]))


def main():
    report = dict(status="PASS", method="Exact integer monomial enumeration of the original graph", direct=[], formula_checks=[])
    a_values = [Fraction(1,10), Fraction(2,3), Fraction(1), Fraction(3)]
    cores = [(0,0,0), (0,0,7), (0,3,1), (2,3,5), (Fraction(1,5),Fraction(7,3),Fraction(11,7))]
    for m in (4,5):
        coeff = original_coefficients(m)
        assert coeff[1] == coeff[2]
        report.setdefault("unweighted_subset_counts", {})[str(m)] = [sum(c.values()) for c in coeff]
        for a in a_values:
            for p,q,r in cores:
                p,q,r = map(Fraction,(p,q,r))
                actual = evaluate(coeff,a,p,q,r)
                expected = [bridge_formula([a]*m,p,q,r),
                            bridge_formula([2*a]+[a]*(m-2),p,q,r),
                            bridge_formula([2*a]+[a]*(m-2),p,q,r),
                            bridge_formula([2*a,2*a]+[a]*(m-4),p,q,r)]
                assert actual == expected
                assert actual[1]*actual[2]-actual[0]*actual[3] == certificate(m,a,p,q,r) > 0
                report["direct"].append(string_row(m,a,p,q,r,actual))
    for m in (4,5,6,9,25,100,250):
        for a in (Fraction(1,100),Fraction(2,3),Fraction(7)):
            for p,q,r in ((Fraction(0),Fraction(0),Fraction(0)),
                          (Fraction(1,5),Fraction(7,3),Fraction(11,7))):
                A = bridge_formula([a]*m,p,q,r)
                B = bridge_formula([2*a]+[a]*(m-2),p,q,r)
                C = bridge_formula([2*a,2*a]+[a]*(m-4),p,q,r)
                assert B*B-A*C == certificate(m,a,p,q,r) > 0
                report["formula_checks"].append(dict(m=m,a=str(a),core=list(map(str,(p,q,r)))))
    report["direct_cases"] = len(report["direct"])
    report["formula_cases"] = len(report["formula_checks"])
    target = Path(__file__).with_name("three_core_twins_ant_independent_checks.json")
    target.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k not in ("direct","formula_checks")},indent=2))


if __name__ == "__main__":
    main()
