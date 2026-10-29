# Re-certification of the six sigma 0.5 certificates with an exact cover (agent A, 19 Oct 2026). The original loop builds
# each ball as arb((lo+hi)/2, (hi-lo)/2); the float midpoint is rounded, and in 4 of the 5 sigma 0.5 argv sets some sub-interval
# endpoints fall outside their ball by up to 2.2e-16. Here each ball is arb(lo).union(arb(hi)), which contains [lo, hi] exactly,
# with the same K / J functions, the same intervals and ball counts as the peer's run_*.cmd launchers. The gain is
# sum (hi - lo) x lower(S - A) over the exact cover.
import sys, importlib; sys.path.insert(0, 'agent_B')
from flint import arb
RUNS = [('KL', 'PQ', -1.4000001, -1.3999999, 20), ('KL', 'QP', -1.0000001, -0.9999999, 20),
        (2, 'PQ', -1.9000000001, -1.8999999999, 10), (3, 'PQ', -2.350000000001, -2.349999999999, 10),
        (2, 'QP', -0.50000001, -0.49999999, 20), (3, 'QP', -0.50000001, -0.49999999, 20)]
km = rm = None
for al, d, a, b, n in RUNS:
    qp = d == 'QP'
    if al == 'KL':
        sys.argv = ['x', '0.5']; km = importlib.reload(km) if km else importlib.import_module('cert_kl_arb_sigma'); F = lambda g, s: km.K(g, s, qp)
    else:
        sys.argv = ['x', '0.5', str(al), d]; rm = importlib.reload(rm) if rm else importlib.import_module('cert_renyi_arb_sigma'); F = lambda g, s: rm.J(g, s, qp)
    ok, gain, minlo = True, arb(0), None
    for i in range(n):
        lo, hi = a + (b - a) * i / n, a + (b - a) * (i + 1) / n
        g = arb(lo).union(arb(hi)); assert g.contains(arb(lo)) and g.contains(arb(hi))
        dd = F(g, True) - F(g, False)
        if not dd > 0: ok = False; print(f"{al} {d} ball {i} NOT certified: {dd.str(5)}", flush=True); break
        gain += (arb(hi) - arb(lo)) * arb(dd.lower()); minlo = dd.lower() if minlo is None else min(minlo, dd.lower())
    print(f"{al} {d} [{a!r}, {b!r}] n {n}: {'CERTIFIED' if ok else 'FAILED'} exact cover, min lower {arb(minlo).str(5) if minlo is not None else '-'}, gain >= {gain.lower().str(6)}", flush=True)
