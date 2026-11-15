VERDICT: PROVED positive curvature on every open candidate arc at Delta = 1/sqrt(2), for all weight ratios

This is a deterministic theorem about the candidate formulas, proved by
an exact integer certificate. It does not prove T133 or identify a
probabilistic liquid region.

New beyond round 4: at gamma=pi/4, the sign
`C(theta)=x0 a''+y0 b''-e'' > 0` holds for every
`0<u<3pi/4` and `|theta|<3pi/4-u`. Thus it includes the previously
missing weights u<gamma and the entire open southwest arc. The arc is an
embedded strictly convex graph, with x0'>0, y0'<0 and
`d²y/dx²=W²/(C b³)>0`. Reflection and u↔T give the other three open arcs.
The small-B critical branch gives a locally convex-side collar at every
interior point, with injectivity uniform on compact subarcs. Distant
critical points are not excluded.

[PROOF.md](PROOF.md) gives the complete reduction. Setting
`x=tan((T+theta)/6)`, `y=tan((T-theta)/6)` turns the domain into
`x,y>0, x+y+xy<1` and the curvature numerator into positive elementary
factors times a symmetric polynomial Q. The substitution
`x=r/(1+r)`, `y=s/((1+s)(1+2r))` turns Q, after clearing positive
denominators, into a polynomial R with 324 positive coefficients and
zero constant term. In fact `R(r,s)>=63(r+s)>0`.

The full coefficient arrays are in [certificate.json](certificate.json).
The rational identity and every coefficient sign are independently checked
by [audit_certificate.py](audit_certificate.py), using standard-library
integer arithmetic. This check shares no symbolic algebra implementation
with the SymPy derivation. Both give coefficient sum 17765219441341512
and maximum coefficient 692394213766656; these checksums are supplementary
to equality of every coefficient.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 derive_certificate.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_certificate.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_geometry.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_branch.py
```

The earlier midpoint result passes 25 independent derivative/decomposition
checks. The new formula passes 63 comparisons with derivatives of the
original trigonometric coefficients, including near parameter edges.
Four direct finite-B computations enter the convex side and recover the
quadratic displacement, with relative extrapolation error at most
7.66e-6. Detailed commands and output are in [LOG.md](LOG.md). Runs take
under seven seconds each, configure one thread, use under 74 MiB measured
peak RSS, and confirm effective nice 20.

What failed: the general midpoint decomposition still has a negative
summand at u<gamma; no general-parameter sign proof was obtained. The
independent numerator audit initially used an insufficient common
denominator; its assertion caught this and the power was corrected.
Near simultaneous parameter edges, 100-digit evaluation lost enough
precision to fail the numerical identity tolerance; 160 digits passed
without relaxing it. These failures and two exploratory SymPy Boolean
counting errors are recorded in LOG.md. The shell cannot raise inherited
nice 20 to 15.

Literature: the bounded check found no later complete solution. Alexey
Bufetov's [arXiv:2609.20576v1](https://arxiv.org/abs/2609.20576) still
announces results with 1/2<Delta<1 omitted. No absence claim beyond that
search is made.

Remaining gaps: other Delta values, joining-point control, global
critical-point classification, and convergence of the random model.
No antiferroelectric extension is claimed. No literature priority is
claimed for the deterministic geometry lemma.

Next worker: use the rational formulas at gamma=pi/4 to compute and match
the four joining-point limits, then determine whether these open-arc
collars combine into a collar of a simple closed convex candidate curve.
For a parameter extension, seek a positive representation of C for
general gamma; the all-positive polynomial here supplies an exact
special-case check for such a representation.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 08:29 Asia/Tbilisi.
