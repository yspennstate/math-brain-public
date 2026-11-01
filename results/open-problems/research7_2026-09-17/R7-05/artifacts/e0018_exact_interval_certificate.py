"""Exact interval certificate for R7-05 / E0018.

Extends e0018_exact_three_rate_certificate.py from three certified rates
to three nondegenerate rational rate intervals.  For a fixed corrector the
signed residual is affine in the switching rate r.  Therefore positivity at
both interval endpoints implies positivity at every intermediate rate.

All endpoint checks use exact rational arithmetic and exact Sturm root counts.
"""
from pathlib import Path
import importlib.util
import sympy as sp

BASE = Path(__file__).with_name("e0018_exact_three_rate_certificate.py")
spec = importlib.util.spec_from_file_location("e0018_base", BASE)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

T = base.T
QQ = sp.Rational

INTERVALS = {
    "left_lower": (QQ(499, 10000), QQ(501, 10000)),
    "middle_upper": (QQ(999, 1000), QQ(1001, 1000)),
    "right_lower": (QQ(9999, 1000), QQ(10001, 1000)),
}


def cleared_residual(data, r, mode):
    K = data["K"]
    C, S = base.cs_table(K)
    phi0, dphi0 = base.build_phi(data["mode0"], sp.Integer(0), C, S)
    phi1, dphi1 = base.build_phi(data["mode1"], data["c1"], C, S)
    phis = [phi0, phi1]
    dphis = [dphi0, dphi1]
    a, b = base.radial_angular((base.B0, base.B1)[mode])
    f = sp.factor(a + b * dphis[mode] + r * (phis[1 - mode] - phis[mode]))
    residual = f - base.H if data["sense"] == "lower" else base.H - f
    return sp.Poly(
        sp.expand(sp.cancel(residual * (1 + T**2) ** (K + 1))),
        T,
        domain=sp.QQ,
    )


def check_endpoint(name, endpoint_name, r):
    data = base.CASES[name]
    for mode in (0, 1):
        P = cleared_residual(data, r, mode)
        nreal = P.count_roots(-sp.oo, sp.oo)
        vm, _ = base.sturm_variations_at_infinity(P, positive=False)
        vp, _ = base.sturm_variations_at_infinity(P, positive=True)
        assert nreal == 0
        assert vm == vp
        assert P.eval(0) > 0
        assert P.LC() > 0
        print(
            f"{name} {endpoint_name}: r={r}, mode={mode}, degree={P.degree()}, "
            f"real_roots={nreal}, V(-inf)={vm}, V(+inf)={vp}, "
            f"P(0)={P.eval(0)}, LC={P.LC()}"
        )


if __name__ == "__main__":
    for name, (lo, hi) in INTERVALS.items():
        check_endpoint(name, "lo", lo)
        check_endpoint(name, "hi", hi)
        print(
            f"AFFINE-IN-r STEP: the same signed residual is affine in r, so strict "
            f"positivity at r={lo} and r={hi} implies strict positivity for every "
            f"r in [{lo},{hi}]."
        )

    print("PASS")
    print("For A_i=B_i-(1/3)I:")
    print("  lambda_A(r)>0 for every r in [499/10000,501/10000].")
    print("  lambda_A(r)<0 for every r in [999/1000,1001/1000].")
    print("  lambda_A(r)>0 for every r in [9999/1000,10001/1000].")
    print("Hence the unstable-rate set contains two separated nondegenerate intervals.")
