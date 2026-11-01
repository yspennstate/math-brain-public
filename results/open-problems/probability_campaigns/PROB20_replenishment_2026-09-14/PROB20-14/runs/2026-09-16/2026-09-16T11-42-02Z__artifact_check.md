# PROB20-14 — artifact execution certificate

Checker:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/canonical_deletion_identity_check_20260916.py`

- creation commit: `d48c856163cbeb57532865ccaf0031c3392a73ec`
- exact-commit readback blob: `031515b56cd6daf58abeb0e0d01e71a546697522`

Purpose: finite-support algebra/indexing check only.  This is **not** evidence for the arbitrary infinite-variance theorem or for Theorem 5.1's infinite lacunary construction.

Test law:
\[
\Pr(\xi=0)=1/2,\qquad \Pr(\xi=1)=1/4,\qquad \Pr(\xi=3)=1/4.
\]
It is critical and span one.

The executed cases were `(m,b)=(4,1),(8,1),(8,2),(10,3),(20,1),(20,5)`.  The `(4,1)` case exercises both endpoint conventions in the append-only correction: `b'=0` at `d=0` and `b'=N` at `d=3`.

Execution output:

```text
m= 4 b= 1 checked_d=3 max_identity_gap=6.661e-16 decomposition_gap=4.441e-16
m= 8 b= 1 checked_d=3 max_identity_gap=2.359e-16 decomposition_gap=4.441e-16
m= 8 b= 2 checked_d=3 max_identity_gap=7.633e-16 decomposition_gap=4.441e-16
m=10 b= 3 checked_d=3 max_identity_gap=2.880e-16 decomposition_gap=4.441e-16
m=20 b= 1 checked_d=3 max_identity_gap=6.575e-16 decomposition_gap=0.000e+00
m=20 b= 5 checked_d=3 max_identity_gap=1.655e-15 decomposition_gap=8.882e-16
ALL_ASSERTIONS_PASSED
```

The checked identities are
\[
\log\frac{\mu_{m,b}(d)}{P_{m,b}(d)}
=
c_{m,b}-c_{m-1,b+d-1}-(m-1)D(P_{m-1,b+d-1}\|P_{m,b})
\]
(with the corrected endpoint canonical references), and
\[
c_{m,b}
=
D(\mu_{m,b}\|P_{m,b})
+\mathbb E_{\mu_{m,b}}c_{m-1,b+\xi-1}
+\mathbb E_{\mu_{m,b}}J_{m,b}(\xi).
\]

All assertions passed to floating precision.