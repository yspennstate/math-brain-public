"""Narrow numerical consistency guard; passing is never a dimension proof."""
from math import isclose, isfinite, sqrt


def check_parameters(gamma, dimension, xi, q=None, crossing_exponent=None, tolerance=1e-10):
    values = [gamma, dimension, xi] + ([q] if q is not None else []) + ([crossing_exponent] if crossing_exponent is not None else [])
    errors = []
    if not all(isfinite(x) for x in values) or not (0 < gamma < 2 and dimension > 0 and xi > 0):
        return {"consistent": False, "errors": ["Requires finite subcritical gamma, positive dimension, and positive xi."], "proof_status": "not a proof"}
    same = lambda x, y: isclose(x, y, rel_tol=tolerance, abs_tol=tolerance)
    canonical_q = 2 / gamma + gamma / 2
    if not same(xi * dimension, gamma):
        errors.append("Canonical normalization requires xi * d_gamma = gamma.")
    if q is not None and not same(q, canonical_q):
        errors.append("Background charge requires Q = 2/gamma + gamma/2.")
    if crossing_exponent is not None and not same(crossing_exponent, 1 - xi * canonical_q):
        errors.append("Epsilon-normalized LFPP requires lambda(xi) = 1 - xi*Q.")
    if same(gamma, sqrt(8 / 3)) and not same(dimension, 4):
        errors.append("The Brownian parameter has the known value d_sqrt(8/3) = 4.")
    return {"consistent": not errors, "errors": errors, "proof_status": "parameter consistency only; d_gamma not proved"}
