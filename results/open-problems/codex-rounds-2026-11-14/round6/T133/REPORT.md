VERDICT: PROVED C2 simple closed strictly convex completion of the candidate curve at Delta = 1/sqrt(2), for all weight ratios

New beyond round 5: the four candidate arcs meet at exactly four contacts
with the square, their tangent speeds are nonzero, and their geometric
curvatures match. Their union is a regular C2 simple closed curve with
positive curvature everywhere. It bounds a strictly convex set and has
an injective inward normal collar of positive width for each fixed weight
ratio. At equal weights the curve is not C3 at the contacts.

This is a deterministic geometry theorem. It does not prove T133 or
extend the Fredholm critical-parameter charts through the contacts.

[PROOF.md](PROOF.md) supplies the argument. With delta=3pi/4,
h=4/3 and T=delta-u, the southern contact is (k,0), where

`k = sin(u)sin(T)/sin(delta) * [cot(T)-h cot(hT)]`.

The exact identity k(u)+k(T)=1 matches all four joins. Dividing the
tangent-line equation by its singular coefficient removes its pole.
The remaining endpoint-speed sign reduces to a degree-8 polynomial;
its positive-quadrant transform has coefficients

`21, 357, 2191, 6930, 12688, 13860, 8764, 2856, 336`.

A symmetric expression for the endpoint curvature proves matching
independently of the rational calculation. Monotone arc coordinates and
strict chord inequalities exclude intersections. The normal collar follows
from compactness and the inverse function theorem.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_certificate.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B derive_joins.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_joins.py
```

The first command rechecks round 5's full curvature certificate, using its
integer verifier and certificate copied byte for byte into this folder.
It passes with the earlier coefficient sum 17765219441341512. The new
endpoint-speed identity is also checked in full with standard-library
integer polynomial arithmetic. Independent Fraction-series reconstruction
passes 29 endpoint-jet checks. Ten high-precision checks using the original
trigonometric formulas include both weight edges; the maximum relative
endpoint-limit error is 2.61e-12. The third derivative at equal weights
is checked separately from the original formulas, with absolute limit
error 5.20e-12. Commands, material output and failures are in
[LOG.md](LOG.md); formulas and audit data are in
[endpoint_formulas.json](endpoint_formulas.json) and
[join_checks.json](join_checks.json).

Runs took at most 26 seconds and used under 80 MiB measured peak RSS,
with one thread configured. Effective nice was 20; the shell could not
raise it to the requested 15. All new files remain in this folder, and
earlier files were read only.

What failed: an initial auxiliary third-derivative series formula missed
a chain-rule factor. It was corrected and checked against the independently
derived rational jets. No contact or curvature result depended on that
formula. A stronger analytic or C3 gluing claim fails: at equal weights,
the southwest third graph derivative is
`-(4168422 sqrt(2)+494262)/1803649`, while reflection reverses its sign.

Literature: the bounded check found no changed status beyond Alexey
Bufetov's [arXiv:2609.20576v1](https://arxiv.org/abs/2609.20576), an
announcement omitting 1/2<Delta<1. No wider absence or priority claim
is made.

Unresolved: uniform Fredholm endpoint asymptotics, gluing of its actual
critical-parameter collars, distant critical points, other Delta values,
and probabilistic convergence. The normal collar proved here is geometric.
No antiferroelectric result or weight-uniform collar width is asserted.

Next worker: analyze the joint limit B->0 and theta->T at gamma=pi/4.
The original coefficient b develops a pole even though its B=0 envelope
regularizes. Determine the correct scaled variables and whether the
piecewise Fredholm formulas give a one-to-one collar at a contact.
The explicit positive endpoint speed and matching curvature above are
boundary data for that analysis; they do not supply its uniform estimates.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 11:03 Asia/Tbilisi.
