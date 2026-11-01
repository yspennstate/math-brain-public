"""Exact algebra for worker 060's three parental-leakage claims.

The proofs of the continuum claims are in agents/060.md. These checks verify
the rational constants, the analytically reduced weighted-minimum lemma, and
the symbolic coefficient family demonstrating sharpness from above at 1/2.
No numerical optimization is used here.
"""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path


class Laurent:
    """Tiny exact Laurent-polynomial implementation in the parameter eta."""
    def __init__(self, value=0):
        raw = value.terms if isinstance(value, Laurent) else (value if isinstance(value, dict) else {0: value})
        self.terms = {k: F(v) for k, v in raw.items() if v}

    def __add__(self, other):
        other = Laurent(other)
        result = dict(self.terms)
        for k, v in other.terms.items():
            result[k] = result.get(k, 0)+v
        return Laurent(result)

    __radd__ = __add__

    def __neg__(self):
        return Laurent({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-Laurent(other))

    def __rsub__(self, other):
        return Laurent(other) + (-self)

    def __mul__(self, other):
        other = Laurent(other)
        result = {}
        for k, v in self.terms.items():
            for j, w in other.terms.items():
                result[k+j] = result.get(k+j, 0)+v*w
        return Laurent(result)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self*F(1, other)

    def __eq__(self, other):
        return self.terms == Laurent(other).terms

    def at(self, eta):
        return sum(v*eta**k for k, v in self.terms.items())

    def __str__(self):
        return " + ".join(f"({v})*eta^{k}" for k, v in sorted(self.terms.items())) or "0"


def text(x):
    return str(x)


def main():
    d = F(7, 50)
    q = F(17, 40)
    eps = (1 - 2*d)/(3 - 2*d)
    r = 1 - 2*q
    cap_slack = q - (d + (1-d)*(1-q)**2)
    assert eps == F(9, 34)
    assert r == F(3, 20)
    assert cap_slack == F(53, 80000)

    vertices = sorted(set(itertools.permutations([q, q, r, F(0)])))
    weighted_min_values = []
    for m in vertices:
        for alpha, beta in itertools.product([eps, 1-eps], repeat=2):
            ap = [alpha, 1-alpha]
            bp = [beta, 1-beta]
            value = sum(ap[i]*bp[j]*min(m[i], m[j+2])
                        for i in range(2) for j in range(2))
            assert value >= eps*r
            weighted_min_values.append(value)
    assert min(weighted_min_values) == eps*r == F(27, 680)
    transfer = d+(1-d)*q-d*eps*r
    assert transfer == F(8499, 17000)
    assert 2*transfer == F(8499, 8500) < 1

    # Parent rows use zero-based labels. The fourth type is index 3.
    eta = Laurent({1: 1})
    eta_inverse = Laurent({-1: 1})
    rows = {}
    for i in range(4):
        for j in range(i, 4):
            row = [Laurent() for _ in range(4)]
            if j < 3:
                if i == j:
                    for k in range(3):
                        if k != i:
                            row[k] = Laurent(F(1, 2))
                else:
                    row[next(k for k in range(3) if k not in {i, j})] = Laurent(1)
            elif i < 3:
                row[3] = eta
                for k in range(3):
                    if k != i:
                        row[k] = (1-eta)/2
            else:
                row[3] = eta
                for k in range(3):
                    row[k] = (1-eta)/3
            assert sum(row)-1 == 0
            # Every coefficient is affine in eta; endpoint nonnegativity
            # therefore certifies nonnegativity throughout 0 <= eta <= 1.
            assert all(set(v.terms) <= {0, 1} for v in row)
            assert all(v.terms.get(0, 0) >= 0 and v.at(F(1)) >= 0 for v in row)
            leakage = sum(row[k] for k in {i, j})
            assert leakage - (eta if j == 3 else 0) == 0
            rows[(i, j)] = row

    # These exact coefficients identify the full fourth-coordinate polynomial.
    assert all(row[3] == (eta if j == 3 else 0) for (i, j), row in rows.items())
    p = [Laurent(F(1, 3))]*3+[Laurent()]
    other = [(eta_inverse-1)/3]*3+[2-eta_inverse]
    for point in [p, other]:
        assert sum(point)-1 == 0
        output = [Laurent() for _ in range(4)]
        for (i, j), row in rows.items():
            for k in range(4):
                output[k] += (1 if i == j else 2)*row[k]*point[i]*point[j]
        assert all(output[k]-point[k] == 0 for k in range(4))

    numeric_eta = F(3, 5)
    numeric_other = [v.at(numeric_eta) for v in other]
    assert numeric_other == [F(2, 9)]*3+[F(1, 3)]
    output = {
        "all_exact_checks_passed": True,
        "uniform_uniqueness": {
            "leakage": text(d), "coordinate_cap": text(q),
            "cap_slack": text(cap_slack), "sign_weight_lower_bound": text(eps),
            "cap_vertices": len(vertices),
            "weighted_minimum_corner_checks": len(weighted_min_values),
            "weighted_minimum": text(min(weighted_min_values)),
            "transfer_upper_bound": text(transfer),
            "fixed_point_difference_factor": text(2*transfer),
        },
        "sharpness_family": {
            "parameter_domain": "1/2 < eta < 1",
            "parent_rows_one_based": {
                f"{i+1}{j+1}": [text(v) for v in row]
                for (i, j), row in rows.items()
            },
            "total_parental_leakage": "eta",
            "fourth_coordinate_on_simplex": "eta*x4*(2-x4)",
            "boundary_fixed_point": [text(v) for v in p],
            "interior_fixed_point": [text(v) for v in other],
            "rational_example_eta": text(numeric_eta),
            "rational_example_second_fixed_point": [text(v) for v in numeric_other],
        },
        "scope": "Exact algebra and finite reduction certificate; full analytic proofs are in agents/060.md. No contraction theorem at leakage 7/50 is asserted.",
    }
    target = Path("computations/060_exact_certificates_output.json")
    target.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
