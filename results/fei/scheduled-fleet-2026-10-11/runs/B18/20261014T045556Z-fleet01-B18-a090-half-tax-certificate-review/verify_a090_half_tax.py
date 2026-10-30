#!/usr/bin/env python3
"""Independent formula reconstruction and interval repair for B10/A047."""

from decimal import Decimal as D, getcontext
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

getcontext().prec = 90
ZERO, ONE, TWO, FOUR = D(0), D(1), D(2), D(4)


def workspace_root():
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "reports/fei-2026-10-11/runs/B10").is_dir():
            return parent
    raise RuntimeError("workspace root not found")


ROOT = workspace_root()
SOURCES = [
    ROOT / "reports/fei-2026-10-11/runs/B10/20261013T072840Z-fleet01-B10-a047-half-tax-compact-core/certify_compact_core.py",
    ROOT / "reports/fei-2026-10-11/runs/B10/20261013T195919Z-fleet01-B10-a047-endpoint-collars/certify_endpoint_collars.py",
]


def h(x):
    if x == ZERO or x == ONE:
        return ZERO
    return -(x * x.ln() + (ONE - x) * (ONE - x).ln()) / TWO.ln()


def e(x):
    if x == ZERO:
        return ZERO
    return -x * x.ln() / TWO.ln()


def formula_audit():
    max_error = ZERO
    cases = 0
    # Interior rational biases, plus exact q endpoints handled separately by
    # the interval checker.  This reconstructs M and J from the four squared
    # product-biased Fourier masses, not from B10's reduced formulas.
    points = [D(k) / D(32) for k in range(1, 16)]
    for p in points:
        for q in points + [ONE - x for x in points]:
            mu0 = (ONE - TWO * p * q) ** 2
            mux = FOUR * q * q * p * (ONE - p)
            muy = FOUR * p * p * q * (ONE - q)
            muxy = FOUR * p * (ONE - p) * q * (ONE - q)
            total = mu0 + mux + muy + muxy
            assert abs(total - ONE) < D("1e-80")

            sy = muy + muxy
            direct_M = sum(e(z) for z in (mu0, mux, muy, muxy)) - h(sy)
            s = FOUR * q * (ONE - q)
            direct_J = h(sy) - p * h(s)

            b = ONE - s * p
            c = FOUR * q * q
            a = c * p * (ONE - p) / b
            closed_M = b * h(a) + s * p * h(p)
            closed_J = h(s * p) - p * h(s)
            err = max(abs(direct_M - closed_M), abs(direct_J - closed_J))
            max_error = max(max_error, err)
            cases += 1
    assert max_error < D("1e-80")
    print(f"formula_reconstruction_cases={cases}")
    print(f"maximum_formula_error={max_error}")


def load(path, name):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def install_repaired_h_point(m):
    def h_point(x):
        if x == m.ZERO or x == m.ONE:
            return m.ZERO, m.ZERO
        lx = m.log2_point(x)
        complement = (m.dn(lambda: m.ONE - x), m.up(lambda: m.ONE - x))
        l1 = (
            m.log2_point(complement[0])[0],
            m.log2_point(complement[1])[1],
        )
        z = m.add(m.mul((x, x), lx), m.mul(complement, l1))
        return -z[1], -z[0]

    m.h_point = h_point


def certificate_audit():
    import decimal
    print(f"formula_audit_decimal_precision={decimal.getcontext().prec}")
    # Restore the process default used by the original scripts, so the audit
    # explicitly reproduces their hidden 28-digit context before monkeypatch.
    decimal.getcontext().prec = 28
    print(f"original_import_decimal_precision={decimal.getcontext().prec}")
    for index, path in enumerate(SOURCES):
        print(f"audited_source={path.relative_to(ROOT)}")
        m = load(path, f"b10_source_{index}")
        install_repaired_h_point(m)
        m.main()


def main():
    formula_audit()
    certificate_audit()
    print("A090 independent repair audit: PASS")
    print("verdict=published scripts formally defective; repaired claim holds")
    print("scope=two-bit half-tax on p in [1/64,49/100], all q")


if __name__ == "__main__":
    main()
