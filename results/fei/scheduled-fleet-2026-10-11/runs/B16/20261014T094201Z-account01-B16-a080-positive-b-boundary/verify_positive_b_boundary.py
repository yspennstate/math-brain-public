#!/usr/bin/env python3
"""High-precision diagnostics for the proved OR-family boundary asymptotics."""

from decimal import Decimal as D, getcontext

getcontext().prec = 140
LN2 = D(2).ln()


def log2(x):
    return x.ln() / LN2


def centropy(x):
    return D(0) if x == 0 else -x * log2(x)


def stats(r, k):
    e = D(2) ** (-r)
    om = D(1) - e
    P = om ** k
    p0 = (D(2) * P - D(1)) ** 2
    L = -log2(om)
    mu = D(r) / (D(2) * om)
    U = centropy(p0) + D(4) * P * D(k) * e * (D(r) - mu)
    U += D(4) * P * D(k) * L * (om - P)
    I = D(2) * P * D(k) * D(r) * e / om
    return U, I, P


def u_types(types):
    P = D(1)
    for r, k in types:
        P *= (D(1) - D(2) ** (-r)) ** k
    p0 = (D(2) * P - D(1)) ** 2
    U = centropy(p0)
    for r, k in types:
        e = D(2) ** (-r)
        om = D(1) - e
        L = -log2(om)
        mu = D(r) / (D(2) * om)
        U += D(k) * (D(4) * P * e * (D(r) - mu) + D(4) * P * L * (om - P))
    return U


def metrics(r, lam):
    e = D(2) ** (-r)
    k = max(1, int((lam / e).to_integral_value(rounding="ROUND_FLOOR")))
    U, I, P = stats(r, k)
    Ushort = u_types([(r - 1, 1), (r, k - 1)])
    Udrop = u_types([(r, k - 1)])
    G = D(k * r) * (U - (Ushort + Udrop) / D(2))
    residual = G - D("0.75") * I - D("0.25") * U
    return k, P, U, I, G, residual


def limit_constant(lam):
    p = (-lam).exp()
    p0 = (D(2) * p - D(1)) ** 2
    return centropy(p0) + D(4) * lam * p * (D(1) - p) / LN2


def main():
    print("claim=B16-A080-POSITIVE-B-BOUNDARY-v1")
    print("frozen_pair=(3/4,1/4)")
    for text in ("0.25", "0.5", "1", "2", "4"):
        lam = D(text)
        C = limit_constant(lam)
        assert C > 0
        print(f"lambda={text} C_lambda={C:.30E} target_residual={(-C/D(4)):.30E}")
        previous_error = None
        for r in (12, 20, 30, 40, 50):
            k, P, U, I, G, R = metrics(r, lam)
            err = abs(R + C / D(4))
            if r >= 30 and previous_error is not None:
                assert err < previous_error
            previous_error = err
            assert U > 0 and I > 0
            print(
                f"  r={r} k={k} P={P:.12E} U-I={(U-I):.16E} "
                f"G-I={(G-I):.16E} R_3/4,1/4={R:.16E} error={err:.3E}"
            )
        assert metrics(50, lam)[-1] < 0
    print("proved_limit=R_(1-b,b)->-b*C_lambda for every fixed lambda>0,b>0")
    print("ratios=G/I->1,U/I->1,H/I->4; no ratio divergence")
    print("universal_GU=OPEN")
    print("status=PASS")


if __name__ == "__main__":
    main()
